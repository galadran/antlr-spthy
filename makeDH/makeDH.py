# Generated from Tamarinrule.g4 by ANTLR 4.7.2
from antlr4 import *
from TamarinruleParser import TamarinruleParser

# This class defines a complete generic visitor for a parse tree produced by TamarinruleParser.

class TamarinruleVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TamarinruleParser#rules.
    def visitRules(self, ctx:TamarinruleParser.RulesContext):
        self.substitutions = dict()
        r = self.visitChildren(ctx)
        for k,v in self.substitutions.items():
            print(k.getText() + " " + v)
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TamarinruleParser#fact.
    def visitFact(self, ctx:TamarinruleParser.FactContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TamarinruleParser#factList.
    def visitFactList(self, ctx:TamarinruleParser.FactListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TamarinruleParser#term.
    def visitTerm(self, ctx:TamarinruleParser.TermContext):
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