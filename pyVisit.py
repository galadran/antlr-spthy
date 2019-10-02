#! /usr/bin/python3

import sys
from antlr4 import *
from out.TamarinruleLexer import TamarinruleLexer
from out.TamarinruleParser import TamarinruleParser
from letSubstitution import TamarinruleVisitor
from letSubListener import TamarinruleListener

def main(argv):
	input_stream = FileStream(argv[1])
	lexer = TamarinruleLexer(input_stream)
	stream = CommonTokenStream(lexer)
	parser = TamarinruleParser(stream)
	tree = parser.rules()
	return tree 

if __name__ == '__main__':
	t = main(sys.argv)
	v = TamarinruleVisitor()
	r = v.visit(t)
	print(r)
	#l = TamarinruleListener()
	#walker = ParseTreeWalker()
	#walker.walk(l, t)