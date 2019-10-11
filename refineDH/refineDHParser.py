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

def termOverride(self,transform=True):
            if self.getSourceInterval() in self.parser.substitutions.keys():
                return self.parser.substitutions[self.getSourceInterval()]
            if self.getChildCount() == 0:
                return ""
            with StringIO() as builder:
                for child in self.getChildren():
                    builder.write(child.getText())
                return builder.getvalue()

TamarinruleParser.TermContext.getText = termOverride

def genericOverride(self):
    def amendList(state,prev,subs):
        def getIn(s):
            return 'In('+s[2]+')'

        def getAction(s):
            return "raised('G'," + s[1]+','+s[2]+','+ s[3]+ ')'

        r = ''
        if state is None:
            #Append Premise
            for s in subs:
                r += ','
                r += getIn(s)
            state = 'P'
        elif state == 'P':
            #Append Action
            for s in subs:
                r += ','
                r += getAction(s)
            state = 'A'
        if r == ',':
            r = ''
        return state,r
            
    if self.getSourceInterval() in self.parser.substitutions.keys():
        subs = self.parser.substitutions[self.getSourceInterval()]
        if self.getChildCount() == 0:
            return ""
        with StringIO() as builder:
            prev = None 
            state = None
            flip = False
            #TODO This might be buggy when certain fact lists are missing.
            for child in self.getChildren():
                if ']' in child.getText():
                    state, r = amendList(state,prev,subs)
                    builder.write(r)
                o = child.getText()
                if flip:
                    o = ']->' + o 
                    flip = False
                if '-->' in o:
                    o = '--['
                    flip = True 
                prev = child 
                builder.write(o)
            builder.write("\n")
            return builder.getvalue().replace("[,","[")   
    else:
        if self.getChildCount() == 0:
            return ""
        with StringIO() as builder:
            for child in self.getChildren():
                builder.write(child.getText())
            builder.write("\n")
            return builder.getvalue()  

TamarinruleParser.GenericRuleContext.getText = genericOverride
