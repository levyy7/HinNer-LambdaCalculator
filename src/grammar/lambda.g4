grammar lambda;

root    : term  #regTerm
        | type  #typeTerm
        | EOF   #nothing
        ;

type    : left=NUM '::' right=CAPS                                              #literalType
        | '(' left=OP ')' '::' right1=CAPS '->' right2=CAPS '->' right3=CAPS    #functionType
        ;

term    : abstraction   
        | application   
        | var           
        | atom          
        | op            
        ;             


abstraction :
        <assoc=right> '\\' left=var '->' right=term ;

application     : left=application right=term            #extApp                               
                | '(' left=abstraction ')' right=term    #absApp
                | '(' left=op ')' right=term             #opApp
                ;


var     : ID
        ;

atom    : 
        NUM;

op      : SUM   #sumOp
        | SUB   #subOp
        | MUL   #mulOp
        | DIV   #divOp
        ;

SUM : '+';
SUB : '-';
MUL : '*';
DIV : '/';
POW : '^';
OP  : ('+' | '-' | '*' | '/');
NUM : [0-9]+ ;
ID  : ('a'..'z') ('a'..'z' | 'A'..'Z' | '_' | '0'..'9')*;
CAPS: ('A'..'Z')+;
WS  : [ \t\n\r]+ -> skip ;