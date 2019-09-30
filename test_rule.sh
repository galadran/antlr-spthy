# wget https://www.antlr.org/download/antlr-4.7.2-complete.jar

rm -r out
echo "Compiling..."
java -jar antlr-4.7.2-complete.jar -o out Tamarinrule.g4
find . -type f -name "*.java" -print | xargs javac -cp antlr-4.7.2-complete.jar
echo "Finished Compiling"
echo "Testing Var Parsing"
java -cp antlr-4.7.2-complete.jar:out/ org.antlr.v4.gui.TestRig Tamarinrule term -tree var.txt 
echo "Testing Fact Parsing"
java -cp antlr-4.7.2-complete.jar:out/ org.antlr.v4.gui.TestRig Tamarinrule fact -tree fact.txt 
echo "Testing Generic Rule Parsing"
java -cp antlr-4.7.2-complete.jar:out/ org.antlr.v4.gui.TestRig Tamarinrule genericRule -tree genericRule.txt 
echo "Testing Full Rule Parsing"
java -cp antlr-4.7.2-complete.jar:out/ org.antlr.v4.gui.TestRig Tamarinrule rules -gui rules.txt 
