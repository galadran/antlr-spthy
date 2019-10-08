#! /usr/bin/python3

import sys
from antlr4 import *
from refineDH.pyVisit import run as refineExp
from makeDH.pyVisit import run as baseExp
from letSubstitution.pyVisit import run as letSub

raw = FileStream(sys.argv[1])
subbed = letSub(raw)
based = baseExp(InputStream(subbed))
refined = refineExp(InputStream(based))
print(refined)
