# Generated from Tamarinrule.g4 by ANTLR 4.7.2
from antlr4 import *
from TamarinruleParser import TamarinruleParser

# This class defines a complete generic visitor for a parse tree produced by TamarinruleParser.

class TamarinruleVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TamarinruleParser#rules.
    def visitRules(self, ctx:TamarinruleParser.RulesContext):
        r = self.visitChildren(ctx)
        return ctx.getText()

    # Visit a parse tree produced by TamarinruleParser#protoRule.
    def visitProtoRule(self, ctx:TamarinruleParser.ProtoRuleContext):
        self.substitutions = dict()
        self.rule = ctx.genericRule().getText()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TamarinruleParser#letBlock.
    def visitLetBlock(self, ctx:TamarinruleParser.LetBlockContext):
        r = self.visitChildren(ctx)
        ctx.children =[]
        return r

    # Visit a parse tree produced by TamarinruleParser#definition.
    def visitDefinition(self, ctx:TamarinruleParser.DefinitionContext):
        self.substitutions[ctx.getChild(0).getText()] = ctx.getChild(2)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TamarinruleParser#genericRule.
    def visitGenericRule(self, ctx:TamarinruleParser.GenericRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TamarinruleParser#fact.
    def visitFact(self, ctx:TamarinruleParser.FactContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TamarinruleParser#factList.
    def visitFactList(self, ctx:TamarinruleParser.FactListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TamarinruleParser#term.
    def visitTerm(self, ctx:TamarinruleParser.TermContext):
        newList = []
        for c in ctx.children:
            if c.getText() in self.substitutions.keys():
                newList.append(self.substitutions[c.getText()])
            else:
                newList.append(c)
        ctx.children = newList
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