antlr4 -o out -Dlanguage=Python3 Tamarinrule.g4 -no-listener -visitor
cp out/TamarinruleParser.py out/TamarinruleLexer.py letSubstitution/
cp out/TamarinruleParser.py out/TamarinruleLexer.py makeDH/
cp out/TamarinruleParser.py out/TamarinruleLexer.py refineDH/