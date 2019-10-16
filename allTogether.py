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
	rulesT = """
	functions: element/3, extract_element/1
	equations: extract_element(element(t,s,n)) = n
	""" + str(rulesT)
	if "Raised(" in rulesT:
		rulesT = rulesT + """
		restriction Consistency:
		        "All  t s r1 r2 y #i #j .
		        Raised(t,s,r1,y) @ i & Raised(t,s,r2,y) @j
		        ==> r1 = r2"

		restriction Identity:
		        "All  t r y #i .
		        Raised(t,grpid,r,y) @ i ==> r = grpid"

		"""
	newpt = pt.replace('\n RULESUBHERE \n',str(rulesT))
	return newpt

if __name__=='__main__':
	s = open(sys.argv[1],'r').read()
	print(transformSpthy(s))
