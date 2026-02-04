"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer


def test_001():
    source = """\t\r\n
    /* 123 // nothing here */
    // OKE
"""
    expected = "EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_002():
    source = "@"
    try:
        Tokenizer(source).get_tokens_as_string()
        assert False, "Expected ErrorToken but no exception was raised"
    except Exception as e:
        assert str(e) == "Error Token @"

def test_003():
    source = "auto auto1"
    expected = "auto,auto1,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_004():
    source = "+ ++"
    expected = "+,++,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_005():
    source = "baobao123"
    expected = "baobao123,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_006():
    source = "0   100   255   2500   -45"
    expected = "0,100,255,2500,-45,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_007():
    source = "0.0   3.14   -2.5   1.23e4   5.67E-2   1.   .5"
    expected = "0.0,3.14,-2.5,1.23e4,5.67E-2,1.,.5,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_008():
    source = """
    "This is a string containing tab \\t"
    "He asked me: \\"Where is John?\\""
"""
    expected = "This is a string containing tab \\t,He asked me: \\\"Where is John?\\\",EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_009():
    source = """
    "This is a string \n containing tab \\t"
"""
    try:
        Tokenizer(source).get_tokens_as_string()
        assert False, "Expected ErrorToken but no exception was raised"
    except Exception as e:
        assert str(e) == "Unclosed String: This is a string \n"
    
def test_010():
    source = """
    "This is a string \\z containing tab \\t"
"""
    try:
        Tokenizer(source).get_tokens_as_string()
        assert False, "Expected ErrorToken but no exception was raised"
    except Exception as e:
        assert str(e) == "Illegal Escape In String: This is a string \\z"

def test_011():
    source = "auto x = 5 + 3 * 2;"
    expected = "auto,x,=,5,+,3,*,2,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_012():
    source = "auto"
    expected = "auto,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_013():
    source = "break"
    expected = "break,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_014():
    source = "case"
    expected = "case,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_015():
    source = "continue"
    expected = "continue,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_016():
    source = "default"
    expected = "default,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_017():
    source = "else"
    expected = "else,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_018():
    source = "float"
    expected = "float,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_019():
    source = "for"
    expected = "for,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_020():
    source = "if"
    expected = "if,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_021():
    source = "int"
    expected = "int,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_022():
    source = "return"
    expected = "return,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_023():
    source = "string"
    expected = "string,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_024():
    source = "struct"
    expected = "struct,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_025():
    source = "switch"
    expected = "switch,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_026():
    source = "void"
    expected = "void,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_027():
    source = "while"
    expected = "while,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_028():
    source = "+"
    expected = "+,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_029():
    source = "-"
    expected = "-,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_030():
    source = "*"
    expected = "*,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_031():
    source = "/"
    expected = "/,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_032():
    source = "%"
    expected = "%,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_033():
    source = "="
    expected = "=,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_034():
    source = "=="
    expected = "==,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_035():
    source = "!="
    expected = "!=,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_036():
    source = ">"
    expected = ">,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_037():
    source = "<"
    expected = "<,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_038():
    source = ">="
    expected = ">=,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_039():
    source = "<="
    expected = "<=,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_040():
    source = "&&"
    expected = "&&,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_041():
    source = "||"
    expected = "||,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_042():
    source = "!"
    expected = "!,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_043():
    source = "++"
    expected = "++,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_044():
    source = "--"
    expected = "--,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_045():
    source = "."
    expected = ".,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_046():
    source = "( )"
    expected = "(,),EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_047():
    source = "{ }"
    expected = "{,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_048():
    source = "a,b"
    expected = "a,,,b,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_049():
    source = "a;b"
    expected = "a,;,b,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_050():
    source = "case 1:"
    expected = "case,1,:,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_051():
    source = "func(a,b,c)"
    expected = "func,(,a,,,b,,,c,),EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_052():
    source = "((x))"
    expected = "(,(,x,),),EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_053():
    source = "a.b"
    expected = "a,.,b,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_054():
    source = "a.b.c"
    expected = "a,.,b,.,c,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_055():
    source = "{a,b}"
    expected = "{,a,,,b,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_056():
    source = "_a a1 A_B _123abc"
    expected = "_a,a1,A_B,_123abc,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_057():
    source = "int1 float_ auto2"
    expected = "int1,float_,auto2,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_058():
    source = "abc123 123abc"
    expected = "abc123,123,abc,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_059():
    source = "x_y_z"
    expected = "x_y_z,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_060():
    source = "_0 _9"
    expected = "_0,_9,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_061():
    source = "0 1 9 10 999"
    expected = "0,1,9,10,999,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_062():
    source = "-1 -10 -999"
    expected = "-1,-10,-999,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_063():
    source = "2147483647 -2147483648"
    expected = "2147483647,-2147483648,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_064():
    source = "5+6"
    expected = "5,+,6,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_065():
    source = "10-3"
    expected = "10,-,3,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_066():
    source = "0.0 3.14 -2.5"
    expected = "0.0,3.14,-2.5,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_067():
    source = "1. .5 0. 0.5"
    expected = "1.,.5,0.,0.5,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_068():
    source = "1e10 2E+3 -4e-2 5E0"
    expected = "1e10,2E+3,-4e-2,5E0,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_069():
    source = "10.5e2 .75E-1"
    expected = "10.5e2,.75E-1,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_070():
    source = "1.23e4 5.67E-2"
    expected = "1.23e4,5.67E-2,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_071():
    source = "\"\" \"a\""
    expected = ",a,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_072():
    source = "\"Hello World\""
    expected = "Hello World,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_073():
    source = "\"Tab\\tSpace\""
    expected = "Tab\\tSpace,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_074():
    source = "\"Quote: \\\"\""
    expected = "Quote: \\\",EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_075():
    source = "\"Backslash\\\\\""
    expected = "Backslash\\\\,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_076():
    source = "\"Line1\\nLine2\""
    expected = "Line1\\nLine2,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_077():
    source = "\"Mix \\t \\n \\r\""
    expected = "Mix \\t \\n \\r,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_078():
    source = "\"Symbols !@#$%^&*()\""
    expected = "Symbols !@#$%^&*(),EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_079():
    source = "\"abc\\a\""
    try:
        Tokenizer(source).get_tokens_as_string()
        assert False, "Expected ErrorToken but no exception was raised"
    except Exception as e:
        assert str(e) == "Illegal Escape In String: abc\\a"

