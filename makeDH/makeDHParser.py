from .TamarinruleParser import TamarinruleParser
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

TamarinruleParser.ProtoRuleContext.getText = protoOverride

def genericOverride(self):
    if self.getChildCount() == 0:
        return ""
    with StringIO() as builder:
        for child in self.getChildren():
            builder.write(child.getText())
        builder.write("\n")
        return builder.getvalue()

TamarinruleParser.GenericRuleContext.getText = genericOverride

def termOverride(self,transform=True):
    if not transform:
        with StringIO() as builder:
            for child in self.getChildren():
                if type(child) == type(self):
                    builder.write(child.getText(transform=False))
                else:
                    builder.write(child.getText())
            return builder.getvalue()
    if transform:
        if 'subs' not in dir(self.parser):
            self.parser.subs = dict()
        from .transformElements import transformTerm
        o = self.getText(transform=False)
        r = transformTerm(self)
        if 'element' in r :
            pass
            #print(o + ' -> ' + r)
            #self.parser.subs[o] = r
        else:
            assert(o == r)
            if o in self.parser.subs.keys():
                #print("Using cache")
                r = self.parser.subs[o]
                #print(o + ' --> ' + r)
        return r

TamarinruleParser.TermContext.getText = termOverride


