"""
AST Generation test cases for TyC compiler.
TODO: Implement 100 test cases for AST generation
"""

from tests.utils import ASTGenerator
from src.utils.nodes import *


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

def test_001():
    source = """
void main() {
    printString("Hello, World!");
}
"""
    expected = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(
                    FuncCall("printString", [StringLiteral("Hello, World!")])
                )
            ])
        )
    ])
    assert str(ASTGenerator(source).generate()) == str(expected)

def test_002():
    source = """
int add(int x, int y) {
    return x + y;
}

int multiply(int x, int y) {
    return x * y;
}

void main() {
    auto a = readInt();
    auto b = readInt();
    
    auto sum = add(a, b);
    auto product = multiply(a, b);
    
    printInt(sum);
    printInt(product);
}
"""
    expected = Program([
        FuncDecl(
            IntType(),
            "add",
            [Param(IntType(), "x"), Param(IntType(), "y")],
            BlockStmt([
                ReturnStmt(
                    BinaryOp(Identifier("x"), "+", Identifier("y"))
                )
            ])
        ),
        FuncDecl(
            IntType(),
            "multiply",
            [Param(IntType(), "x"), Param(IntType(), "y")],
            BlockStmt([
                ReturnStmt(
                    BinaryOp(Identifier("x"), "*", Identifier("y"))
                )
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(None, "a", FuncCall("readInt", [])),
                VarDecl(None, "b", FuncCall("readInt", [])),
                VarDecl(None, "sum", FuncCall("add", [Identifier("a"), Identifier("b")])),
                VarDecl(None, "product", FuncCall("multiply", [Identifier("a"), Identifier("b")])),
                ExprStmt(FuncCall("printInt", [Identifier("sum")])),
                ExprStmt(FuncCall("printInt", [Identifier("product")]))
            ])
        )
    ])
    assert str(ASTGenerator(source).generate()) == str(expected)

def test_003():
    source = """
void main() {
    auto n = readInt();
    auto i = 0;
    
    while (i < n) {
        printInt(i);
        ++i;
    }
    
    for (auto j = 0; j < n; ++j) {
        if (j % 2 == 0) {
            printInt(j);
        }
    }
}
"""
    expected = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(None, "n", FuncCall("readInt", [])),
                VarDecl(None, "i", IntLiteral(0)),
                WhileStmt(
                    BinaryOp(Identifier("i"), "<", Identifier("n")),
                    BlockStmt([
                        ExprStmt(FuncCall("printInt", [Identifier("i")])),
                        ExprStmt(PrefixOp("++", Identifier("i")))
                    ])
                ),
                ForStmt(
                    VarDecl(None, "j", IntLiteral(0)),
                    BinaryOp(Identifier("j"), "<", Identifier("n")),
                    PrefixOp("++", Identifier("j")),
                    BlockStmt([
                        IfStmt(
                            BinaryOp(
                                BinaryOp(Identifier("j"), "%", IntLiteral(2)),
                                "==",
                                IntLiteral(0)
                            ),
                            BlockStmt([
                                ExprStmt(FuncCall("printInt", [Identifier("j")]))
                            ]),
                            None
                        )
                    ])
                )
            ])
        )
    ])
    assert str(ASTGenerator(source).generate()) == str(expected)

def test_004():
    source = """
int factorial(int n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

void main() {
    auto num = readInt();
    auto result = factorial(num);
    printInt(result);
}
"""
    expected = Program([
        FuncDecl(
            IntType(),
            "factorial",
            [Param(IntType(), "n")],
            BlockStmt([
                IfStmt(
                    BinaryOp(Identifier("n"), "<=", IntLiteral(1)),
                    BlockStmt([
                        ReturnStmt(IntLiteral(1))
                    ]),
                    BlockStmt([
                        ReturnStmt(
                            BinaryOp(
                                Identifier("n"),
                                "*",
                                FuncCall(
                                    "factorial",
                                    [BinaryOp(Identifier("n"), "-", IntLiteral(1))]
                                )
                            )
                        )
                    ])
                )
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(None, "num", FuncCall("readInt", [])),
                VarDecl(None, "result", FuncCall("factorial", [Identifier("num")])),
                ExprStmt(FuncCall("printInt", [Identifier("result")]))
            ])
        )
    ])
    assert str(ASTGenerator(source).generate()) == str(expected)

