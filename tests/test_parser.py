"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser


# ========== Simple Test Cases (10 types) ==========
def test_empty_program():
    """1. Empty program"""
    assert Parser("").parse() == "success"


def test_program_with_only_main():
    """2. Program with only main function"""
    assert Parser("void main() {}").parse() == "success"


def test_struct_simple():
    """3. Struct declaration"""
    source = "struct Point { int x; int y; };"
    assert Parser(source).parse() == "success"


def test_function_no_params():
    """4. Function with no parameters"""
    source = "void greet() { printString(\"Hello\"); }"
    assert Parser(source).parse() == "success"


def test_var_decl_auto_with_init():
    """5. Variable declaration"""
    source = "void main() { auto x = 5; }"
    assert Parser(source).parse() == "success"


def test_if_simple():
    """6. If statement"""
    source = "void main() { if (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_while_simple():
    """7. While statement"""
    source = "void main() { while (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_for_simple():
    """8. For statement"""
    source = "void main() { for (auto i = 0; i < 10; ++i) printInt(i); }"
    assert Parser(source).parse() == "success"


def test_switch_simple():
    """9. Switch statement"""
    source = "void main() { switch (1) { case 1: printInt(1); break; } }"
    assert Parser(source).parse() == "success"


def test_assignment_simple():
    """10. Assignment statement"""
    source = "void main() { int x; x = 5; }"
    assert Parser(source).parse() == "success"

def test_011():
    """11. Print string function"""
    source = """
void main() {
    printString("Hello, World!");
}
"""
    assert Parser(source).parse() == "success"

def test_012():
    """12. Functions with parameters and return values"""
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
    assert Parser(source).parse() == "success"

def test_013():
    """13. Loop and conditional statements"""
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
    assert Parser(source).parse() == "success"

def test_014():
    """14. Recursive function (factorial)"""
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
    assert Parser(source).parse() == "success"

def test_015():
    """15. Variable declarations with auto and explicit types"""
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
    
    // Note: String concatenation is NOT supported
    // This is because + operator applies to int or float, not string
}
"""
    assert Parser(source).parse() == "success"


def test_016():
    """16. Structs: declaration, initialization, member access, and assignment"""
    source ="""
struct Point {
    int x;
    int y;
};

struct Person {
    string name;
    int age;
    float height;
};

void main() {
    // Struct variable declaration without initialization
    Point p1;
    p1.x = 10;
    p1.y = 20;
    
    // Struct variable declaration with initialization
    Point p2 = {30, 40};
    
    // Access and modify struct members
    printInt(p2.x);
    printInt(p2.y);
    
    // Struct assignment
    p1 = p2;  // Copy all members
    
    // Person struct usage
    Person person1 = {"John", 25, 1.75};
    printString(person1.name);
    printInt(person1.age);
    printFloat(person1.height);
    
    // Modify struct members
    person1.age = 26;
    person1.height = 1.76;
    
    // Using struct with auto
    auto p3 = p2;  // p3: Point (inferred from assignment)
    printInt(p3.x);
}
"""
    assert Parser(source).parse() == "success"

def test_017():
    """17. Switch statement with multiple cases and default"""
    source = """
void main() {
    auto choice = readInt();
    switch (choice) {
        case 1:
            printString("You chose option 1");
            break;
        case 2:
            printString("You chose option 2");
            break;
        case 3:
            printString("You chose option 3");
            break;
        default:
            printString("Invalid choice");
    }
}
"""
    assert Parser(source).parse() == "success"

def test_018():
    """18. Function calls with various argument types and return values"""
    source = """
int sum(int a, int b) {
    return a + b;
}
float average(float x, float y) {
    return (x + y) / 2.0;
}
string greet(string name) {
    return "Hello, " + name;  // Note: String concatenation is NOT supported
}
void main() {
    auto s = sum(10, 20);
    printInt(s);
    auto avg = average(5.0, 15.0);
    printFloat(avg);
    auto message = greet("Alice");
    printString(message);
}
"""
    assert Parser(source).parse() == "success"


def test_019():
    """19. Nested control flow statements"""
    source = """
void main() {
    auto n = readInt();
    
    for (auto i = 0; i < n; ++i) {
        if (i % 2 == 0) {
            printString("Even: ");
            printInt(i);
        } else {
            printString("Odd: ");
            printInt(i);
        }
    }
}
"""    
    assert Parser(source).parse() == "success"


def test_020():
    """20. Complex expressions with multiple operators and parentheses"""
    source = """
void main() {
    auto a = readInt();
    auto b = readInt();
    auto c = readInt();
    
    auto result = (a + b) * c - (a / b) + (b % c);
    printInt(result);
}
"""    
    assert Parser(source).parse() == "success"

def test_021():
    """21. Function with struct parameter and return type"""
    source = """
struct Point {
    int x;
    int y;
};
Point createPoint(int x, int y) {
    Point p;
    p.x = x;
    p.y = y;
    return p;
}
void main() {
    auto p1 = createPoint(10, 20);
    printInt(p1.x);
    printInt(p1.y);
}
"""
    assert Parser(source).parse() == "success"

#thêm các testcase kiểm tra lỗi cú pháp
def test_022():
    """22. Missing semicolon after variable declaration"""
    source = """
void main() {
    auto x = 10
    printInt(x);
}
"""
    assert Parser(source).parse() == "Error on line 4 col 4: printInt"

def test_023():
    """23. Unmatched parentheses in expression"""
    source = """
