grammar bezBoolow;

file_:
    inputBlock blockseq EOF;

blockseq:
    block+;

block:
    variableDefinition
	|ifBlock
	|loopBlock
	|printBlock
	|inputBlock
	;

printBlock:
    PRINT LPAREN printSeq* RPAREN ENDCHAR;

printSeq:
    atom
    |atom (',' atom)*;

inputBlock:
    INPUT EQ INPUT LPAREN inputSeq RPAREN ENDCHAR;

inputSeq:
    filename;

filename:
    QUOTATION FILENAME QUOTATION;

variableDefinition:
    VARIABLE EQ equation ENDCHAR|
    VARIABLE EQ expression ENDCHAR;

loopBlock:
    WHILE LPAREN expression RPAREN LPARENCURLY blockseq RPARENCURLY
    ;

ifBlock:
    IF LPAREN expression RPAREN LPARENCURLY blockseq RPARENCURLY;

expression
    :   expression (OR | AND) expression
    |   expression (GT | LT) expression
    |   expression (EQ_LOGICAL | NOT_EQ_LOGICAL) expression
    |   LPAREN expression RPAREN
    |   NOT expression
    |   equation;

equation
   :   equation (TIMES | DIV)  equation
   |   equation (PLUS | MINUS) equation
   |   LPAREN equation RPAREN
   |   MINUS? atom
   ;


atom:
    NUM  |FLOAT |VARIABLE
   ;

NUM:
    ('0'..'9')
    |('1'..'9')+('0'..'9')*;

 FLOAT:
    ('0'..'9')+
     |('0'..'9')+ '.' ('0'..'9')*
     |'.' ('0'..'9')+;

VARIABLE:
    VAR_NAME ID_VAR;

VAR_NAME:
    'v_';

ID_VAR:
    ('1'..'9')('0'..'9')*;


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
