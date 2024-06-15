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


    # Visit a parse tree produced by lambdaParser#typeTerm.
    def visitTypeTerm(self, ctx:lambdaParser.TypeTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#nothing.
    def visitNothing(self, ctx:lambdaParser.NothingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#type.
    def visitType(self, ctx:lambdaParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#typeFunction.
    def visitTypeFunction(self, ctx:lambdaParser.TypeFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#typeValue.
    def visitTypeValue(self, ctx:lambdaParser.TypeValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#op.
    def visitOp(self, ctx:lambdaParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#application.
    def visitApplication(self, ctx:lambdaParser.ApplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#termParenthesis.
    def visitTermParenthesis(self, ctx:lambdaParser.TermParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#abstraction.
    def visitAbstraction(self, ctx:lambdaParser.AbstractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#num.
    def visitNum(self, ctx:lambdaParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#id.
    def visitId(self, ctx:lambdaParser.IdContext):
        return self.visitChildren(ctx)



del lambdaParser