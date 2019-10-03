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

if __name__ == '__main__':
	f = FileStream(sys.argv[1])
	t = makeTree(f)
	v = TamarinruleVisitor()
	r1 = v.visit(t)
	print(r1)