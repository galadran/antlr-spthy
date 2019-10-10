# Generated from Tamarinrule.g4 by ANTLR 4.7.2
# encoding: utf-8
import TamarinruleParser
from io import StringIO

def protoOverride(self):
    if self.getChildCount() == 0:
        return ""
    with StringIO() as builder:
        builder.write("\n")
        for child in self.getChildren():
            builder.write(child.getText())
            if ':' in child.getText():
                builder.write("\n")
            if child.getText() == 'rule':
                builder.write(" ")
        return builder.getvalue()

TamarinruleParser.TamarinruleParser.ProtoRuleContext.getText = protoOverride

def genericOverride(self):
    if self.getChildCount() == 0:
        return ""
    with StringIO() as builder:
        for child in self.getChildren():
            builder.write(child.getText())
        builder.write("\n")
        return builder.getvalue()

TamarinruleParser.TamarinruleParser.GenericRuleContext.getText = genericOverride