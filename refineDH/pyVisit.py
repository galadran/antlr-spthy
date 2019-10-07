#! /usr/bin/python3

import sys
from antlr4 import *
from TamarinruleLexer import TamarinruleLexer
from TamarinruleParser import TamarinruleParser
from makeDH import TamarinruleVisitor

def makeTree(input_stream):
	lexer = TamarinruleLexer(input_stream)
	stream = CommonTokenStream(lexer)
	parser = TamarinruleParser(stream)
	tree = parser.rules()
	return tree 

def makeTransform(f):
	t = makeTree(f)
	v = TamarinruleVisitor()
	r1 = v.visit(t)
	return r1

if __name__ == '__main__':
	old = ''
	new = makeTransform(FileStream(sys.argv[1]))
	while old != new:
		print(new)
		input()
		old = new 
		new = makeTransform(InputStream(old))
