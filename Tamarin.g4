grammar Tamarin;

//Question mark stands for: zero or one
//Plus stands for: one or more
//Star stands for: zero or more

SQUOTE : '\'';
TILDQ : '~\'';
PLAY : '▶';
BAR : '∥';

theory : 'theory' identifier 'begin' (theorycomponent)* 'end';

//Modified removing     | formalComment
theorycomponent : builtins
    | functions
    | equations
    | restriction
    | lemma
    | protoRule
    | intrRule
    ;

builtins : 'builtins' ':' (builtin_theory)+;

builtin_theory : 'diffie-hellman'
    | 'bilinear-pairing'
    | 'multiset'
    | 'xor'
    | 'symmetric-encryption'
    | 'asymmetric-encryption'
    | 'signing'
    | 'revealing-signing'
    | 'hashing'
    ;

functions : 'functions' ':' (function_symbol)+;

function_symbol : identifier '/' natural | identifier '/' natural '[private]';

equations : 'equations' ':' equation (',' equation)*;

equation : termNoPub '=' termNoPub;

restriction : 'restriction' identifier ':' '"' standardFormula '"';


lemma : 'lemma' identifier ':' '"' standardFormula '"'
    | 'lemma' identifier ':' '"' standardFormula '"' proofSkeleton
    | 'lemma'  identifier  ':' ('all-traces' | 'exists-trace') '"' standardFormula '"'
    | 'lemma'  identifier ':' ('all-traces' | 'exists-trace') '"' standardFormula '"' proofSkeleton
    | 'lemma' identifier lemmaAttribute (',' lemmaAttribute)* ':'  '"' standardFormula '"' 
    | 'lemma' identifier lemmaAttribute (',' lemmaAttribute)* ':'  '"' standardFormula '"' proofSkeleton
    | 'lemma' identifier lemmaAttribute (',' lemmaAttribute)* ':' 'all-traces' | 'exists-trace' '"' standardFormula '"'
    | 'lemma' identifier lemmaAttribute (',' lemmaAttribute)* ':' 'all-traces' | 'exists-trace' '"' standardFormula '"' proofSkeleton
    | 'lemma' modulo identifier ':' '"' standardFormula '"'
    | 'lemma' modulo identifier ':' '"' standardFormula '"' proofSkeleton
    | 'lemma' modulo identifier  ':' ('all-traces' | 'exists-trace') '"' standardFormula '"'
    | 'lemma' modulo identifier ':' ('all-traces' | 'exists-trace') '"' standardFormula '"' proofSkeleton
    | 'lemma' modulo identifier lemmaAttribute (',' lemmaAttribute)* ':'  '"' standardFormula '"' 
    | 'lemma' modulo identifier lemmaAttribute (',' lemmaAttribute)* ':'  '"' standardFormula '"' proofSkeleton
    | 'lemma' modulo identifier lemmaAttribute (',' lemmaAttribute)* ':' 'all-traces' | 'exists-trace' '"' standardFormula '"'
    | 'lemma' modulo identifier lemmaAttribute (',' lemmaAttribute)* ':' 'all-traces' | 'exists-trace' '"' standardFormula '"' proofSkeleton;

lemmaAttribute : 'sources'
    | 'reuse'
    | 'use_induction'
    | 'hide_lemma=' identifier
    | 'heuristic=' identifier
    | 'left'
    | 'right'
    ;

proofSkeleton : 'SOLVED'
    | 'by' proofMethod
    | proofMethod proofSkeleton
    | proofMethod 'case' identifier proofSkeleton ('next' 'case' identifier proofSkeleton)* 'qed'
    ;

proofMethod : 'sorry'
    | 'simplify'
    | 'solve' '(' goal ')'
    | 'contradiction'
    | 'induction'
    ;

goal : fact PLAY naturalSubscript node_var
    | fact '@' node_var
    | '(' node_var ',' natural ')' '~~>' '(' node_var ',' natural ')'
    | guardedFormula (BAR guardedFormula)*
    | 'splitEqs' '(' natural ')'
    ;

naturalSubscript : ('₀'|'₁'|'₂'|'₃'|'₄'|'₅'|'₆'|'₇'|'₈'|'₉')+;

//Modified removing ruleAttribute
protoRule : 'rule' identifier  ':' genericRule
| 'rule' identifier ':' letBlock genericRule
//| 'rule' identifier ruleAttribute (',' ruleAttribute)* ':' genericRule
//| 'rule' identifier ruleAttribute (',' ruleAttribute)* ':' letBlock genericRule
| 'rule' modulo identifier ':' genericRule
| 'rule' modulo identifier ':' letBlock genericRule
//| 'rule' modulo identifier ruleAttribute (',' ruleAttribute)* ':' genericRule
//| 'rule' modulo identifier ruleAttribute (',' ruleAttribute)* ':' letBlock genericRule
;

