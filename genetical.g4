grammar genetical;

file_ : blockseq? EOF;

blockseq: block+;

block:
	variableDefinition
	|variableOperation
	| ifBlock
	| loopBlock
	;

variableOperation:
    VARIABLE EQ expression ENDCHAR
    | VARIABLE EQ logicalExp ENDCHAR;


loopBlock:
    WHILE LPAREN logicalExp RPAREN LPARENCURLY blockseq RPARENCURLY
    ;

ifBlock:
    IF LPAREN logicalExp RPAREN LPARENCURLY blockseq RPARENCURLY
    ;



variableDefinition:
    variable EQ NUMBER ENDCHAR|
    variable EQ equation ENDCHAR
//   |variable EQ expression ENDCHAR
    ;

//logicalExp:
//    expression relopLogical expression
//    ;

logicalExp
   :  logicalExp  relopLogical logicalExp|
   expression relopLogical logicalExp |
   expression relopLogical expression
   |  LPAREN expression RPAREN
   |  (PLUS | MINUS)* atom

    ;

relopLogical
   : EQ_LOGICAL
   | GT
   | LT
  |AND
  |OR
   ;


equation
   : expression relop expression|
   expression relopLogical expression
   ;

expression
   :  expression  POW expression 
   |  expression  (TIMES | DIV)  expression 
   |  expression  (PLUS | MINUS) expression 
   |  LPAREN expression RPAREN 
   |  (PLUS | MINUS)* atom 
   ;


NUMBER:
    DIGIT+;

atom:
    NUMBER
    |variable
   ;


variable
   : VARIABLE
   ;

relop
   : EQ
   | GT
   | LT
   ;


VARIABLE
   : BOOL_VARIABLE | NUM_VARIABLE
   ;

BOOL_VARIABLE
    : BOOL_NAME ID_NUM
    ;

NUM_VARIABLE
    : NUM_NAME ID_NUM
    ;

NUM_NAME
    : 'n_'
    ;

BOOL_NAME
    : 'b_'
    ;

ID_NUM
    : [0-9]+
    ;

fragment
DIGIT   :   ('0'..'9');

//fragment NUMBER
//    : ('0'..'9')
//  | ('0' .. '9') + ('.' ('0' .. '9') +)?
//   ;

fragment UNSIGNED_INTEGER
   : ('0' .. '9')+
   ;


fragment SIGN
   : ('+' | '-')
   ;


LPAREN
   : '('
   ;


RPAREN
   : ')'
   ;

LPARENCURLY
    : '{'
    ;

RPARENCURLY
    : '}'
    ;


PLUS
   : '+'
   ;


MINUS
   : '-'
   ;


TIMES
   : '*'
   ;


DIV
   : '/'
   ;


GT
   : '>'
   ;


LT
   : '<'
   ;


EQ
   : '='
   ;

EQ_LOGICAL
   : '=='
   ;


POINT
   : '.'
   ;


POW
   : '^'
   ;

IF
    : 'if'
    ;
AND
    : ' &'
    ;

OR
    :'|'
    ;
WS
   : [ \r\n\t] + -> skip
   ;
WHILE : 'while';

ENDCHAR
    :   ';'
    ;
