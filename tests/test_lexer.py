"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer


# ========== Simple Test Cases (10 types) ==========
def test_keyword_auto():
    """1. Keyword"""
    tokenizer = Tokenizer("auto")
    assert tokenizer.get_tokens_as_string() == "auto,<EOF>"


def test_operator_assign():
    """2. Operator"""
    tokenizer = Tokenizer("=")
    assert tokenizer.get_tokens_as_string() == "=,<EOF>"


def test_separator_semi():
    """3. Separator"""
    tokenizer = Tokenizer(";")
    assert tokenizer.get_tokens_as_string() == ";,<EOF>"


def test_integer_single_digit():
    """4. Integer literal"""
    tokenizer = Tokenizer("5")
    assert tokenizer.get_tokens_as_string() == "5,<EOF>"


def test_float_decimal():
    """5. Float literal"""
    tokenizer = Tokenizer("3.14")
    assert tokenizer.get_tokens_as_string() == "3.14,<EOF>"


def test_string_simple():
    """6. String literal"""
    tokenizer = Tokenizer('"hello"')
    assert tokenizer.get_tokens_as_string() == "hello,<EOF>"


def test_identifier_simple():
    """7. Identifier"""
    tokenizer = Tokenizer("x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"


def test_line_comment():
    """8. Line comment"""
    tokenizer = Tokenizer("// This is a comment")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_integer_in_expression():
    """9. Mixed: integers and operator"""
    tokenizer = Tokenizer("5+10")
    assert tokenizer.get_tokens_as_string() == "5,+,10,<EOF>"


def test_complex_expression():
    """10. Complex: variable declaration"""
    tokenizer = Tokenizer("auto x = 5 + 3 * 2;")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,5,+,3,*,2,;,<EOF>"

# ================================================

def test_011():
    """11. String with escape sequences"""
    tokenizer = Tokenizer(r'"Hello\nWorld\t!"')
    assert tokenizer.get_tokens_as_string() == r'Hello\nWorld\t!,<EOF>'

def test_012():
    """12. Float literals with exponent"""
    tokenizer = Tokenizer("1.5e10 2E-3 .75 4.")
    assert tokenizer.get_tokens_as_string() == "1.5e10,2E-3,.75,4.,<EOF>"

def test_013():
    """13. Unclosed string error"""
    tokenizer = Tokenizer('"This is unclosed string')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: This is unclosed string"

def test_014():
    """14. Illegal escape sequence error"""
    tokenizer = Tokenizer(r'"Illegal escape: \x"')
    assert tokenizer.get_tokens_as_string() == r'Illegal Escape In String: Illegal escape: \x'

def test_015():
    """15. Error character"""
    tokenizer = Tokenizer("@")
    assert tokenizer.get_tokens_as_string() == "Error Token @"

def test_016():
    """16. Unclosed string with newline"""
    tokenizer = Tokenizer('"This string has no end\n next_line = 1;')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: This string has no end"

def test_017():
    """17. Illegal escape with newline"""
    tokenizer = Tokenizer(r'"This string has illegal escape \q\n')
    assert tokenizer.get_tokens_as_string() == r'Illegal Escape In String: This string has illegal escape \q'

def test_018():
    """18. Illegal escape at end of string"""
    tokenizer = Tokenizer(r'"Ends with illegal escape \z"')
    assert tokenizer.get_tokens_as_string() == r'Illegal Escape In String: Ends with illegal escape \z'

def test_019():
    """19. Valid string with multiple escape sequences"""
    tokenizer = Tokenizer(r'"Line1\nLine2\tTabbed\\Backslash\""')
    assert tokenizer.get_tokens_as_string() == r'Line1\nLine2\tTabbed\\Backslash\",<EOF>'

def test_020():
    """20. Mixed valid and invalid tokens"""
    tokenizer = Tokenizer('auto x = 10; @ "Bad escape: \\y"')
    assert tokenizer.get_tokens_as_string() == "auto,x,=,10,;,Error Token @"

def test_021():
    """21. Multiple unclosed strings"""
    tokenizer = Tokenizer('"First unclosed string\n"Second unclosed string\n')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: First unclosed string"

def test_022():
    """22. Error character in expression"""
    tokenizer = Tokenizer("x, y = 5, @;")
    assert tokenizer.get_tokens_as_string() == "x,,,y,=,5,,,Error Token @"

def test_023():
    """23. Keywords and identifiers"""
    tokenizer = Tokenizer("auto var1 = readInt();")
    assert tokenizer.get_tokens_as_string() == "auto,var1,=,readInt,(,),;,<EOF>"

def test_024():
    """24. Keywords with similar prefixes"""
    tokenizer = Tokenizer("auto aut autoo")
    assert tokenizer.get_tokens_as_string() == "auto,aut,autoo,<EOF>"

def test_025():
    """25. Keywords in comments"""
    tokenizer = Tokenizer("// auto var1 = readInt();")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_026():
    """26. Some Keyword tokens in various contexts"""
    tokenizer = Tokenizer("if (x > 0) return x; else return -x;")
    assert tokenizer.get_tokens_as_string() == "if,(,x,>,0,),return,x,;,else,return,-,x,;,<EOF>"

def test_027():
    """27. Some Keyword tokens in various contexts"""
    tokenizer = Tokenizer("for (auto i = 0; i < 10; ++i) { printInt(i); }")
    assert tokenizer.get_tokens_as_string() == "for,(,auto,i,=,0,;,i,<,10,;,++,i,),{,printInt,(,i,),;,},<EOF>"

def test_028():
    """28. Some Keyword tokens in various contexts"""
    tokenizer = Tokenizer("while (n != 0) { n = n - 1; }")
    assert tokenizer.get_tokens_as_string() == "while,(,n,!=,0,),{,n,=,n,-,1,;,},<EOF>"

def test_029():
    """29. Some Keyword tokens in various contexts"""
    tokenizer = Tokenizer("switch (x) { case 1: break; default: return; }")
    assert tokenizer.get_tokens_as_string() == "switch,(,x,),{,case,1,:,break,;,default,:,return,;,},<EOF>"

def test_030():
    """30. Some Keyword tokens in various contexts"""
    tokenizer = Tokenizer("void main() { printString(\"Hello World\"); }")
    assert tokenizer.get_tokens_as_string() == "void,main,(,),{,printString,(,Hello World,),;,},<EOF>"

def test_031():
    """31. Various operators in expressions"""
    tokenizer = Tokenizer("a + b - c * d / e % f;")
    assert tokenizer.get_tokens_as_string() == "a,+,b,-,c,*,d,/,e,%,f,;,<EOF>"

def test_032():
    """32. Various comparison operators"""
    tokenizer = Tokenizer("if (x == y && a != b || c < d) { return; }")
    assert tokenizer.get_tokens_as_string() == "if,(,x,==,y,&&,a,!=,b,||,c,<,d,),{,return,;,},<EOF>"

def test_033():
    """33. Assignment and increment/decrement operators"""
    tokenizer = Tokenizer("x = y; ++x; --y;")
    assert tokenizer.get_tokens_as_string() == "x,=,y,;,++,x,;,--,y,;,<EOF>"

def test_034():
    """34. Bitwise operators"""
    tokenizer = Tokenizer("a & b | c ^ d ~e;")
    assert tokenizer.get_tokens_as_string() == "a,Error Token &"

def test_035():
    """35. Mixed operators in complex expression"""
    tokenizer = Tokenizer("result = (a + b) * (c - d) / e % f;")
    assert tokenizer.get_tokens_as_string() == "result,=,(,a,+,b,),*,(,c,-,d,),/,e,%,f,;,<EOF>"

def test_036():
    """36. Operators with no spaces"""
    tokenizer = Tokenizer("x+=1;y-=2;z*=3;a/=4;b%=5;")
    assert tokenizer.get_tokens_as_string() == "x,+,=,1,;,y,-,=,2,;,z,*,=,3,;,a,/,=,4,;,b,%,=,5,;,<EOF>"

def test_037():
    """37. Chained comparison operators"""
    tokenizer = Tokenizer("if (a < b <= c > d >= e == f != g) { return; }")
    assert tokenizer.get_tokens_as_string() == "if,(,a,<,b,<=,c,>,d,>=,e,==,f,!=,g,),{,return,;,},<EOF>"

def test_038():
    """38. Logical operators in conditions"""
    tokenizer = Tokenizer("while (x && y || !z) { x = x + 1; }")
    assert tokenizer.get_tokens_as_string() == "while,(,x,&&,y,||,!,z,),{,x,=,x,+,1,;,},<EOF>"

def test_039():
    """39. Bitwise and logical operators combined"""
    tokenizer = Tokenizer("result = (a && b) | (c ^ d) && (e || f);")
    assert tokenizer.get_tokens_as_string() == "result,=,(,a,&&,b,),Error Token |"

def test_040():
    """40. Complex expression with all operator types"""
    tokenizer = Tokenizer("x = (a + b) * c - d / e % f && g || h == i != j < k <= l > m >= n;")
    assert tokenizer.get_tokens_as_string() == "x,=,(,a,+,b,),*,c,-,d,/,e,%,f,&&,g,||,h,==,i,!=,j,<,k,<=,l,>,m,>=,n,;,<EOF>"

def test_041():
    """41. Dot operator in member access"""
    tokenizer = Tokenizer("object.member;")
    assert tokenizer.get_tokens_as_string() == "object,.,member,;,<EOF>"

def test_042():
    """42. Arrow operator in pointer access"""
    tokenizer = Tokenizer("ptr->member;")
    assert tokenizer.get_tokens_as_string() == "ptr,-,>,member,;,<EOF>"

def test_043():
    """43. Various separators in code"""
    tokenizer = Tokenizer("func(a, b; c: d{ e} )")
    assert tokenizer.get_tokens_as_string() == "func,(,a,,,b,;,c,:,d,{,e,},),<EOF>"

def test_044():
    """44. Brackets separators"""
    tokenizer = Tokenizer("array[func(x, y); z];")
    assert tokenizer.get_tokens_as_string() == "array,Error Token ["

def test_045():
    """45. Mixed separators in expressions"""
    tokenizer = Tokenizer("result = func(a, b) + arr[i];")
    assert tokenizer.get_tokens_as_string() == "result,=,func,(,a,,,b,),+,arr,Error Token ["

#Test cho chuỗi IDENTIFIER dài
def test_046():
    """46. Long identifier names"""
    tokenizer = Tokenizer("this0IsAVeryLongName12345;")
    assert tokenizer.get_tokens_as_string() == "this0IsAVeryLongName12345,;,<EOF>"

def test_047():
    """47. Identifiers with underscores"""
    tokenizer = Tokenizer("int _my_variable_name = 10;")
    assert tokenizer.get_tokens_as_string() == "int,_my_variable_name,=,10,;,<EOF>"
    
def test_048():
    """48. String with many Error Token"""
    tokenizer = Tokenizer("'ab\\'ab',")
    assert tokenizer.get_tokens_as_string() == "Error Token '"

def test_049():
    """49. String with many Error Token"""
    tokenizer = Tokenizer("ab\\'ab',")
    assert tokenizer.get_tokens_as_string() == "ab,Error Token \\"


def test_050():
    """50. Integer with leading zeros"""
    tokenizer = Tokenizer("0 00 000123")
    assert tokenizer.get_tokens_as_string() == "0,00,000123,<EOF>"

def test_051():
    """51. Large integer"""
    tokenizer = Tokenizer("999999999999")
    assert tokenizer.get_tokens_as_string() == "999999999999,<EOF>"

def test_052():
    """52. Integer followed by operator"""
    tokenizer = Tokenizer("42+58")
    assert tokenizer.get_tokens_as_string() == "42,+,58,<EOF>"

def test_053():
    """53. Integer in assignment"""
    tokenizer = Tokenizer("x = 12345;")
    assert tokenizer.get_tokens_as_string() == "x,=,12345,;,<EOF>"

def test_054():
    """54. Multiple integers separated by operators"""
    tokenizer = Tokenizer("1 * 2 / 3 - 4 + 5")
    assert tokenizer.get_tokens_as_string() == "1,*,2,/,3,-,4,+,5,<EOF>"

def test_055():
    """55. Integer with comparison operators"""
    tokenizer = Tokenizer("if (100 >= 50) return 0;")
    assert tokenizer.get_tokens_as_string() == "if,(,100,>=,50,),return,0,;,<EOF>"

def test_056():
    """56. Integer in function call"""
    tokenizer = Tokenizer("printInt(42);")
    assert tokenizer.get_tokens_as_string() == "printInt,(,42,),;,<EOF>"

def test_057():
    """57. Simple float with decimal point"""
    tokenizer = Tokenizer("3.14")
    assert tokenizer.get_tokens_as_string() == "3.14,<EOF>"

def test_058():
    """58. Float starting with zero"""
    tokenizer = Tokenizer("0.5")
    assert tokenizer.get_tokens_as_string() == "0.5,<EOF>"

def test_059():
    """59. Float with scientific notation"""
    tokenizer = Tokenizer("1.5e-10")
    assert tokenizer.get_tokens_as_string() == "1.5e-10,<EOF>"

def test_060():
    """60. Float with uppercase E notation"""
    tokenizer = Tokenizer("2.5E+5")
    assert tokenizer.get_tokens_as_string() == "2.5E+5,<EOF>"

def test_061():
    """61. Float without leading digit"""
    tokenizer = Tokenizer(".75")
    assert tokenizer.get_tokens_as_string() == ".75,<EOF>"

def test_062():
    """62. Float without trailing digits"""
    tokenizer = Tokenizer("5.")
    assert tokenizer.get_tokens_as_string() == "5.,<EOF>"

def test_063():
    """63. Multiple floats in expression"""
    tokenizer = Tokenizer("x = 1.5 + 2.7 * 3.14;")
    assert tokenizer.get_tokens_as_string() == "x,=,1.5,+,2.7,*,3.14,;,<EOF>"

def test_064():
    """64. String with spaces"""
    tokenizer = Tokenizer('"hello world"')
    assert tokenizer.get_tokens_as_string() == "hello world,<EOF>"

def test_065():
    """65. Empty string"""
    tokenizer = Tokenizer('""')
    assert tokenizer.get_tokens_as_string() == ",<EOF>"

def test_066():
    """66. String with numbers"""
    tokenizer = Tokenizer('"abc123"')
    assert tokenizer.get_tokens_as_string() == "abc123,<EOF>"

def test_067():
    """67. String with punctuation"""
    tokenizer = Tokenizer('"Hello, World!"')
    assert tokenizer.get_tokens_as_string() == "Hello, World!,<EOF>"

def test_068():
    """68. String with tab escape sequence"""
    tokenizer = Tokenizer(r'"Column1\tColumn2"')
    assert tokenizer.get_tokens_as_string() == r'Column1\tColumn2,<EOF>'

def test_069():
    """69. String with newline escape sequence"""
    tokenizer = Tokenizer(r'"Line1\nLine2"')
    assert tokenizer.get_tokens_as_string() == r'Line1\nLine2,<EOF>'

def test_070():
    """70. String with quote escape sequence"""
    tokenizer = Tokenizer(r'"He said \"Hello\""')
    assert tokenizer.get_tokens_as_string() == r'He said \"Hello\",<EOF>'

# Sinh ra 7 testcase cho các chuỗi lỗi của STRING_LITERAL, INTEGER_LITERAL, FLOAT_LITERAL

def test_071():
    """71. Float with multiple decimal points"""
    tokenizer = Tokenizer("3.14.15")
    assert tokenizer.get_tokens_as_string() == "3.14,.15,<EOF>"

def test_072():
    """72. Float with invalid exponent format"""
    tokenizer = Tokenizer("1.5e")
    assert tokenizer.get_tokens_as_string() == "1.5,e,<EOF>"

def test_073():
    """73. Float with multiple e notation"""
    tokenizer = Tokenizer("1e5e3")
    assert tokenizer.get_tokens_as_string() == "1e5,e3,<EOF>"

def test_074():
    """74. String with invalid escape sequence in middle"""
    tokenizer = Tokenizer('"abc_def"')
    assert tokenizer.get_tokens_as_string() == "abc_def,<EOF>"

def test_075():
    """75. Integer with invalid character in middle"""
    tokenizer = Tokenizer("123a45")
    assert tokenizer.get_tokens_as_string() == "123,a45,<EOF>"

def test_076():
    """76. Float starting with e notation only"""
    tokenizer = Tokenizer("e-5")
    assert tokenizer.get_tokens_as_string() == "e,-,5,<EOF>"

def test_077():
    """77. String with double backslash at end"""
    tokenizer = Tokenizer(r'"invalid\\"')
    assert tokenizer.get_tokens_as_string() == r'invalid\\,<EOF>'

# Testcases cho các ký tự đặc biệt đứng đầu
def test_078():
    """78. Dot operator alone"""
    tokenizer = Tokenizer(".")
    assert tokenizer.get_tokens_as_string() == ".,<EOF>"

def test_079():
    """79. Arrow operator alone"""
    tokenizer = Tokenizer("->")
    assert tokenizer.get_tokens_as_string() == "-,>,<EOF>"

def test_080():
    """80. Comma separator alone"""
    tokenizer = Tokenizer(",")
    assert tokenizer.get_tokens_as_string() == ",,<EOF>"
def test_081():
    """81. Colon separator alone"""
    tokenizer = Tokenizer(":")
    assert tokenizer.get_tokens_as_string() == ":,<EOF>"
def test_082():
    """82. Left brace separator alone"""
    tokenizer = Tokenizer("{")
    assert tokenizer.get_tokens_as_string() == "{,<EOF>"
def test_083():
    """83. Right brace separator alone"""
    tokenizer = Tokenizer("}")
    assert tokenizer.get_tokens_as_string() == "},<EOF>"
def test_084():
    """84. Increment operator alone"""
    tokenizer = Tokenizer("++")
    assert tokenizer.get_tokens_as_string() == "++,<EOF>"
def test_085():
    """85. Decrement operator alone"""
    tokenizer = Tokenizer("--")
    assert tokenizer.get_tokens_as_string() == "--,<EOF>"
def test_086():
    """86. Mixed special characters"""
    tokenizer = Tokenizer(".->, : { } ++ --")
    assert tokenizer.get_tokens_as_string() == ".,-,>,,,:,{,},++,--,<EOF>"
def test_087():
    """87. Dot operator in expression"""
    tokenizer = Tokenizer("obj.member + 5;")
    assert tokenizer.get_tokens_as_string() == "obj,.,member,+,5,;,<EOF>"
def test_088():
    """88. Arrow operator in expression"""
    tokenizer = Tokenizer("ptr->value - 10;")
    assert tokenizer.get_tokens_as_string() == "ptr,-,>,value,-,10,;,<EOF>"
def test_089():
    """89. Separators in function definition"""
    tokenizer = Tokenizer("void func(int a, float b) { return; }")
    assert tokenizer.get_tokens_as_string() == "void,func,(,int,a,,,float,b,),{,return,;,},<EOF>"
def test_090():
    """90. Increment and decrement in loop"""
    tokenizer = Tokenizer("for (auto i = 0; i < n; ++i) { --j; }")
    assert tokenizer.get_tokens_as_string() == "for,(,auto,i,=,0,;,i,<,n,;,++,i,),{,--,j,;,},<EOF>"
def test_091():
    """91. Complex use of special characters"""
    tokenizer = Tokenizer("result = obj.member->value + arr[i++];")
    assert tokenizer.get_tokens_as_string() == "result,=,obj,.,member,-,>,value,+,arr,Error Token ["
def test_092():
    """92. Special characters in comments"""
    tokenizer = Tokenizer("// This is a comment with special chars .->, : { } ++ --")
    assert tokenizer.get_tokens_as_string() == "<EOF>"
def test_093():
    """93. Special characters in strings"""
    tokenizer = Tokenizer("'{'}")
    assert tokenizer.get_tokens_as_string() == "Error Token '"
def test_094():
    """94. Mixed special characters and identifiers"""
    tokenizer = Tokenizer("myObj.member->func(param1, param2);")
    assert tokenizer.get_tokens_as_string() == "myObj,.,member,-,>,func,(,param1,,,param2,),;,<EOF>"
def test_095():
    """95. Special characters with no spaces"""
    tokenizer = Tokenizer("obj.member->value++;")
    assert tokenizer.get_tokens_as_string() == "obj,.,member,-,>,value,++,;,<EOF>"

def test_096():
    """96. Function with multiple parameters and operations"""
    tokenizer = Tokenizer("int calculate(int x, float y) { return x + y * 2; }")
    assert tokenizer.get_tokens_as_string() == "int,calculate,(,int,x,,,float,y,),{,return,x,+,y,*,2,;,},<EOF>"

def test_097():
    """97. Nested if-else with logical operators"""
    tokenizer = Tokenizer("if (x > 0 && y < 10) { if (z == 5) return 1; else return 0; }")
    assert tokenizer.get_tokens_as_string() == "if,(,x,>,0,&&,y,<,10,),{,if,(,z,==,5,),return,1,;,else,return,0,;,},<EOF>"

def test_098():
    """98. For loop with multiple variables and string output"""
    tokenizer = Tokenizer('for (auto i = 0; i < 100; ++i) { printString("Count: "); printInt(i); }')
    assert tokenizer.get_tokens_as_string() == "for,(,auto,i,=,0,;,i,<,100,;,++,i,),{,printString,(,Count: ,),;,printInt,(,i,),;,},<EOF>"

def test_099():
    """99. While loop with arithmetic and member access"""
    tokenizer = Tokenizer("while (node.value != 0) { result = result + node.value; node = node.next; }")
    assert tokenizer.get_tokens_as_string() == "while,(,node,.,value,!=,0,),{,result,=,result,+,node,.,value,;,node,=,node,.,next,;,},<EOF>"

def test_100():
    """100. Complex program with mixed statements and operations"""
    tokenizer = Tokenizer('auto sum = 0; for (auto i = 1; i <= 10; ++i) { sum = sum + i; } if (sum >= 50) printString("Large"); else printInt(sum);')
    assert tokenizer.get_tokens_as_string() == "auto,sum,=,0,;,for,(,auto,i,=,1,;,i,<=,10,;,++,i,),{,sum,=,sum,+,i,;,},if,(,sum,>=,50,),printString,(,Large,),;,else,printInt,(,sum,),;,<EOF>"
