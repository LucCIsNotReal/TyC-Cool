"""Parser test cases for TyC compiler"""

import pytest

from tests.utils import Parser


def test_parser_minimal_function():
    source = "func number foo(): return 1; endfunc"
    parser = Parser(source)
    assert parser.parse() == "success"


def test_parser_global_and_function():
    source = "number @x = 0; func number main(): return @x; endfunc"
    parser = Parser(source)
    assert parser.parse() == "success"


def test_parser_if_else_block():
    source = "func number main(): if T { return 1; } else { return 2; } endfunc"
    parser = Parser(source)
    assert parser.parse() == "success"


def test_parser_for_statement():
    source = "func number main(): for (number i <- 0; < 10; # 1) { continue; } return 0; endfunc"
    parser = Parser(source)
    assert parser.parse() == "success"


def test_parser_missing_semicolon_error():
    source = "func number main(): return 1 endfunc"
    parser = Parser(source)
    result = parser.parse()
    assert result != "success"
    assert "Error on line" in result