def test_080():
    source = "\"\\9\""
    try:
        Tokenizer(source).get_tokens_as_string()
        assert False, "Expected ErrorToken but no exception was raised"
    except Exception as e:
        assert str(e) == "Illegal Escape In String: \\9"

def test_081():
    source = '"abc'
    try:
        Tokenizer(source).get_tokens_as_string()
        assert False, "Expected ErrorToken but no exception was raised"
    except Exception as e:
        assert str(e) == "Unclosed String: abc"

def test_082():
    source = """
    "abc
"""
    try:
        Tokenizer(source).get_tokens_as_string()
        assert False, "Expected ErrorToken but no exception was raised"
    except Exception as e:
        assert str(e) == "Unclosed String: abc"

def test_083():
    source = "$"
    try:
        Tokenizer(source).get_tokens_as_string()
        assert False, "Expected ErrorToken but no exception was raised"
    except Exception as e:
        assert str(e) == "Error Token $"

def test_084():
    source = "`"
    try:
        Tokenizer(source).get_tokens_as_string()
        assert False, "Expected ErrorToken but no exception was raised"
    except Exception as e:
        assert str(e) == "Error Token `"

def test_085():
    source = "~"
    try:
        Tokenizer(source).get_tokens_as_string()
        assert False, "Expected ErrorToken but no exception was raised"
    except Exception as e:
        assert str(e) == "Error Token ~"

def test_086():
    source = "auto/*comment*/x"
    expected = "auto,x,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_087():
    source = "auto//comment\nx"
    expected = "auto,x,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_088():
    source = "/* comment */"
    expected = "EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_089():
    source = "/* line1\nline2 */ auto"
    expected = "auto,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_090():
    source = "// only comment"
    expected = "EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_091():
    source = "// comment with /* */\nauto"
    expected = "auto,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_092():
    source = "/* comment with // */ auto"
    expected = "auto,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_093():
    source = "int x = 10; float y = 3.14;"
    expected = "int,x,=,10,;,float,y,=,3.14,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_094():
    source = "if(x<10) x=x+1;"
    expected = "if,(,x,<,10,),x,=,x,+,1,;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_095():
    source = "while(x>0){x--; }"
    expected = "while,(,x,>,0,),{,x,--,;,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_096():
    source = "for(i=0;i<3;i++){}"
    expected = "for,(,i,=,0,;,i,<,3,;,i,++,),{,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_097():
    source = "switch(n){case 0: n=1; break; case 1: n=2; break; default: n=0;}"
    expected = "switch,(,n,),{,case,0,:,n,=,1,;,break,;,case,1,:,n,=,2,;,break,;,default,:,n,=,0,;,},EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_098():
    source = "struct S { int a; float b; string c; };"
    expected = "struct,S,{,int,a,;,float,b,;,string,c,;,},;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_099():
    source = "S s = {1,2.0,\"hi\"};"
    expected = "S,s,=,{,1,,,2.0,,,hi,},;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected

def test_100():
    source = "auto msg = \"Hi\"; printString(msg);"
    expected = "auto,msg,=,Hi,;,printString,(,msg,),;,EOF"
    assert Tokenizer(source).get_tokens_as_string() == expected