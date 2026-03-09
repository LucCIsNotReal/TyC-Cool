"""
AST Generation module for TyC programming language.
This module contains the ASTGeneration class that converts parse trees
into Abstract Syntax Trees using the visitor pattern.
"""

from build.TyCVisitor import TyCVisitor
from src.utils.nodes import *


class ASTGeneration(TyCVisitor):
    """AST Generation visitor for TyC language."""

    def _fold_left(self, operands, operators):
        expr = operands[0]
        for op, rhs in zip(operators, operands[1:]):
            expr = BinaryOp(expr, op, rhs)
        return expr

    def visitProgram(self, ctx):
        return Program([self.visit(decl_ctx) for decl_ctx in ctx.decl()])

    def visitDecl(self, ctx):
        if ctx.struct_decl():
            return self.visit(ctx.struct_decl())
        return self.visit(ctx.func_decl())

    def visitStruct_decl(self, ctx):
        return StructDecl(
            name=ctx.ID().getText(),
            members=[self.visit(member_ctx) for member_ctx in ctx.member_decl()],
        )

    def visitMember_decl(self, ctx):
        return MemberDecl(
            member_type=self.visit(ctx.type_spec()),
            name=ctx.ID().getText(),
        )

    def visitFunc_decl(self, ctx):
        return FuncDecl(
            return_type=self.visit(ctx.return_type()) if ctx.return_type() else None,
            name=ctx.ID().getText(),
            params=self.visit(ctx.param_list()) if ctx.param_list() else [],
            body=self.visit(ctx.block_stmt()),
        )

    def visitReturn_type(self, ctx):
        if ctx.VOID():
            return VoidType()
        return self.visit(ctx.type_spec())

    def visitParam_list(self, ctx):
        return [self.visit(param_ctx) for param_ctx in ctx.param()]

    def visitParam(self, ctx):
        return Param(
            param_type=self.visit(ctx.type_spec()),
            name=ctx.ID().getText(),
        )

    def visitType_spec(self, ctx):
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        return StructType(ctx.ID().getText())

    def visitBlock_stmt(self, ctx):
        return BlockStmt([self.visit(stmt_ctx) for stmt_ctx in ctx.statement()])

    def visitStatement(self, ctx):
        if ctx.block_stmt():
            return self.visit(ctx.block_stmt())
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        if ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        if ctx.while_stmt():
            return self.visit(ctx.while_stmt())
        if ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        if ctx.switch_stmt():
            return self.visit(ctx.switch_stmt())
        if ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        if ctx.continue_stmt():
            return self.visit(ctx.continue_stmt())
        if ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        return self.visit(ctx.expr_stmt())

    def visitVar_decl(self, ctx):
        init_value = self.visit(ctx.expr()) if ctx.expr() else None
        if ctx.AUTO():
            return VarDecl(var_type=None, name=ctx.ID().getText(), init_value=init_value)
        return VarDecl(
            var_type=self.visit(ctx.type_spec()),
            name=ctx.ID().getText(),
            init_value=init_value,
        )

    def visitIf_stmt(self, ctx):
        statements = ctx.statement()
        then_stmt = self.visit(statements[0])
        else_stmt = self.visit(statements[1]) if len(statements) > 1 else None
        return IfStmt(
            condition=self.visit(ctx.expr()),
            then_stmt=then_stmt,
            else_stmt=else_stmt,
        )

    def visitWhile_stmt(self, ctx):
        return WhileStmt(
            condition=self.visit(ctx.expr()),
            body=self.visit(ctx.statement()),
        )

    def visitFor_stmt(self, ctx):
        return ForStmt(
            init=self.visit(ctx.for_init()) if ctx.for_init() else None,
            condition=self.visit(ctx.expr()) if ctx.expr() else None,
            update=self.visit(ctx.for_update()) if ctx.for_update() else None,
            body=self.visit(ctx.statement()),
        )

    def visitFor_init(self, ctx):
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        return ExprStmt(self.visit(ctx.expr()))

    def visitFor_update(self, ctx):
        return self.visit(ctx.expr())

    def visitSwitch_stmt(self, ctx):
        cases = []
        default_case = None

        for item_ctx in ctx.switch_block_item():
            if item_ctx.case_clause():
                cases.append(self.visit(item_ctx.case_clause()))
            else:
                default_case = self.visit(item_ctx.default_clause())

        return SwitchStmt(
            expr=self.visit(ctx.expr()),
            cases=cases,
            default_case=default_case,
        )

    def visitSwitch_block_item(self, ctx):
        if ctx.case_clause():
            return self.visit(ctx.case_clause())
        return self.visit(ctx.default_clause())

    def visitCase_clause(self, ctx):
        return CaseStmt(
            expr=self.visit(ctx.expr()),
            statements=[self.visit(stmt_ctx) for stmt_ctx in ctx.statement()],
        )

    def visitDefault_clause(self, ctx):
        return DefaultStmt([self.visit(stmt_ctx) for stmt_ctx in ctx.statement()])

    def visitBreak_stmt(self, ctx):
        return BreakStmt()

    def visitContinue_stmt(self, ctx):
        return ContinueStmt()

    def visitReturn_stmt(self, ctx):
        return ReturnStmt(self.visit(ctx.expr()) if ctx.expr() else None)

    def visitExpr_stmt(self, ctx):
        return ExprStmt(self.visit(ctx.expr()))

    def visitExpr(self, ctx):
        return self.visit(ctx.assignment())

    def visitAssignment(self, ctx):
        lhs = self.visit(ctx.logical_or())
        if ctx.assignment():
            return AssignExpr(lhs=lhs, rhs=self.visit(ctx.assignment()))
        return lhs

    def visitLogical_or(self, ctx):
        operands = [self.visit(child_ctx) for child_ctx in ctx.logical_and()]
        operators = [token.getText() for token in ctx.OR()]
        return self._fold_left(operands, operators)

    def visitLogical_and(self, ctx):
        operands = [self.visit(child_ctx) for child_ctx in ctx.equality()]
        operators = [token.getText() for token in ctx.AND()]
        return self._fold_left(operands, operators)

    def visitEquality(self, ctx):
        operands = [self.visit(child_ctx) for child_ctx in ctx.relational()]
        operators = [token.getText() for token in (ctx.EQ() + ctx.NEQ())]
        if len(operators) > 1:
            operators = [ctx.getChild(2 * idx + 1).getText() for idx in range(len(operands) - 1)]
        return self._fold_left(operands, operators)

    def visitRelational(self, ctx):
        operands = [self.visit(child_ctx) for child_ctx in ctx.additive()]
        operators = [ctx.getChild(2 * idx + 1).getText() for idx in range(len(operands) - 1)]
        return self._fold_left(operands, operators)

    def visitAdditive(self, ctx):
        operands = [self.visit(child_ctx) for child_ctx in ctx.multiplicative()]
        operators = [ctx.getChild(2 * idx + 1).getText() for idx in range(len(operands) - 1)]
        return self._fold_left(operands, operators)

    def visitMultiplicative(self, ctx):
        operands = [self.visit(child_ctx) for child_ctx in ctx.unary()]
        operators = [ctx.getChild(2 * idx + 1).getText() for idx in range(len(operands) - 1)]
        return self._fold_left(operands, operators)

    def visitUnary(self, ctx):
        if ctx.postfix():
            return self.visit(ctx.postfix())
        operator = ctx.getChild(0).getText()
        return PrefixOp(operator=operator, operand=self.visit(ctx.unary()))

    def visitPostfix(self, ctx):
        expr = self.visit(ctx.primary())

        for part_ctx in ctx.postfix_part():
            if part_ctx.LPAREN():
                args = self.visit(part_ctx.arg_list()) if part_ctx.arg_list() else []
                if isinstance(expr, Identifier):
                    expr = FuncCall(name=expr.name, args=args)
                else:
                    expr = FuncCall(name=str(expr), args=args)
            elif part_ctx.DOT():
                expr = MemberAccess(obj=expr, member=part_ctx.ID().getText())
            elif part_ctx.INC():
                expr = PostfixOp(operator="++", operand=expr)
            else:
                expr = PostfixOp(operator="--", operand=expr)

        return expr

    def visitPostfix_part(self, ctx):
        return ctx

    def visitArg_list(self, ctx):
        return [self.visit(expr_ctx) for expr_ctx in ctx.expr()]

    def visitPrimary(self, ctx):
        if ctx.literal():
            return self.visit(ctx.literal())
        if ctx.ID():
            return Identifier(ctx.ID().getText())
        if ctx.expr():
            return self.visit(ctx.expr())
        return self.visit(ctx.struct_literal())

    def visitLiteral(self, ctx):
        if ctx.INT_LIT():
            return IntLiteral(int(ctx.INT_LIT().getText()))
        if ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        return StringLiteral(ctx.STRING_LIT().getText())

    def visitStruct_literal(self, ctx):
        values = self.visit(ctx.expr_list()) if ctx.expr_list() else []
        return StructLiteral(values)

    def visitExpr_list(self, ctx):
        return [self.visit(expr_ctx) for expr_ctx in ctx.expr()]