//ruleAttribute : 'colour=' hexColor
//    | 'color=' hexColor;

//hexColor : hexDigit+
//    | '#' hexDigit+
//    |'SQUOTE hexDigit+ SQUOTE 
//    | SQUOTE '#' hexDigit+ SQUOTE 
//    ;

//hexDigit : ('A'-'F' | digit);


letBlock : 'let' definition+ 'in';

definition : msg_var '=' msetterm;

intrRule : 'rule' identifier genericRule
    | 'rule' identifier natural genericRule
    | 'rule' modulo identifier genericRule
    | 'rule' modulo identifier natural genericRule
    ;

genericRule : '[' (fact)+ ']'
    ('-->' | '--[' (fact)+ ']->')
    '[' (fact)+ ']';

modulo : '(' 'modulo' ('E' | 'AC') ')';

fact : factIdentifier '('')'
| factIdentifier '(' msetterm (',' msetterm)* ')'
| '!' factIdentifier '('')'
| '!' factIdentifier '(' msetterm (',' msetterm)* ')'
; 

//Error here: I cannot use _ for the name of the facts
factIdentifier : (alphaNum | '_')+;

llit : SQUOTE  identifier SQUOTE
    | TILDQ identifier SQUOTE
    | nonnode_var
    ;

llitNoPub : TILDQ identifier SQUOTE
    | nonnode_var
    ;

nonnode_var : identifier
            | identifier '.' natural
            | identifier '.' natural ':' 'pub'
            | identifier '.' natural ':' 'fresh'
            | identifier ':' 'pub'
            | identifier ':' 'fresh'
            | '$' identifier
            | '$' identifier '.' natural
            | '~' identifier
            | '~' identifier '.' natural
            | msg_var
            ;

msg_var : identifier
    | identifier ':' 'msg'
    | identifier '.' natural
    | identifier '.' natural ':' 'msg'
    ;

node_var : identifier
    | identifier '.' natural
    | identifier '.' natural ':' 'node'
    | identifier ':' 'node'
    | '#' identifier
    | '#' identifier '.' natural
    ;

lvar : node_var | nonnode_var;

// This has a FIXME on it, currently it parses a standard formula and converts it afterwards
// to guarded, the FIXME says to write a proper parser instead.

guardedFormula : standardFormula;

standardFormula : implication
    | implication ('<=>' | '⇔') implication
	;

implication : disjunction
	| disjunction ('==>' | '⇒') implication
	;

disjunction : conjunction (('|' | '∨') conjunction)*;

conjunction : negation (('&' | '∧') negation)*;

negation : fatom
    | ('¬' | 'not') fatom
	;

fatom : '⊥'
    | 'F'
    | '⊤'
    | 'T'
    | blatom
    | ('Ex' | '∃' | 'All' | '∀') (lvar)+ '.' standardFormula
    | '(' standardFormula ')'
    ;

blatom : 'last' '(' node_var ')'
    | fact '@' node_var
    | node_var '<' node_var
    | msetterm '=' msetterm
    | node_var '=' node_var
    ;

identifier : (alphaNum | '_')+;

// If multisets are not enabled, this only allows the first case
msetterm : xorterm
    | xorterm '+' xorterm
    ;

// If xor is not enabled, this only allows the first case
xorterm : multterm
    | multterm ('XOR' | '⊕') multterm
    ;

// If diffie-hellman is not enabled, this only allows the first case
multterm : term
    | term '*' term
    | term '^' term
    ;

//Modified to remove nullaryApp
//Modified removing literal
term : tupleterm
    | '(' msetterm ')'
    | identifier '(' (tupleterm | (msetterm)+) ')'
    | identifier '{' tupleterm '}' term
    | llit
    | '1'
    ;

tupleterm : '<' (msetterm)+ '>';

termNoPub : tupleterm
    | '(' msetterm ')'
    | identifier '(' (tupleterm | (msetterm)+) ')'
    | identifier '{' tupleterm '}' term
    | llitNoPub
    ;

natural : digit+;

digit : '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9';

ALPH : ('a'..'z' | 'A'..'Z');

ALPHA : 'A'..'Z';

alphaNum : (ALPH | digit);


//formalComment : identifier '{*' identifier* '*}';

//
// Whitespace and comments
//

WS: ( '\t' | ' ' | '\r' | '\n' | '\u000C' )+    -> skip ;

COMMA : ',' -> skip;

COMMENT
    : '/*' .*? '*/' -> skip
;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
;
