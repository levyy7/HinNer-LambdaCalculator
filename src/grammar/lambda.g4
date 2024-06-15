grammar lambda;

root    : term EOF  #regTerm
        | type EOF  #typeTerm
        | EOF       #nothing
        ;

type    : left=(OP | NUM | ID) '::' typeRec ('->' typeRec)*
        ;

typeRec : '(' typeRec '->' typeRec ('->' typeRec)* ')'  #typeFunction
        | CAPS                                          #typeValue
        ;

term    : '(' term ')'                                  #termParenthesis
        | term term                                     #application
        | '\\' left=ID '->' right=term                  #abstraction
        | ID                                            #id
        | NUM                                           #num
        | OP                                            #op
        ;             


OP : '(+)' | '(-)' | '(*)' | '(/)' | '(^)';
NUM : [0-9]+ ;
ID  : ('a'..'z') ('a'..'z' | 'A'..'Z' | '_' | '0'..'9')*;
CAPS: ('A'..'Z')+;
WS  : [ \t\n\r]+ -> skip ;

LEXICAL_ERROR : . ;