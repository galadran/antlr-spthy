grammar Tamarinrule;

//Question mark stands for: zero or one
//Plus stands for: one or more
//Star stands for: zero or more

SQUOTE : '\'';
TILDQ : '~\'';
PLAY : '▶';
BAR : '∥';

rules : (protoRule)*;

protoRule :   RULE Identifier  ':' genericRule
            | RULE Identifier  ':' letBlock genericRule
            ;

letBlock : LET definition+ IN;

definition : term '=' term;

genericRule : '[' factList ']'
            ('-->' | '--[' factList ']->')
            '[' factList ']'
            ;

fact :  factIdentifier '(' termList ')'; 

factList : (fact (',' fact)*)?;

term : '<' termList '>'
     | term '^' term
     | varIdentifier
     | Identifier '(' termList  ')';

termList : (term (',' term)*)?;

factIdentifier : (Identifier | '!' Identifier );

varIdentifier : (Identifier | '~' Identifier | '\'' Identifier '\'' | '$' Identifier);

LET : 'let';
RULE : 'rule';
IN : 'in';

Identifier: LetterNum (LetterNum | '_')*;

Digit : ('0' .. '9');

Letter : ('a'..'z' | 'A'..'Z');

LetterNum : (Letter | Digit);


//
// Whitespace and comments
//

WS: ( '\t' | ' ' | '\r' | '\n' | '\u000C' )+    -> channel(HIDDEN) ;

//COMMA : ',' -> skip;

COMMENT
    : '/*' .*? '*/' -> skip
;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
;
