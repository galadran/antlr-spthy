#! /usr/bin/python3

import sys
from antlr4 import *
from .TamarinruleLexer import TamarinruleLexer
from .TamarinruleParser import TamarinruleParser
from .letSubstitution import TamarinruleVisitor

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
	f = FileStream(sys.argv[1])
	r1 = run(f)
	print(r1)

	i = InputStream(r1)
	r2 = run(i)
	assert(r1 == r2)

	print(r1)