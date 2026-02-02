grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

// TODO: Define grammar rules here

//Lexical rules
// KEYWORDS
AUTO     : 'auto';
BREAK    : 'break';
CASE     : 'case';
CONTINUE : 'continue';
DEFAULT  : 'default';
ELSE     : 'else';
FLOAT    : 'float';
FOR      : 'for';
IF       : 'if';
INT      : 'int';
RETURN   : 'return';
STRING   : 'string';
STRUCT   : 'struct';
SWITCH   : 'switch';
VOID     : 'void';
WHILE    : 'while';

// OPERATORS
PLUS     : '+';
SUB      : '-';
MUL      : '*';
DIV      : '/';
MOD      : '%';
ASSIGN   : '=';
EQ       : '==';
NE       : '!=';
GT       : '>';
LT       : '<';
GE       : '>=';
LE       : '<=';
AND      : '&&';
OR       : '||';
NOT      : '!';
INC      : '++';
DEC      : '--';
DOT      : '.';

// SEPARATOR
LPAREN   : '(';
RPAREN   : ')';
LBRACE   : '{';
RBRACE   : '}';
COMMA    : ',';
SEMI     : ';';
COLON    : ':';

//IDENTIFIERS
ID: [A-Za-z_][A-Za-z0-9_]*;
GLOBAL_ID: '@' ID;

// LITERAL
INT_LIT: [1-9] [0-9]* | '0';
FLOAT_LIT: ([0-9]+ '.' [0-9]* | '.' [0-9]+) ([Ee] [+-]? [0-9]+)? | [0-9]+ [Ee] [+-]? [0-9]+;
STRING_LIT: '"' STR_CHAR* '"' {self.text = self.text[1:-1] };
fragment STR_CHAR: ~[\n\\"] | ESC_SEQ;
fragment ESC_SEQ: '\\' [bfrnt\\"];
fragment ESC_ILLEGAL: '\\' ~[bfrnt\\"];

// COMMENT, WHITE SPACE
LINE_COMMENT
    :   '//' ~[\r\n]* -> skip
    ;

BLOCK_COMMENT
    :   '/*' .*? '*/' -> skip
    ;
WS: [ \t\r\n]+ -> skip;

// ERROR
ERROR_CHAR: .;
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL {
    raise IllegalEscape(self.text[1:])
};
UNCLOSE_STRING: '"' STR_CHAR* ('\r\n' | '\n' | EOF) {
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[1:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[1:-1])
    else:
        raise UncloseString(self.text[1:])
};

// EXPRESSIONS - Following operator precedence from specification
expression: assignment;

assignment: logical_or (ASSIGN assignment)?;

logical_or: logical_and (OR logical_and)*;

logical_and: equality (AND equality)*;

equality: relational ((EQ | NE) relational)*;

relational: additive ((LT | LE | GT | GE) additive)*;

additive: multiplicative ((PLUS | SUB) multiplicative)*;

multiplicative: unary ((MUL | DIV | MOD) unary)*;

unary: (NOT | SUB | PLUS | INC | DEC) unary | postfix;

postfix: primary ((INC | DEC))?;

primary: ID (DOT ID)* | literal | function_call | LPAREN expression RPAREN;

function_call: ID LPAREN argument_list? RPAREN;

argument_list: expression (COMMA expression)*;

// LITERALS
literal: INT_LIT | FLOAT_LIT | STRING_LIT | struct_init;

struct_init: LBRACE argument_list? RBRACE;

// PROGRAM STRUCTURE
program: struct_decl* function* EOF;

struct_decl: STRUCT ID LBRACE struct_member* RBRACE SEMI;

struct_member: type_name ID SEMI;

function: type_name? ID LPAREN param_list? RPAREN LBRACE statement* RBRACE;

param_list: param (COMMA param)*;

param: ID COLON type_name;

type_name: INT | FLOAT | STRING | VOID | AUTO | ID;

// LVALUE - for assignment targets
lvalue: ID (DOT ID)*;

// STATEMENTS
statement: var_decl SEMI
         | assign_stmt SEMI
         | if_stmt
         | while_stmt
         | for_stmt
         | switch_stmt
         | break_stmt SEMI
         | continue_stmt SEMI
         | return_stmt SEMI
         | expr_stmt SEMI
         | block_stmt;

var_decl: type_name ID (ASSIGN expression)?;

assign_stmt: lvalue ASSIGN expression;

if_stmt: IF LPAREN expression RPAREN statement (ELSE statement)?;

while_stmt: WHILE LPAREN expression RPAREN statement;

for_stmt: FOR LPAREN var_decl? SEMI expression? SEMI assign_stmt? RPAREN statement;

switch_stmt: SWITCH LPAREN expression RPAREN LBRACE switch_case* RBRACE;

switch_case: CASE INT_LIT COLON statement*
           | DEFAULT COLON statement*;

break_stmt: BREAK;

continue_stmt: CONTINUE;

return_stmt: RETURN expression?;

expr_stmt: expression;

block_stmt: LBRACE statement* RBRACE;

