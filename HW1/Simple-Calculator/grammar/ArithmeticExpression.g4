grammar ArithmeticExpression;

start: assigns EOF;
assigns: assign NEWLINE* assigns* | assign;
assign: ID '=' expr;
expr: expr ADD term | expr SUB term | term | WS;
term: term MUL factor | term DIV factor | factor;
factor: number | signednum | LPAREN expr RPAREN | STRING | ID;

number: FLOAT | INTEGER;
signednum: ('+' | '-')* number;
//signednum: (SIGN)* number;

//signednum: (sign)* number;
//sign: ('+' | '-');

//SIGN: '+' | '-';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
LPAREN: '(';
RPAREN: ')';
STRING: '"'.*?'"';
WS: [ \t\r]+ -> skip;
NEWLINE: '\n';
ID: [a-z,A-Z] ([a-z,A-Z] | [0-9])*;

FLOAT: [0-9]*'.'[0-9]+;
INTEGER: [0-9]+;

//SIGN: '+' | '-';

//postorder checking
//tagging