def test_005():
    source = """
void main() {
    // With auto and initialization
    auto x = readInt();
    auto y = readFloat();
    auto name = readString();
    
    // With auto without initialization
    auto sum;
    sum = x + y;              // sum: float (inferred from first usage - assignment)
    
    // With explicit type and initialization
    int count = 0;
    float total = 0.0;
    string greeting = "Hello, ";
    
    // With explicit type without initialization
    int i;
    float f;
    i = readInt();            // assignment to int
    f = readFloat();          // assignment to float
    
    printFloat(sum);
    printString(greeting);
    printString(name);
}
"""
    expected = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(None, "x", FuncCall("readInt", [])),
                VarDecl(None, "y", FuncCall("readFloat", [])),
                VarDecl(None, "name", FuncCall("readString", [])),

                VarDecl(None, "sum", None),
                ExprStmt(
                    AssignExpr(
                        Identifier("sum"),
                        BinaryOp(Identifier("x"), "+", Identifier("y"))
                    )
                ),

                VarDecl(IntType(), "count", IntLiteral(0)),
                VarDecl(FloatType(), "total", FloatLiteral(0.0)),
                VarDecl(StringType(), "greeting", StringLiteral("Hello, ")),

                VarDecl(IntType(), "i", None),
                VarDecl(FloatType(), "f", None),
                ExprStmt(
                    AssignExpr(Identifier("i"), FuncCall("readInt", []))
                ),
                ExprStmt(
                    AssignExpr(Identifier("f"), FuncCall("readFloat", []))
                ),

                ExprStmt(FuncCall("printFloat", [Identifier("sum")])),
                ExprStmt(FuncCall("printString", [Identifier("greeting")])),
                ExprStmt(FuncCall("printString", [Identifier("name")]))
            ])
        )
    ])
    assert str(ASTGenerator(source).generate()) == str(expected)

def test_step2_inferred_return_type_and_nested_assignment():
    source = """
add(int x, int y) {
    return x + y;
}

void main() {
    int a;
    int b;
    int c;
    a = b = c = 1;
}
"""
    expected = Program([
        FuncDecl(
            None,
            "add",
            [Param(IntType(), "x"), Param(IntType(), "y")],
            BlockStmt([
                ReturnStmt(BinaryOp(Identifier("x"), "+", Identifier("y")))
            ]),
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "a", None),
                VarDecl(IntType(), "b", None),
                VarDecl(IntType(), "c", None),
                ExprStmt(
                    AssignExpr(
                        Identifier("a"),
                        AssignExpr(
                            Identifier("b"),
                            AssignExpr(Identifier("c"), IntLiteral(1)),
                        ),
                    )
                ),
            ]),
        ),
    ])
    assert str(ASTGenerator(source).generate()) == str(expected)


def test_step2_operator_precedence_chain():
    source = """
void main() {
    auto x = 1 + 2 * 3 == 7 || 0;
}
"""
    expected = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(
                    None,
                    "x",
                    BinaryOp(
                        BinaryOp(
                            BinaryOp(
                                IntLiteral(1),
                                "+",
                                BinaryOp(IntLiteral(2), "*", IntLiteral(3)),
                            ),
                            "==",
                            IntLiteral(7),
                        ),
                        "||",
                        IntLiteral(0),
                    ),
                )
            ]),
        )
    ])
    assert str(ASTGenerator(source).generate()) == str(expected)


def test_step2_for_expr_init_and_postfix_update():
    source = """
void main() {
    int i;
    for (i = 0; i < 3; i++)
        printInt(i);
}
"""
    expected = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "i", None),
                ForStmt(
                    ExprStmt(AssignExpr(Identifier("i"), IntLiteral(0))),
                    BinaryOp(Identifier("i"), "<", IntLiteral(3)),
                    PostfixOp("++", Identifier("i")),
                    ExprStmt(FuncCall("printInt", [Identifier("i")])),
                ),
            ]),
        )
    ])
    assert str(ASTGenerator(source).generate()) == str(expected)


def test_step2_struct_literal_as_argument_and_switch_layout():
    source = """
struct Point { int x; int y; };

void printPoint(Point p) {
    printInt(p.x);
}

void main() {
    auto x = 2;
    switch (x) {
        case 1:
            break;
        default:
            break;
        case 2:
            printPoint({1, 2});
    }
}
"""
    expected = Program([
        StructDecl(
            "Point",
            [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")],
        ),
        FuncDecl(
            VoidType(),
            "printPoint",
            [Param(StructType("Point"), "p")],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [MemberAccess(Identifier("p"), "x")]))
            ]),
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(None, "x", IntLiteral(2)),
                SwitchStmt(
                    Identifier("x"),
                    [
                        CaseStmt(IntLiteral(1), [BreakStmt()]),
                        CaseStmt(
                            IntLiteral(2),
                            [
                                ExprStmt(
                                    FuncCall(
                                        "printPoint",
                                        [StructLiteral([IntLiteral(1), IntLiteral(2)])],
                                    )
                                )
                            ],
                        ),
                    ],
                    DefaultStmt([BreakStmt()]),
                ),
            ]),
        ),
    ])
    assert str(ASTGenerator(source).generate()) == str(expected)


