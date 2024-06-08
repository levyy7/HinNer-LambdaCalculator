from antlr4 import *
from grammar.lambdaParser import lambdaParser

from grammar.lambdaVisitor import lambdaVisitor
from visitor.SemanticTree import *


class LambdaVisitorExpanded(lambdaVisitor):

    # ROOT

    # Visit a parse tree produced by lambdaParser#regTerm.
    def visitRegTerm(self, ctx: lambdaParser.RegTermContext):
        [term, _] = ctx.getChildren()
        return SemanticTree(self.visit(term))

    # Visit a parse tree produced by lambdaParser#typeTerm.
    def visitTypeTerm(self, ctx: lambdaParser.TypeTermContext):
        [term, _] = ctx.getChildren()
        return self.visit(term)

    # Visit a parse tree produced by lambdaParser#nothing.
    def visitNothing(self, ctx: lambdaParser.NothingContext):
        return SemanticTree(None)

    # TYPE

    # Visit a parse tree produced by lambdaParser#type.

    def visitType(self, ctx: lambdaParser.TypeContext):
        symbol = ctx.left.text
        tipos = [self.visit(tipo) for tipo in ctx.typeRec()]
        return {symbol: tipos}

    # Visit a parse tree produced by lambdaParser#typeFunction.
    def visitTypeFunction(self, ctx: lambdaParser.TypeFunctionContext):
        return [self.visit(tipo) for tipo in ctx.typeRec()]

    # Visit a parse tree produced by lambdaParser#typeValue.
    def visitTypeValue(self, ctx: lambdaParser.TypeValueContext):
        return ctx.CAPS().getText()

    # TERM

    # Visit a parse tree produced by lambdaParser#termParenthesis.

    def visitTermParenthesis(self, ctx: lambdaParser.TermParenthesisContext):
        [_, term, _] = ctx.getChildren()
        return self.visit(term)

    # Visit a parse tree produced by lambdaParser#abstraction.
    def visitAbstraction(self, ctx: lambdaParser.AbstractionContext):
        inp = Variable(ctx.ID().getText())
        out = ctx.right

        return Abstraction(inp, self.visit(out))

    # Visit a parse tree produced by lambdaParser#application.
    def visitApplication(self, ctx: lambdaParser.ApplicationContext):
        [term1, term2] = ctx.getChildren()
        return Application(self.visit(term1), self.visit(term2))

    # Visit a parse tree produced by lambdaParser#op.
    def visitOp(self, ctx: lambdaParser.OpContext):
        op = ctx.OP().getText()
        # print(id)
        return Variable(op)

    # Visit a parse tree produced by lambdaParser#num.
    def visitNum(self, ctx: lambdaParser.NumContext):
        num = ctx.NUM().getText()
        # print(id)
        return Variable(num)

    # Visit a parse tree produced by lambdaParser#id.
    def visitId(self, ctx: lambdaParser.IdContext):
        iden = ctx.ID().getText()
        # print(id)
        return Variable(iden)
