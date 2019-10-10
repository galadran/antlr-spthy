from convert import convert
from convertWhole import extractRules
from antlr4 import InputStream
import sys

s = open(sys.argv[1],'r').read()
(pt,rules) = extractRules(s)
rulesT = convert(InputStream(rules))

newpt = pt.replace('\n RULESUBHERE \n',str(rulesT))

print(newpt)
