# wget https://www.antlr.org/download/antlr-4.7.2-complete.jar

rm -r out
java -jar antlr-4.7.2-complete.jar -o out Tamarin.g4
find . -type f -name "*.java" -print | xargs javac -cp antlr-4.7.2-complete.jar
java -cp antlr-4.7.2-complete.jar:out/ org.antlr.v4.gui.TestRig Tamarin theory -gui tendermint_subgroups.spthy 
