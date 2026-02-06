# Generated from d:/PPL/tyc-compiler/src/grammar/TyC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TyCParser import TyCParser
else:
    from TyCParser import TyCParser

# This class defines a complete listener for a parse tree produced by TyCParser.
class TyCListener(ParseTreeListener):

    # Enter a parse tree produced by TyCParser#list_expression.
    def enterList_expression(self, ctx:TyCParser.List_expressionContext):
        pass

    # Exit a parse tree produced by TyCParser#list_expression.
    def exitList_expression(self, ctx:TyCParser.List_expressionContext):
        pass


    # Enter a parse tree produced by TyCParser#expression.
    def enterExpression(self, ctx:TyCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by TyCParser#expression.
    def exitExpression(self, ctx:TyCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by TyCParser#expression1.
    def enterExpression1(self, ctx:TyCParser.Expression1Context):
        pass

    # Exit a parse tree produced by TyCParser#expression1.
    def exitExpression1(self, ctx:TyCParser.Expression1Context):
        pass


    # Enter a parse tree produced by TyCParser#expression2.
    def enterExpression2(self, ctx:TyCParser.Expression2Context):
        pass

    # Exit a parse tree produced by TyCParser#expression2.
    def exitExpression2(self, ctx:TyCParser.Expression2Context):
        pass


    # Enter a parse tree produced by TyCParser#expression3.
    def enterExpression3(self, ctx:TyCParser.Expression3Context):
        pass

    # Exit a parse tree produced by TyCParser#expression3.
    def exitExpression3(self, ctx:TyCParser.Expression3Context):
        pass


    # Enter a parse tree produced by TyCParser#expression4.
    def enterExpression4(self, ctx:TyCParser.Expression4Context):
        pass

    # Exit a parse tree produced by TyCParser#expression4.
    def exitExpression4(self, ctx:TyCParser.Expression4Context):
        pass


    # Enter a parse tree produced by TyCParser#expression5.
    def enterExpression5(self, ctx:TyCParser.Expression5Context):
        pass

    # Exit a parse tree produced by TyCParser#expression5.
    def exitExpression5(self, ctx:TyCParser.Expression5Context):
        pass


    # Enter a parse tree produced by TyCParser#expression6.
    def enterExpression6(self, ctx:TyCParser.Expression6Context):
        pass

    # Exit a parse tree produced by TyCParser#expression6.
    def exitExpression6(self, ctx:TyCParser.Expression6Context):
        pass


    # Enter a parse tree produced by TyCParser#function_call.
    def enterFunction_call(self, ctx:TyCParser.Function_callContext):
        pass

    # Exit a parse tree produced by TyCParser#function_call.
    def exitFunction_call(self, ctx:TyCParser.Function_callContext):
        pass


    # Enter a parse tree produced by TyCParser#list_literal.
    def enterList_literal(self, ctx:TyCParser.List_literalContext):
        pass

    # Exit a parse tree produced by TyCParser#list_literal.
    def exitList_literal(self, ctx:TyCParser.List_literalContext):
        pass


    # Enter a parse tree produced by TyCParser#literal.
    def enterLiteral(self, ctx:TyCParser.LiteralContext):
        pass

    # Exit a parse tree produced by TyCParser#literal.
    def exitLiteral(self, ctx:TyCParser.LiteralContext):
        pass


    # Enter a parse tree produced by TyCParser#array_lit.
    def enterArray_lit(self, ctx:TyCParser.Array_litContext):
        pass

    # Exit a parse tree produced by TyCParser#array_lit.
    def exitArray_lit(self, ctx:TyCParser.Array_litContext):
        pass


    # Enter a parse tree produced by TyCParser#program.
    def enterProgram(self, ctx:TyCParser.ProgramContext):
        pass

    # Exit a parse tree produced by TyCParser#program.
    def exitProgram(self, ctx:TyCParser.ProgramContext):
        pass


    # Enter a parse tree produced by TyCParser#variable.
    def enterVariable(self, ctx:TyCParser.VariableContext):
        pass

    # Exit a parse tree produced by TyCParser#variable.
    def exitVariable(self, ctx:TyCParser.VariableContext):
        pass


    # Enter a parse tree produced by TyCParser#function.
    def enterFunction(self, ctx:TyCParser.FunctionContext):
        pass

    # Exit a parse tree produced by TyCParser#function.
    def exitFunction(self, ctx:TyCParser.FunctionContext):
        pass


    # Enter a parse tree produced by TyCParser#list_param.
    def enterList_param(self, ctx:TyCParser.List_paramContext):
        pass

    # Exit a parse tree produced by TyCParser#list_param.
    def exitList_param(self, ctx:TyCParser.List_paramContext):
        pass


    # Enter a parse tree produced by TyCParser#param.
    def enterParam(self, ctx:TyCParser.ParamContext):
        pass

    # Exit a parse tree produced by TyCParser#param.
    def exitParam(self, ctx:TyCParser.ParamContext):
        pass


    # Enter a parse tree produced by TyCParser#all_type.
    def enterAll_type(self, ctx:TyCParser.All_typeContext):
        pass

    # Exit a parse tree produced by TyCParser#all_type.
    def exitAll_type(self, ctx:TyCParser.All_typeContext):
        pass


    # Enter a parse tree produced by TyCParser#list_statement.
    def enterList_statement(self, ctx:TyCParser.List_statementContext):
        pass

    # Exit a parse tree produced by TyCParser#list_statement.
    def exitList_statement(self, ctx:TyCParser.List_statementContext):
        pass


    # Enter a parse tree produced by TyCParser#statement.
    def enterStatement(self, ctx:TyCParser.StatementContext):
        pass

    # Exit a parse tree produced by TyCParser#statement.
    def exitStatement(self, ctx:TyCParser.StatementContext):
        pass


    # Enter a parse tree produced by TyCParser#declared_statement.
    def enterDeclared_statement(self, ctx:TyCParser.Declared_statementContext):
        pass

    # Exit a parse tree produced by TyCParser#declared_statement.
    def exitDeclared_statement(self, ctx:TyCParser.Declared_statementContext):
        pass


    # Enter a parse tree produced by TyCParser#assign_statement.
    def enterAssign_statement(self, ctx:TyCParser.Assign_statementContext):
        pass

    # Exit a parse tree produced by TyCParser#assign_statement.
    def exitAssign_statement(self, ctx:TyCParser.Assign_statementContext):
        pass


    # Enter a parse tree produced by TyCParser#lhs.
    def enterLhs(self, ctx:TyCParser.LhsContext):
        pass

    # Exit a parse tree produced by TyCParser#lhs.
    def exitLhs(self, ctx:TyCParser.LhsContext):
        pass


    # Enter a parse tree produced by TyCParser#if_statement.
    def enterIf_statement(self, ctx:TyCParser.If_statementContext):
        pass

    # Exit a parse tree produced by TyCParser#if_statement.
    def exitIf_statement(self, ctx:TyCParser.If_statementContext):
        pass


    # Enter a parse tree produced by TyCParser#for_statement.
    def enterFor_statement(self, ctx:TyCParser.For_statementContext):
        pass

    # Exit a parse tree produced by TyCParser#for_statement.
    def exitFor_statement(self, ctx:TyCParser.For_statementContext):
        pass


    # Enter a parse tree produced by TyCParser#continue_statement.
    def enterContinue_statement(self, ctx:TyCParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by TyCParser#continue_statement.
    def exitContinue_statement(self, ctx:TyCParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by TyCParser#call_statement.
    def enterCall_statement(self, ctx:TyCParser.Call_statementContext):
        pass

    # Exit a parse tree produced by TyCParser#call_statement.
    def exitCall_statement(self, ctx:TyCParser.Call_statementContext):
        pass


    # Enter a parse tree produced by TyCParser#return_statement.
    def enterReturn_statement(self, ctx:TyCParser.Return_statementContext):
        pass

    # Exit a parse tree produced by TyCParser#return_statement.
    def exitReturn_statement(self, ctx:TyCParser.Return_statementContext):
        pass


    # Enter a parse tree produced by TyCParser#block_statement.
    def enterBlock_statement(self, ctx:TyCParser.Block_statementContext):
        pass

    # Exit a parse tree produced by TyCParser#block_statement.
    def exitBlock_statement(self, ctx:TyCParser.Block_statementContext):
        pass



del TyCParser