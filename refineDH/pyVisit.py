#! /usr/bin/python3

import sys
from antlr4 import *

def makeTree(input_stream):
	lexer = TamarinruleLexer(input_stream)
	stream = CommonTokenStream(lexer)
	from . import refineDHParser
	parser = TamarinruleParser(stream)
	tree = parser.rules()
	return tree 

def makeTransform(f):
	t = makeTree(f)
	v = TamarinruleVisitor()
	r1 = v.visit(t)
	return r1

def run(stream):
	old = ''
	new = stream
	i = 0 
	#print(new)
	while str(old) != str(new):
		old = new
		new = InputStream(makeTransform(old))
		#print('#####')
		#print(new)
		#print('######')
		i += 1 
		if i > 10:
			print("Error, loop limit reached whilst converting")
			exit(-1)
	return new

if __name__ == '__main__':
	from TamarinruleLexer import TamarinruleLexer
	from TamarinruleParser import TamarinruleParser
	from refineDH import TamarinruleVisitor
	print(run(FileStream(sys.argv[1])))
else:
	from .TamarinruleLexer import TamarinruleLexer
	from .TamarinruleParser import TamarinruleParser
	from .refineDH import TamarinruleVisitor