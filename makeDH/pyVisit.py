#! /usr/bin/python3

import sys
from antlr4 import *
from .TamarinruleLexer import TamarinruleLexer
from .TamarinruleParser import TamarinruleParser
from .makeDH import TamarinruleVisitor


def makeTree(input_stream):
	lexer = TamarinruleLexer(input_stream)
	stream = CommonTokenStream(lexer)
	from . import makeDHParser
	parser = TamarinruleParser(stream)
	tree = parser.rules()
	return tree 

def run(stream):
	t = makeTree(stream)
	v = TamarinruleVisitor()
	old = ''
	new = v.visit(t)
	i = 0
	while old != new and i < 10:
		old = new
		new = v.visit(t)
		#print(t.parser.subs)
		i+= 1
	if i >= 10:
		print("Loop limit reached in makeDH")
		exit(-1)
	return new
 
if __name__ == '__main__':
	f = FileStream(sys.argv[1])
	print(run(f))