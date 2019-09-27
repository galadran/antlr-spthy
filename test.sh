
rm -r out
/opt/antlr -o out Tamarin.g4
cd out
javac Tamarin*.java
java org.antlr.v4.gui.TestRig Tamarin theory -gui ../tendermint_subgroups.spthy     
