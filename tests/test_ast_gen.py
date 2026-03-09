"""
AST Generation test cases for TyC compiler.
TODO: Implement 100 test cases for AST generation
"""

from tests.utils import ASTGenerator


def test_ast_001_empty_main():
    source = "void main() {}"
    expected = "Program([FuncDecl(VoidType(), main, [], BlockStmt([]))])"
    assert str(ASTGenerator(source).generate()) == expected


def test_ast_002_struct_and_var_decl():
    source = """
struct Point { int x; int y; };
void main() { Point p; }
"""
    expected = (
        "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)]), "
        "FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p)]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected


def test_ast_003_auto_var_init_and_assignment_chain():
    source = """
void main() {
    auto a = 1;
    a = a + 2;
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(auto, a = IntLiteral(1)), "
        "ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(a), +, IntLiteral(2))))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected


def test_ast_004_if_else_and_return():
    source = """
int f(int x) {
    if (x > 0) return x;
    else return 0;
}
"""
    expected = (
        "Program([FuncDecl(IntType(), f, [Param(IntType(), x)], "
        "BlockStmt([IfStmt(if BinaryOp(Identifier(x), >, IntLiteral(0)) then "
        "ReturnStmt(return Identifier(x)), else ReturnStmt(return IntLiteral(0)))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected


def test_ast_005_while_and_prefix_update():
    source = """
void main() {
    int i = 0;
    while (i < 3) {
        ++i;
    }
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(IntType(), i = IntLiteral(0)), "
        "WhileStmt(while BinaryOp(Identifier(i), <, IntLiteral(3)) do "
        "BlockStmt([ExprStmt(PrefixOp(++Identifier(i)))]))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected


def test_ast_006_for_with_var_init_and_update():
    source = """
void main() {
    for (auto i = 0; i < 10; ++i) {
        printInt(i);
    }
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt([ForStmt(for VarDecl(auto, i = IntLiteral(0)); "
        "BinaryOp(Identifier(i), <, IntLiteral(10)); PrefixOp(++Identifier(i)) do "
        "BlockStmt([ExprStmt(FuncCall(printInt, [Identifier(i)]))]))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected


def test_ast_007_switch_case_default():
    source = """
void main() {
    auto x = 1;
    switch (x) {
        case 1:
            break;
        default:
            return;
    }
}
"""
    expected = (
        "Program([FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(auto, x = IntLiteral(1)), "
        "SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [BreakStmt()])], "
        "default DefaultStmt(default: [ReturnStmt(return)]))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected


def test_ast_008_struct_literal_and_member_postfix():
    source = """
struct Point { int x; int y; };
void main() {
    Point p = {1, 2};
    p.x++;
}
"""
    expected = (
        "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)]), "
        "FuncDecl(VoidType(), main, [], BlockStmt([VarDecl(StructType(Point), p = "
        "StructLiteral({IntLiteral(1), IntLiteral(2)})), "
        "ExprStmt(PostfixOp(MemberAccess(Identifier(p).x)++))]))])"
    )
    assert str(ASTGenerator(source).generate()) == expected
