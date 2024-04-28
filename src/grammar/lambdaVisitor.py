# Generated from ./src/grammar/lambda.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .lambdaParser import lambdaParser
else:
    from lambdaParser import lambdaParser

# This class defines a complete generic visitor for a parse tree produced by lambdaParser.

class lambdaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lambdaParser#regTerm.
    def visitRegTerm(self, ctx:lambdaParser.RegTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#nothing.
    def visitNothing(self, ctx:lambdaParser.NothingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#term.
    def visitTerm(self, ctx:lambdaParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#abstraction.
    def visitAbstraction(self, ctx:lambdaParser.AbstractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#opApp.
    def visitOpApp(self, ctx:lambdaParser.OpAppContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#extApp.
    def visitExtApp(self, ctx:lambdaParser.ExtAppContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#absApp.
    def visitAbsApp(self, ctx:lambdaParser.AbsAppContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#var.
    def visitVar(self, ctx:lambdaParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#atom.
    def visitAtom(self, ctx:lambdaParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#sumOp.
    def visitSumOp(self, ctx:lambdaParser.SumOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#subOp.
    def visitSubOp(self, ctx:lambdaParser.SubOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#mulOp.
    def visitMulOp(self, ctx:lambdaParser.MulOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#divOp.
    def visitDivOp(self, ctx:lambdaParser.DivOpContext):
        return self.visitChildren(ctx)



del lambdaParser