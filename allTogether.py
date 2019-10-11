from convert import convert
from convertWhole import extractRules
from antlr4 import InputStream
import sys
from traceback import print_exc

def transformSpthy(s):
	(pt,rules) = extractRules(s)
	try:
		rulesT = convert(InputStream(rules))
	except Exception as E:
		#print(rules)

		print('---')
		print_exc()
		exit(-1)
	rulesT = 'functions: element/3, grpid/0\n' + str(rulesT)
	newpt = pt.replace('\n RULESUBHERE \n',str(rulesT))
	return newpt

if __name__=='__main__':
	s = open(sys.argv[1],'r').read()
	print(transformSpthy(s))
