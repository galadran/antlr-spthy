#! /usr/bin/python3

import sys
from antlr4 import *
from refineDH.pyVisit import run as refineExp
from makeDH.pyVisit import run as baseExp
from letSubstitution.pyVisit import run as letSub

def convert(stream):
	subbed = letSub(stream)
	based = baseExp(InputStream(subbed))
	refined = refineExp(InputStream(based))
	return refined 

if __name__ == '__main__':
	raw = FileStream(sys.argv[1])
	print(convert(raw))