# ============================================================
# Step 3: Edge cases — member-access LHS, postfix chain,
#          logical NOT/unary, continue, empty for corners,
#          nested struct, switch fall-through, void return
# ============================================================

def test_step3_member_access_lhs_assignment():
    """Assignment to struct member (member access as LHS)."""
    source = """
struct Point { int x; int y; };
void main() {
    Point p;
    p.x = 10;
    p.y = p.x + 1;
}
"""
    expected = Program([
        StructDecl("Point", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(
            VoidType(), "main", [],
            BlockStmt([
                VarDecl(StructType("Point"), "p", None),
                ExprStmt(AssignExpr(MemberAccess(Identifier("p"), "x"), IntLiteral(10))),
                ExprStmt(AssignExpr(
                    MemberAccess(Identifier("p"), "y"),
                    BinaryOp(MemberAccess(Identifier("p"), "x"), "+", IntLiteral(1)),
                )),
            ]),
        ),
    ])
    assert str(ASTGenerator(source).generate()) == str(expected)


def test_step3_chained_postfix_call_then_member():
    """Chained postfix: function call result then member access."""
    source = """
struct Point { int x; int y; };
Point getPoint() { Point p; return p; }
void main() {
    auto v = getPoint().x;
}
"""
    expected = Program([
        StructDecl("Point", [MemberDecl(IntType(), "x"), MemberDecl(IntType(), "y")]),
        FuncDecl(
            StructType("Point"), "getPoint", [],
            BlockStmt([
                VarDecl(StructType("Point"), "p", None),
                ReturnStmt(Identifier("p")),
            ]),
        ),
        FuncDecl(
            VoidType(), "main", [],
            BlockStmt([
                VarDecl(None, "v",
                    MemberAccess(FuncCall("getPoint", []), "x"),
                ),
            ]),
        ),
    ])
    assert str(ASTGenerator(source).generate()) == str(expected)


def test_step3_unary_not_and_minus():
    """Unary NOT and unary minus in expressions."""
    source = """
void main() {
    auto a = 1;
    auto b = !a;
    auto c = -a;
    auto d = +a;
    auto e = --a;
}
"""
    expected = Program([
        FuncDecl(
            VoidType(), "main", [],
            BlockStmt([
                VarDecl(None, "a", IntLiteral(1)),
                VarDecl(None, "b", PrefixOp("!", Identifier("a"))),
                VarDecl(None, "c", PrefixOp("-", Identifier("a"))),
                VarDecl(None, "d", PrefixOp("+", Identifier("a"))),
                VarDecl(None, "e", PrefixOp("--", Identifier("a"))),
            ]),
        )
    ])
    assert str(ASTGenerator(source).generate()) == str(expected)


def test_step3_logical_chain_and_or():
    """Chained && and || with correct left-associativity."""
    source = """
void main() {
    auto r = 1 && 2 && 3 || 4 || 5;
}
"""
    expected = Program([
        FuncDecl(
            VoidType(), "main", [],
            BlockStmt([
                VarDecl(None, "r",
                    BinaryOp(
                        BinaryOp(
                            BinaryOp(
                                BinaryOp(IntLiteral(1), "&&", IntLiteral(2)),
                                "&&",
                                IntLiteral(3),
                            ),
                            "||",
                            IntLiteral(4),
                        ),
                        "||",
                        IntLiteral(5),
                    ),
                ),
            ]),
        )
    ])
    assert str(ASTGenerator(source).generate()) == str(expected)


def test_step3_continue_in_while():
    """Continue statement inside while loop."""
    source = """
void main() {
    auto i = 0;
    while (i < 10) {
        i++;
        if (i == 5) continue;
        printInt(i);
    }
}
"""
    expected = Program([
        FuncDecl(
            VoidType(), "main", [],
            BlockStmt([
                VarDecl(None, "i", IntLiteral(0)),
                WhileStmt(
                    BinaryOp(Identifier("i"), "<", IntLiteral(10)),
                    BlockStmt([
                        ExprStmt(PostfixOp("++", Identifier("i"))),
                        IfStmt(
                            BinaryOp(Identifier("i"), "==", IntLiteral(5)),
                            ContinueStmt(),
                            None,
                        ),
                        ExprStmt(FuncCall("printInt", [Identifier("i")])),
                    ]),
                ),
            ]),
        )
    ])
    assert str(ASTGenerator(source).generate()) == str(expected)


def test_step3_void_return_explicit():
    """Explicit void return (return;) inside function."""
    source = """
void check(int x) {
    if (x < 0) return;
    printInt(x);
}
void main() {}
"""
    expected = Program([
        FuncDecl(
            VoidType(), "check", [Param(IntType(), "x")],
            BlockStmt([
                IfStmt(
                    BinaryOp(Identifier("x"), "<", IntLiteral(0)),
                    ReturnStmt(None),
                    None,
                ),
                ExprStmt(FuncCall("printInt", [Identifier("x")])),
            ]),
        ),
        FuncDecl(VoidType(), "main", [], BlockStmt([])),
    ])
    assert str(ASTGenerator(source).generate()) == str(expected)


def test_step3_for_empty_condition_and_update():
    """For loop with omitted condition and update (infinite-style)."""
    source = """
void main() {
    for (auto i = 0; ; ) {
        break;
    }
}
"""
    expected = Program([
        FuncDecl(
            VoidType(), "main", [],
            BlockStmt([
                ForStmt(
                    VarDecl(None, "i", IntLiteral(0)),
                    None,
                    None,
                    BlockStmt([BreakStmt()]),
                ),
            ]),
        )
    ])
    assert str(ASTGenerator(source).generate()) == str(expected)


def test_step3_nested_struct_member():
    """Struct with a struct-typed member, nested member access."""
    source = """
struct Inner { int val; };
struct Outer { Inner inner; int id; };
void main() {
    Outer o;
    o.inner.val = 42;
}
"""
    expected = Program([
        StructDecl("Inner", [MemberDecl(IntType(), "val")]),
        StructDecl("Outer", [
            MemberDecl(StructType("Inner"), "inner"),
            MemberDecl(IntType(), "id"),
        ]),
        FuncDecl(
            VoidType(), "main", [],
            BlockStmt([
                VarDecl(StructType("Outer"), "o", None),
                ExprStmt(AssignExpr(
                    MemberAccess(MemberAccess(Identifier("o"), "inner"), "val"),
                    IntLiteral(42),
                )),
            ]),
        ),
    ])
    assert str(ASTGenerator(source).generate()) == str(expected)


def test_step3_switch_fallthrough_multi_case():
    """Switch with fall-through: multiple case labels sharing a body."""
    source = """
void main() {
    auto x = 2;
    switch (x) {
        case 1:
        case 2:
        case 3:
            printInt(1);
            break;
        default:
            printInt(0);
    }
}
"""
    expected = Program([
        FuncDecl(
            VoidType(), "main", [],
            BlockStmt([
                VarDecl(None, "x", IntLiteral(2)),
                SwitchStmt(
                    Identifier("x"),
                    [
                        CaseStmt(IntLiteral(1), []),
                        CaseStmt(IntLiteral(2), []),
                        CaseStmt(IntLiteral(3), [
                            ExprStmt(FuncCall("printInt", [IntLiteral(1)])),
                            BreakStmt(),
                        ]),
                    ],
                    DefaultStmt([ExprStmt(FuncCall("printInt", [IntLiteral(0)]))]),
                ),
            ]),
        )
    ])
    assert str(ASTGenerator(source).generate()) == str(expected)


def test_step3_postfix_decrement_and_assignment():
    """Postfix decrement as expression statement and in assignment."""
    source = """
void main() {
    int x = 5;
    x--;
    auto y = x--;
}
"""
    expected = Program([
        FuncDecl(
            VoidType(), "main", [],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(5)),
                ExprStmt(PostfixOp("--", Identifier("x"))),
                VarDecl(None, "y", PostfixOp("--", Identifier("x"))),
            ]),
        )
    ])
    assert str(ASTGenerator(source).generate()) == str(expected)


def test_step3_parenthesized_expr_in_condition():
    """Parenthesized expressions preserve correct AST structure."""
    source = """
void main() {
    auto x = 2;
    auto y = 3;
    if ((x + y) * 2 == 10) printInt(1);
}
"""
    expected = Program([
        FuncDecl(
            VoidType(), "main", [],
            BlockStmt([
                VarDecl(None, "x", IntLiteral(2)),
                VarDecl(None, "y", IntLiteral(3)),
                IfStmt(
                    BinaryOp(
                        BinaryOp(
                            BinaryOp(Identifier("x"), "+", Identifier("y")),
                            "*",
                            IntLiteral(2),
                        ),
                        "==",
                        IntLiteral(10),
                    ),
                    ExprStmt(FuncCall("printInt", [IntLiteral(1)])),
                    None,
                ),
            ]),
        )
    ])
    assert str(ASTGenerator(source).generate()) == str(expected)
