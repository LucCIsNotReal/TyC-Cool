"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser


def test_001():
    source = """
void main() {
    printString("Hello, World!");
}
"""
    expected = "success"
    assert Parser(source).parse() == expected

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
    expected = "success"
    assert Parser(source).parse() == expected

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
    expected = "success"
    assert Parser(source).parse() == expected

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
    expected = "success"
    assert Parser(source).parse() == expected

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
    
    // Note: String concatenation is NOT supported
    // This is because + operator applies to int or float, not string
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_006():
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
    expected = "success"
    assert Parser(source).parse() == expected

def test_007():
    source = """
void main() {
"""
    expected = "Error on line 3 col 0: <EOF>"
    assert Parser(source).parse() == expected

def test_008():
    source = """
void main {}
"""
    expected = "Error on line 2 col 10: {"
    assert Parser(source).parse() == expected


def test_009():
    source = """
void main() {
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_010():
    source = """
void main() {
    int a;
    float b;
    string c;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_011():
    source = """
void main() {
    auto a = 1;
    auto b = 2.5;
    auto c = "hi";
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_012():
    source = """
void main() {
    int a;
    a = 10;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_013():
    source = """
void main() {
    1 + 2;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_014():
    source = """
void main() {
    if (1) {
        int a = 1;
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_015():
    source = """
void main() {
    int a = 0;
    if (a) {
        a = 1;
    } else {
        a = 2;
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_016():
    source = """
void main() {
    int a = 0;
    if (a) {
        a = 1;
    } else {
        if (1) {
            a = 3;
        }
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_017():
    source = """
void main() {
    int i = 0;
    while (i < 10) {
        i = i + 1;
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_018():
    source = """
void main() {
    for (int i = 0; i < 10; i = i + 1) {
        printInt(i);
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_019():
    source = """
void main() {
    for (; ; ) {
        break;
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_020():
    source = """
void main() {
    int x = 0;
    switch (x) {
        case 0:
            x = 1;
            break;
        default:
            x = 2;
            break;
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_021():
    source = """
void main() {
    int x = 0;
    switch (x) {
        case 1:
            x = 10;
        case 2:
            x = 20;
            break;
        default:
            x = 0;
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_022():
    source = """
void main() {
    int i = 0;
    while (i < 3) {
        if (i == 2) {
            break;
        }
        i = i + 1;
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_023():
    source = """
void main() {
    int i = 0;
    for (; i < 5; i = i + 1) {
        if (i == 1) {
            continue;
        }
        printInt(i);
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_024():
    source = """
void main() {
    return;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_025():
    source = """
add() {
    return 1;
}

void main() {
    auto x = add();
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_026():
    source = """
int one() {
    return 1;
}

void main() {
    auto x = one();
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_027():
    source = """
sum() {
    return 1 + 2;
}

void main() {
    auto x = sum();
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_028():
    source = """
struct Empty {
};

void main() {
    Empty e;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_029():
    source = """
struct P {
    int x;
};

void main() {
    P p;
    p.x = 1;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_030():
    source = """
struct P {
    int x;
    int y;
};

void main() {
    P p = {1, 2};
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_031():
    source = """
struct P {
    int x;
    int y;
};

void main() {
    P a = {1, 2};
    P b;
    b = a;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_032():
    source = """
void main() {
    {
        int a = 1;
        {
            int b = 2;
            a = b;
        }
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_033():
    source = """
void main() {
    auto a = 1 && 0;
    auto b = 1 || 0;
    auto c = !1;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_034():
    source = """
void main() {
    auto a = 1 < 2;
    auto b = 1 == 2;
    auto c = 1 != 2;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_035():
    source = """
void main() {
    auto a = 1 + 2 * 3 - 4 / 2;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_036():
    source = """
void main() {
    auto a = -(1 + 2);
    auto b = +3;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_037():
    source = """
void main() {
    int i = 0;
    i++;
    i--;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_038():
    source = """
void main() {
    int i = 0;
    ++i;
    --i;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_039():
    source = """
struct P {
    int x;
};

void main() {
    P p;
    auto a = p.x;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_040():
    source = """
int add(int x, int y) {
    return x + y;
}

void main() {
    auto s = add(1, 2);
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_041():
    source = """
int add(int x, int y) {
    return x + y;
}

void main() {
    auto s = add(1, add(2, 3));
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_042():
    source = """
void main() {
    int a;
    int b;
    a = b = 1;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_043():
    source = """
struct P {
    int x;
};

void main() {
    P p;
    p.x = 3;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_044():
    source = """
struct S {
    int a;
};

void main() {
    S s = {};
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_045():
    source = """
void main() {
    printInt(1);
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_046():
    source = """
void main() {
    {
        int a = 1;
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_047():
    source = """
void main() {
    int a = 1;
    int b = 2;
    while (a < b && b > 0) {
        a = a + 1;
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_048():
    source = """
void main() {
    int a = 0;
    if (a) a = 1;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_049():
    source = """
void main() {
    int i = 0;
    for (; i < 3; ) {
        i = i + 1;
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_050():
    source = """
void main() {
    for (int i = 0; ; i = i + 1) {
        if (i == 2) break;
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_051():
    source = """
void main() {
    int x = 2;
    switch (x) {
        case 1:
            x = 10;
            x = x + 1;
            break;
        default:
            x = 0;
            break;
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_052():
    source = """
struct A {
    int x;
};

struct B {
    float y;
};

void main() {
    A a;
    B b;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_053():
    source = """
struct A {
    int x;
};

struct B {
    A a;
};

void main() {
    B b;
    b.a.x = 1;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_054():
    source = """
void main() {
    auto a = (1 + 2) * (3 + 4);
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_055():
    source = """
void main() {
    auto a = !(1 < 2);
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_056():
    source = """
void main() {
    auto a = (1 < 2) && (2 < 3);
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_057():
    source = """
void main() {
    auto a = 1.5 + 2.25 * 3.0;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_058():
    source = """
void main() {
    string s = "hello";
    printString(s);
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_059():
    source = """
void main() {
    printString("Line1\\nLine2");
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_060():
    source = """
float pi() {
    return 3.14;
}

void main() {
    auto x = pi();
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_061():
    source = """
int f() { return 1; }
int g() { return f(); }

void main() {
    auto x = g();
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_062():
    source = """
void main() {
    int a = 1;
    int b = 2;
    return;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_063():
    source = """
int max(int a, int b) {
    if (a > b) return a;
    return b;
}

void main() {
    auto m = max(1, 2);
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_064():
    source = """
void main() {
    int i = 0;
    for (; i < 3; i = i + 1) {
        int j = 0;
        while (j < 2) {
            j = j + 1;
        }
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_065():
    source = """
void main() {
    int i = 0;
    while (i < 2) {
        int j = 0;
        for (; j < 2; j = j + 1) {
            printInt(j);
        }
        i = i + 1;
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_066():
    source = """
void main() {
    int x = 1;
    switch (x) {
        case 1:
            if (x) {
                x = 2;
            }
            break;
        default:
            x = 0;
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_067():
    source = """
void main() {
    int x = 0;
    while (x < 1) {
        switch (x) {
            case 0:
                x = 1;
                break;
            default:
                x = 2;
        }
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_068():
    source = """
void main() {
    int a = 0;
    if (a) {
        a = 1;
    } else {
        {
            a = 2;
        }
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_069():
    source = """
struct P {
    int x;
};

void main() {
    P p;
    p.x = (1 + 2) * 3;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_070():
    source = """
struct P {
    int x;
    int y;
};

void main() {
    P p = {1, 2};
    printInt(p.x);
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_071():
    source = """
void main() {
    auto x;
    x = 10;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_072():
    source = """
helper() {
}

void main() {
    helper();
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_073():
    source = """
int f(int x) {
    if (x) return 1;
    return 0;
}

void main() {
    auto v = f(1);
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_074():
    source = """
struct P { int x; };

void main() {
    P p;
    p.x;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_075():
    source = """
foo() { }

void main() {
    foo();
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_076():
    source = """
string msg() {
    return "hi";
}

void main() {
    auto s = msg();
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_077():
    source = """
void main() {
    int x = 1;
    switch (x) {
        case 1:
            x = 2;
            break;
        case 2:
            x = 3;
            break;
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_078():
    source = """
void main() {
    int x = 0;
    switch (x) {
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_079():
    source = """
void main() {
    {}
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_080():
    source = """
struct Point { int x; int y; };

void main() {
    Point p;
    p.x = 1;
    p.y = 2;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_081():
    source = """
void main() {
    int a = 1;
    int a2 = 2;
    a = a2;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_082():
    source = """
void main() {
    auto a = +1.0;
    auto b = -2.0;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_083():
    source = """
void main() {
    auto a = 10 % 3;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_084():
    source = """
void main() {
    int a;
    return a = 1;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_085():
    source = """
void main() {
    auto a = (1 < 2) && (2 != 3) || (3 > 4);
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_086():
    source = """
void main() {
    auto x;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_087():
    source = """
struct A { int b; };
struct B { A a; };

void main() {
    B p;
    p.a.b = 1;
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_088():
    source = """
int add(int a, int b) {
    return a + b;
}

void main() {
    auto s = add(3, 4);
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_089():
    source = """
int sum3(int a, int b, int c) {
    return a + b + c;
}

void main() {
    auto s = sum3(1, 2, 3);
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_090():
    source = """
struct P { int x; int y; };

void main() {
    auto p = {1, 2};
    printInt(p.x);
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_091():
    source = """
int get() { return 1; }

void main() {
    auto v = get();
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_092():
    source = """
void main() {
    int i = 0;
    while (i < 3) {
        if (i == 1) {
            i = i + 1;
            continue;
        }
        if (i == 2) break;
        i = i + 1;
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_093():
    source = """
helper() {
    return;
}

void main() {
    helper();
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_094():
    source = """
void main() { int a = 1; a = a + 1; }
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_095():
    source = """
int inc(int x) { return x + 1; }

void main() {
    inc(1);
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_096():
    source = """
void main() {
    auto a = (1 + 2) * 3;
    auto b = (a > 0) && (a < 10);
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_097():
    source = """
struct P { int x; int y; };

void main() {
    P p = {1, 2};
    if (p.x < p.y) {
        p.x = p.y;
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_098():
    source = """
void main() {
    int a = 1;
    int b = 2;
    int c = 3;
    a = b + c * (a + 1);
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_099():
    source = """
struct Person {
    string name;
    int age;
};

void main() {
    Person p = {"John", 20};
    printString(p.name);
}
"""
    expected = "success"
    assert Parser(source).parse() == expected


def test_100():
    source = """
struct Point { int x; int y; };

int add(int a, int b) { return a + b; }

void main() {
    Point p = {1, 2};
    int s = add(p.x, p.y);
    if (s > 0) {
        printInt(s);
    } else {
        printInt(0);
    }
}
"""
    expected = "success"
    assert Parser(source).parse() == expected
