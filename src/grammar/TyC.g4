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
INC      : '++';
DEC      : '--';
LE       : '<=';
GE       : '>=';
EQ       : '==';
NEQ      : '!=';
AND      : '&&';
OR       : '||';
ASSIGN   : '=';
GT       : '>';
LT       : '<';
ADD      : '+';
SUB      : '-';
MUL      : '*';
DIV      : '/';
MOD      : '%';
NOT      : '!';
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
ID: [A-Za-z_] [A-Za-z0-9_]*;

// LITERAL
FLOAT_LIT: DIGITS '.' DIGITS? EXP? | '.' DIGITS EXP? | DIGITS EXP;
INT_LIT: DIGITS;

// STRING LITERAL AND ERROR DETECTION
fragment DIGITS: [0-9]+;
fragment EXP: [Ee] [+-]? DIGITS;
fragment STR_CHAR: ~[\r\n\\"] | ESC_SEQ;
fragment ESC_SEQ: '\\' [bfrnt\\"];
fragment ESC_ILLEGAL: '\\' ~[bfrnt\\"\r\n];

ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL {
    self.text = self.text[1:]
};
UNCLOSE_STRING: '"' STR_CHAR* ('\r\n' | '\n' | EOF) {
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        self.text = self.text[1:-2]
    elif (self.text[-1] == '\n'):
        self.text = self.text[1:-1]
    else:
        self.text = self.text[1:]
};
STRING_LIT: '"' STR_CHAR* '"' {self.text = self.text[1:-1] };

// COMMENT, WHITE SPACE
LINE_COMMENT
    :   '//' ~[\r\n]* -> skip
    ;

BLOCK_COMMENT
    :   '/*' .*? '*/' -> skip
    ;
WS: [ \t\r\n]+ -> skip;

ERROR_CHAR: .;

// TODO EXPRESSION AND LITERAL
program: decl* EOF;
decl: struct_decl | func_decl;
struct_decl: STRUCT ID LBRACE member_decl* RBRACE SEMI;
member_decl: type_spec ID SEMI;
func_decl: return_type? ID LPAREN param_list? RPAREN block_stmt;
return_type: type_spec | VOID;
param_list: param (COMMA param)*;
param: type_spec ID;
type_spec: INT | FLOAT | STRING | ID;
block_stmt: LBRACE statement* RBRACE;

statement:
    block_stmt
    | var_decl SEMI
    | if_stmt
    | while_stmt
    | for_stmt
    | switch_stmt
    | break_stmt SEMI
    | continue_stmt SEMI
    | return_stmt SEMI
    | expr_stmt SEMI;

var_decl: AUTO ID (ASSIGN expr)? | type_spec ID (ASSIGN expr)?;
if_stmt: IF LPAREN expr RPAREN statement (ELSE statement)?;
while_stmt: WHILE LPAREN expr RPAREN statement;
for_stmt: FOR LPAREN for_init? SEMI expr? SEMI for_update? RPAREN statement;
for_init: var_decl | expr;
for_update: expr;
switch_stmt: SWITCH LPAREN expr RPAREN LBRACE switch_block_item* RBRACE;
switch_block_item: case_clause | default_clause;
case_clause: CASE expr COLON statement*;
default_clause: DEFAULT COLON statement*;

break_stmt: BREAK;
continue_stmt: CONTINUE;
return_stmt: RETURN expr?;
expr_stmt: expr;

expr: assignment;
assignment: logical_or (ASSIGN assignment)?;
logical_or: logical_and (OR logical_and)*;
logical_and: equality (AND equality)*;
equality: relational ((EQ | NEQ) relational)*;
relational: additive ((LT | LE | GT | GE) additive)*;
additive: multiplicative ((ADD | SUB) multiplicative)*;
multiplicative: unary ((MUL | DIV | MOD) unary)*;
unary: (INC | DEC | NOT | ADD | SUB) unary | postfix;
postfix: primary postfix_part*;
postfix_part: LPAREN arg_list? RPAREN | DOT ID | INC | DEC;
arg_list: expr (COMMA expr)*;
primary: literal | ID | LPAREN expr RPAREN | struct_literal;
literal: INT_LIT | FLOAT_LIT | STRING_LIT;
struct_literal: LBRACE expr_list? RBRACE;
expr_list: expr (COMMA expr)*;