void main() {
    auto result = (10 + 5 * (2 - 3);
    printInt(result);
}
"""
    assert Parser(source).parse() == "Error on line 3 col 35: ;"

def test_024():
    """24. Invalid struct member access"""
    source = """
struct Point {
    int x;
    int y;
};
void main() {
    Point p;
    p.z = 10;  // 'z' is not a member of 'Point'
}
"""
    assert Parser(source).parse() == "success"

def test_025():
    """25. Missing return statement in non-void function"""
    source = """int add(int a, int b) {
    auto sum = a + b;
}
void main() {
    auto result = add(5, 10);
    printInt(result);
}
"""
    assert Parser(source).parse() == "success"

def test_026():
    """26. Missing semicolon after variable declaration"""
    source = """
void main() {
    auto x = 10
    printInt(x);
}
"""
    assert "Error" in Parser(source).parse()

def test_027():
    """27. Missing semicolon after struct declaration"""
    source = """
struct Point { int x; int y; }
void main() {}
"""
    assert "Error" in Parser(source).parse()

def test_028():
    """28. Missing closing brace in function"""
    source = """
void main() {
    auto x = 5;
    printInt(x);
"""
    assert "Error" in Parser(source).parse()

def test_029():
    """29. Missing opening brace in function"""
    source = """
void main()
    auto x = 5;
    printInt(x);
}
"""
    assert "Error" in Parser(source).parse()

def test_030():
    """30. Unmatched parentheses in expression"""
    source = """
void main() {
    auto result = (10 + 5 * (2 - 3);
}
"""
    assert "Error" in Parser(source).parse()

def test_031():
    """31. Missing parentheses in if statement"""
    source = """
void main() {
    if x > 5 {
        printInt(x);
    }
}
"""
    assert "Error" in Parser(source).parse()

def test_032():
    """32. Missing parentheses in while statement"""
    source = """
void main() {
    while x < 10 {
        ++x;
    }
}
"""
    assert "Error" in Parser(source).parse()

def test_033():
    """33. Missing colon in case statement"""
    source = """
void main() {
    switch (x) {
        case 1
            printInt(1);
            break;
    }
}
"""
    assert "Error" in Parser(source).parse()

def test_034():
    """34. Missing closing brace in struct declaration"""
    source = """
struct Point {
    int x;
    int y;
"""
    assert "Error" in Parser(source).parse()

def test_035():
    """35. Invalid parameter list - missing type"""
    source = """
int add(a, int b) {
    return a + b;
}
void main() {}
"""
    assert "Error" in Parser(source).parse()

def test_036():
    """36. Missing comma in parameter list"""
    source = """
int add(int a int b) {
    return a + b;
}
void main() {}
"""
    assert "Error" in Parser(source).parse()

def test_037():
    """37. Invalid variable declaration - missing identifier"""
    source = """
void main() {
    auto = 10;
}
"""
    assert "Error" in Parser(source).parse()

def test_038():
    """38. Invalid type specification"""
    source = """
void main() {
    int flag = 0;
}
"""
    assert "success" in Parser(source).parse()

def test_039():
    """39. Missing semicolon in for loop initializer"""
    source = """
void main() {
    for (auto i = 0 i < 10; ++i) {
        printInt(i);
    }
}
"""
    assert "Error" in Parser(source).parse()

def test_040():
    """40. Missing semicolon in for loop condition"""
    source = """
void main() {
    for (auto i = 0; i < 10 ++i) {
        printInt(i);
    }
}
"""
    assert "Error" in Parser(source).parse()

def test_041():
    """41. Missing parentheses in for statement"""
    source = """
void main() {
    for auto i = 0; i < 10; ++i {
        printInt(i);
    }
}
"""
    assert "Error" in Parser(source).parse()

def test_042():
    """42. Invalid expression - missing operand"""
    source = """
void main() {
    auto x = 5 +;
}
"""
    assert "Error" in Parser(source).parse()

def test_043():
    """43. Invalid unary operator placement"""
    source = """
void main() {
    auto x = 5++;
}
"""
    assert "success" in Parser(source).parse()

def test_044():
    """44. Missing comma in struct member list"""
    source = """
struct Point {
    int x
    int y;
};
void main() {}
"""
    assert "Error" in Parser(source).parse()

def test_045():
    """45. Duplicate case statement without break"""
    source = """
void main() {
    switch (x) {
        case 1:
        case 1:
            printInt(1);
    }
}
"""
    assert Parser(source).parse() == "success"

def test_046():
    """46. Missing semicolon in return statement"""
    source = """
int getValue() {
    return 42
}
void main() {}
"""
    assert "Error" in Parser(source).parse()

def test_047():
    """47. Invalid expression in assignment"""
    source = """
void main() {
    int x;
    x = ;
}
"""
    assert "Error" in Parser(source).parse()

def test_048():
    """48. Missing closing parenthesis in function call"""
    source = """
void main() {
    printInt(5;
}
"""
    assert "Error" in Parser(source).parse()

def test_049():
    """49. Invalid member access - missing member name"""
    source = """
struct Point { int x; };
void main() {
    Point p;
    p.;
}
"""
    assert "Error" in Parser(source).parse()

def test_050():
    """50. Multiple default cases in switch statement"""
    source = """
void main() {
    switch (x) {
        case 1:
            printInt(1);
        default:
            printInt(0);
        default:
            printInt(-1);
    }
}
"""
    assert "success" in Parser(source).parse()