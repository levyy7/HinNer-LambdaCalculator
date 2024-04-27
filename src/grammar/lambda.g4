grammar lambda;

root : term | EOF;

term : 
        abstraction | 
        application | 
        var         |
        atom        |
        op;

pterm : 
        abstraction         | 
        '(' application ')' | 
        var                 |
        atom                |
        op;


abstraction :
        <assoc=right> '\\' var '->' term ;

application : 
        application term |
        '(' ( op | abstraction) ')' term;


var : ID;

atom : NUM;

op: (SUM | SUB | MUL | DIV) ;

SUM : '+';
SUB : '-';
MUL : '*';
DIV : '/';
POW : '^';
NUM : [0-9]+ ;
ID  : ('a'..'z') ('a'..'z' | 'A'..'Z' | '_' | '0'..'9')*;
WS  : [ \t\n\r]+ -> skip ;