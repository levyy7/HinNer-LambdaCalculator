grammar lambda;

root    : term  #regTerm
        | EOF   #nothing
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
NUM : [0-9]+ ;
ID  : ('a'..'z') ('a'..'z' | 'A'..'Z' | '_' | '0'..'9')*;
WS  : [ \t\n\r]+ -> skip ;