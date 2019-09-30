#! /usr/bin/python3

import sys
from antlr4 import *
from out.TamarinruleLexer import TamarinruleLexer
from out.TamarinruleParser import TamarinruleParser
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = TamarinruleLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = TamarinruleParser(stream)
    tree = parser.rules()
 
if __name__ == '__main__':
    main(sys.argv)