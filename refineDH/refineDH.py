# Generated from Tamarinrule.g4 by ANTLR 4.7.2
from antlr4 import *
from .TamarinruleParser import TamarinruleParser

# This class defines a complete generic visitor for a parse tree produced by TamarinruleParser.

class TamarinruleVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TamarinruleParser#rules.
    def visitRules(self, ctx:TamarinruleParser.RulesContext):
        ctx.parser.substitutions = dict()
        self.visitChildren(ctx)
        return ctx.getText()

    # Visit a parse tree produced by TamarinruleParser#protoRule.
    def visitProtoRule(self, ctx:TamarinruleParser.ProtoRuleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TamarinruleParser#letBlock.
    def visitLetBlock(self, ctx:TamarinruleParser.LetBlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TamarinruleParser#definition.
    def visitDefinition(self, ctx:TamarinruleParser.DefinitionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TamarinruleParser#genericRule.
    def visitGenericRule(self, ctx:TamarinruleParser.GenericRuleContext):
        self.currentRule = ctx.getSourceInterval()
        ctx.parser.substitutions[self.currentRule] = set()
        #TODO Needs to be unique rule identifier
        r = self.visitChildren(ctx)
        self.currentRule = None
        #print(ctx.parser.substitutions)
        #TODO Have GetText use this?
        return r


    # Visit a parse tree produced by TamarinruleParser#fact.
    def visitFact(self, ctx:TamarinruleParser.FactContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TamarinruleParser#factList.
    def visitFactList(self, ctx:TamarinruleParser.FactListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TamarinruleParser#term.
    def visitTerm(self, ctx:TamarinruleParser.TermContext):
        def extractTerms(c):
            c = c.getChild(0)
            assert(c.getChild(0).getText()=='element')
            advVar = c.getChild(2).getChild(2)
            base = c.getChild(2).getChild(4)
            return advVar,base

        def extractExponent(c):
            return c.getChild(2)

        def isElementExpSite(c):
            if c.getChildCount() <= 1:
                return False 
            if c.getChild(1).getText() != '^':
                return False
            if c.getChild(0).getChild(0).getText() != 'element':
                return False
            return True 

        def clean(t):
            replacements = {
                '~' : "sF",
                "$" : "sP",
                "'" : "sP",
                "(" : "sLB",
                ")" : "sRB"
            }
            for (k,v) in replacements.items():
                t = t.replace(k,v)
            return t

        def isTermAtomic(c):
            print(c.getText())
            #print(dir(c))
            if c.Identifier() is not None and c.termList is not None:
                print("Overrode!")
                return True
            return c.getChild(0).getText()[0] in ["'","~","$"]

        def getNewAdvVar(av,e):
            return clean(av.getText() + '_' + e.getText())

        def getNewBase(b,e):
            return clean(b.getText() + '_' + e.getText())


        if isElementExpSite(ctx):

            k = ctx.getSourceInterval()
            if k not in ctx.parser.substitutions.keys():
                ctx.parser.substitutions[k] = ""
            # We are the base. Child 0 = Base. Child 2 = Exponent.
            advVar,base = extractTerms(ctx)
            exp = extractExponent(ctx)
            if isTermAtomic(exp):
                NadvVar = getNewAdvVar(advVar,exp)
                Nbase = base.getText() + '^'+exp.getText()
                ctx.parser.substitutions[self.currentRule].add(
                    ('G',
                    advVar.getText(),
                    NadvVar,
                    exp.getText(),
                    Nbase))
                ctx.parser.substitutions[k] = "element('G',"+NadvVar+','+Nbase+')'
            else:
                #Move the exponent inside and rename the variables
                NadvVar = getNewAdvVar(advVar,exp)
                Nbase = getNewBase(base,exp)
                ctx.parser.substitutions[k] = "element('G',"+NadvVar+','+Nbase+')'
        else:
            # Don't descent if we did a substitution here. 
            return self.visitChildren(ctx)

    # Visit a parse tree produced by TamarinruleParser#termList.
    def visitTermList(self, ctx:TamarinruleParser.TermListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TamarinruleParser#factIdentifier.
    def visitFactIdentifier(self, ctx:TamarinruleParser.FactIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TamarinruleParser#varIdentifier.
    def visitVarIdentifier(self, ctx:TamarinruleParser.VarIdentifierContext):
        return self.visitChildren(ctx)



del TamarinruleParser