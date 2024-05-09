from antlr4 import *
from grammar.lambdaParser import lambdaParser

from grammar.lambdaVisitor import lambdaVisitor
from visitor.SemanticTree import *


class LambdaVisitorExpanded(lambdaVisitor):
    # Visit a parse tree produced by lambdaParser#regTerm.
    def visitRegTerm(self, ctx:lambdaParser.RegTermContext):
        [term] = ctx.getChildren()
        return SemanticTree(self.visit(term))



    # TYPE VISITORS

    # Visit a parse tree produced by lambdaParser#typeTerm.
    def visitTypeTerm(self, ctx:lambdaParser.TypeTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#literalType.
    def visitLiteralType(self, ctx:lambdaParser.LiteralTypeContext):
        symbol = ctx.NUM().getText()
        tipus = ctx.CAPS().getText()
        print(symbol)
        print(tipus)
        return {symbol : tipus}


    # Visit a parse tree produced by lambdaParser#functionType.
    def visitFunctionType(self, ctx:lambdaParser.FunctionTypeContext):
        symbol = ctx.left.getText()
        tipus1 = ctx.right1.getText()
        tipus2 = ctx.right2.getText()
        tipus3 = ctx.right3.getText()
        
        return {symbol : [tipus1, tipus2, tipus3]}




    # Visit a parse tree produced by lambdaParser#nothing.
    def visitNothing(self, ctx:lambdaParser.NothingContext):
        return SemanticTree(None)


    # Visit a parse tree produced by lambdaParser#term.
    def visitTerm(self, ctx:lambdaParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lambdaParser#abstraction.
    def visitAbstraction(self, ctx:lambdaParser.AbstractionContext):
        inp = ctx.left
        out = ctx.right

        return Abstraction(self.visit(inp), self.visit(out))


    # Visit a parse tree produced by lambdaParser#opApp.
    def visitOpApp(self, ctx:lambdaParser.OpAppContext):
        func = ctx.left
        arg = ctx.right

        return Application(self.visit(func), self.visit(arg))


    # Visit a parse tree produced by lambdaParser#extApp.
    def visitExtApp(self, ctx:lambdaParser.ExtAppContext):
        func = ctx.left
        arg = ctx.right

        return Application(self.visit(func), self.visit(arg))


    # Visit a parse tree produced by lambdaParser#absApp.
    def visitAbsApp(self, ctx:lambdaParser.AbsAppContext):
        func = ctx.left
        arg = ctx.right

        return Application(self.visit(func), self.visit(arg))


    # Visit a parse tree produced by lambdaParser#var.
    def visitVar(self, ctx:lambdaParser.VarContext):
        id = ctx.ID().getText()
        print(id)
        return Variable(id)


    # Visit a parse tree produced by lambdaParser#atom.
    def visitAtom(self, ctx:lambdaParser.AtomContext):
        value = int(ctx.NUM().getText())
        print(value)
        return Terminal(value)


    # Visit a parse tree produced by lambdaParser#sumOp.
    def visitSumOp(self, ctx:lambdaParser.SumOpContext):
        return Operator(ArithmeticOP('+'))


    # Visit a parse tree produced by lambdaParser#subOp.
    def visitSubOp(self, ctx:lambdaParser.SubOpContext):
        return Operator(ArithmeticOP('-'))


    # Visit a parse tree produced by lambdaParser#mulOp.
    def visitMulOp(self, ctx:lambdaParser.MulOpContext):
        return Operator(ArithmeticOP('*'))


    # Visit a parse tree produced by lambdaParser#divOp.
    def visitDivOp(self, ctx:lambdaParser.DivOpContext):
        return Operator(ArithmeticOP('/'))
        
   
    # Visit a parse tree produced by lambdaParser#pterm.
    #def visitPterm(self, ctx:lambdaParser.PtermContext):
    #    return self.visitChildren(ctx)

        
