grammar genetical;

file_ : inputBlock blockseq EOF;

blockseq: block+;

block:
	variableDefinition
	| ifBlock
	| loopBlock
	| printBlock
	|inputBlock
	;

printBlock:
    PRINT LPAREN printSeq* RPAREN ENDCHAR;

printSeq:
    atom|
    atom (',' atom)*;

inputBlock:
    INPUT EQ INPUT LPAREN inputSeq RPAREN ENDCHAR;

inputSeq:
    filename;

filename:
    QUOTATION FILENAME QUOTATION
;
variableDefinition:
    numDefinition|
    boolDefinition;

numDefinition:
    NUM_NAME ID_NUM  EQ '12' ENDCHAR|
    NUM_VARIABLE EQ equation ENDCHAR;


boolDefinition:
    BOOL_VARIABLE EQ expression ENDCHAR|
    BOOL_VARIABLE EQ ('0'|'1') ENDCHAR;



loopBlock:
    WHILE LPAREN expression RPAREN LPARENCURLY blockseq RPARENCURLY
    ;

ifBlock:
    IF LPAREN expression RPAREN LPARENCURLY blockseq RPARENCURLY
    ;

expression
    :   expression (OR | AND) expression
    |   expression (GT | LT) expression
    |   expression (EQ_LOGICAL | NOT_EQ_LOGICAL) expression
    |   LPAREN expression RPAREN
    |   NOT expression
    |   equation ;

equation
   :   equation (TIMES | DIV)  equation
   |   equation (PLUS | MINUS) equation
   |   LPAREN equation RPAREN
   |   MINUS? atom
   ;

NUMBER:
   ('0'..'9')| ('1'..'9')  ('0'..'9')+  ;

atom:
 FLOAT
   ;
 INT :    '0'..'9'+
     ;

 DOT: '.';

 FLOAT
     :   ('0'..'9')+ '.' ('0'..'9')*
     |   '.' ('0'..'9')+
     |   ('0'..'9')+
     ;


//VARIABLE
//   : BOOL_VARIABLE | NUM_VARIABLE
//   ;

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
    : ('1'..'9')('0'..'9')*
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

NOT_EQ_LOGICAL
   : '!='
   ;



QUOTATION:
    '"'
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
NOT    : '!' ;

PRINT : 'print'
;
INPUT : 'input' ;

FILENAME:
    ((  'a'..'z'  ) | ('A'..'Z')|('0'..'9'))+'.txt'
;