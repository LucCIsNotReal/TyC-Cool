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
CONTINUE : 'continue';
IF       : 'if';
ELSE     : 'else';
FOR      : 'for';
BOOL     : 'bool';
NUMBER   : 'number';
STRING   : 'string';
TRUE     : 'T';
FALSE    : 'F';
FUNC     : 'func';
ENDFUNC  : 'endfunc';
CALL     : 'call';
RETURN   : 'return';

// OPERATORS
PLUS     : '+';
SUB      : '-';
MUL      : '*';
EQ       : '=';
GT       : '>';
LT       : '<';
POW      : '**';
HASH     : '#';
ARROW    : '<-';

// SEPARATOR
LPAREN   : '(';
RPAREN   : ')';
LBRACK   : '[';
RBRACK   : ']';
LBRACE   : '{';
RBRACE   : '}';
COMMA    : ',';
SEMI     : ';';
COLON    : ':';

//IDENTIFIERS
ID: [A-Za-z_] [A-Za-z0-9_]*;
GLOBAL_ID: '@' ID;

// LITERAL
INT_LIT: [1-9] [0-9]* | '0';
FLOAT_LIT: [0-9]+ ('.' [0-9]* [Ee] [+-]? ([0-9]+) |  '.' [0-9]* | [Ee] [+-]? ([0-9]+));
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
    raise illegalEscape(self.text[1:])
};
UNCLOSE_STRING: '"' STR_CHAR* ('\r\n' | '\n' | EOF) {
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise uncloseString(self.text[1:-2])
    elif (self.text[-1] == '\n'):
        raise uncloseString(self.text[1:-1])
    else:
        raise uncloseString(self.text[1:])
};

// TODO EXPRESSION AND LITERAL
list_expression: expression COMMA list_expression | expression;
expression: expression1 (GT | LT | EQ) expression1 | expression1;
expression1: expression2 POW expression1 | expression2;
expression2: expression2 (PLUS | SUB) expression3 | expression3;
expression3: expression3 MUL expression4 | expression4;
expression4: SUB expression4 | expression5;
expression5: LBRACK expression RBRACK expression5 | expression6;
expression6: ID | GLOBAL_ID | literal | function_call | LPAREN expression RPAREN;
function_call: CALL ID (ARROW list_expression)?;
 
list_literal: literal COMMA list_literal | literal;
literal: TRUE | FALSE | INT_LIT | FLOAT_LIT | STRING_LIT | array_lit;
array_lit: LT list_literal GT;

// TODO DECLARED
program: variable* function* EOF;
variable: all_type GLOBAL_ID EQ literal SEMI;
function: FUNC all_type? ID LPAREN list_param? RPAREN COLON list_statement ENDFUNC;

list_param: param COMMA list_param | param;
param: ID COLON all_type;
all_type: NUMBER | BOOL | STRING;


// TODO STATEMENT
list_statement: statement list_statement | statement;
statement: declared_statement SEMI
		| assign_statement SEMI
		| if_statement
		| for_statement
		| continue_statement SEMI
		| call_statement SEMI
		| return_statement SEMI
        | block_statement;
declared_statement: all_type ID ARROW expression;
assign_statement: lhs ARROW expression;
lhs: LBRACK expression RBRACK lhs | ID;

if_statement: IF expression block_statement (ELSE block_statement)?;
for_statement: FOR LPAREN (declared_statement | ID ARROW expression) SEMI (GT | LT | EQ) expression SEMI HASH expression RPAREN block_statement;
continue_statement: CONTINUE;
call_statement: function_call;
return_statement: RETURN expression?;
block_statement: LBRACE list_statement? RBRACE;


