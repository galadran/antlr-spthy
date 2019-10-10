from convert import convert
from convertWhole import extractRules
from antlr4 import InputStream
import sys

def transformSpthy(s):
	(pt,rules) = extractRules(s)
	rulesT = convert(InputStream(rules))
	newpt = pt.replace('\n RULESUBHERE \n',str(rulesT))
	return newpt

if __name__=='__main__':
	s = open(sys.argv[1],'r').read()
	print(transformSpthy(s))
