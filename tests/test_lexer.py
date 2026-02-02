"""Lexer test cases for TyC compiler"""

import pytest

from src.grammar.lexererr import ErrorToken, IllegalEscape, UncloseString
from tests.utils import Tokenizer


def test_lexer_simple_declaration():
    source = "number @x = 10;"
    tokenizer = Tokenizer(source)
    expected = "NUMBER,number,GLOBAL_ID,@x,EQ,=,INT_LIT,10,SEMI,;,EOF"
    assert tokenizer.get_tokens_as_string() == expected


def test_lexer_float_and_string():
    source = 'number @y = 1.23e-4; string @s = "hi\\n";'
    tokenizer = Tokenizer(source)
    expected = (
        "NUMBER,number,GLOBAL_ID,@y,EQ,=,FLOAT_LIT,1.23e-4,SEMI,;,"
        "STRING,string,GLOBAL_ID,@s,EQ,=,STRING_LIT,hi\\n,SEMI,;,EOF"
    )
    assert tokenizer.get_tokens_as_string() == expected


def test_lexer_comments_are_skipped():
    source = "// line comment\nnumber @x = 1; /* block */"
    tokenizer = Tokenizer(source)
    expected = "NUMBER,number,GLOBAL_ID,@x,EQ,=,INT_LIT,1,SEMI,;,EOF"
    assert tokenizer.get_tokens_as_string() == expected


def test_lexer_error_token():
    source = "@@"
    tokenizer = Tokenizer(source)
    with pytest.raises(ErrorToken) as excinfo:
        tokenizer.get_tokens_as_string()
    assert str(excinfo.value) == "Error Token @"


def test_lexer_unclosed_string():
    source = '"abc'
    tokenizer = Tokenizer(source)
    with pytest.raises(UncloseString) as excinfo:
        tokenizer.get_tokens_as_string()
    assert str(excinfo.value) == "Unclosed String: abc"
