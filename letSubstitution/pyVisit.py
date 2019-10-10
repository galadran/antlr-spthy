#! /usr/bin/python3

import sys
from antlr4 import *


def makeTree(input_stream):
	lexer = TamarinruleLexer(input_stream)
	stream = CommonTokenStream(lexer)
	parser = TamarinruleParser(stream)
	tree = parser.rules()
	return tree 

def run(stream):
	t = makeTree(stream)
	v = TamarinruleVisitor()
	return v.visit(t)

if __name__ == '__main__':
	from TamarinruleLexer import TamarinruleLexer
	from TamarinruleParser import TamarinruleParser
	from letSubstitution import TamarinruleVisitor
	import substitutionParser
	f = FileStream(sys.argv[1])
	r1 = run(f)


	i = InputStream(r1)
	r2 = run(i)

	assert(r1 == r2)
	print(r1)
else:
	from .TamarinruleLexer import TamarinruleLexer
	from .TamarinruleParser import TamarinruleParser
	from .letSubstitution import TamarinruleVisitor
	import substitutionParser