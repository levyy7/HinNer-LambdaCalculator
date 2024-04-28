# Generated from ./src/grammar/lambda.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,61,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,3,0,17,8,0,1,1,1,1,1,1,1,1,1,1,3,1,24,8,1,1,2,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,42,8,3,1,
        3,1,3,5,3,46,8,3,10,3,12,3,49,9,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,
        6,3,6,59,8,6,1,6,0,1,6,7,0,2,4,6,8,10,12,0,0,63,0,16,1,0,0,0,2,23,
        1,0,0,0,4,25,1,0,0,0,6,41,1,0,0,0,8,50,1,0,0,0,10,52,1,0,0,0,12,
        58,1,0,0,0,14,17,3,2,1,0,15,17,5,0,0,1,16,14,1,0,0,0,16,15,1,0,0,
        0,17,1,1,0,0,0,18,24,3,4,2,0,19,24,3,6,3,0,20,24,3,8,4,0,21,24,3,
        10,5,0,22,24,3,12,6,0,23,18,1,0,0,0,23,19,1,0,0,0,23,20,1,0,0,0,
        23,21,1,0,0,0,23,22,1,0,0,0,24,3,1,0,0,0,25,26,5,1,0,0,26,27,3,8,
        4,0,27,28,5,2,0,0,28,29,3,2,1,0,29,5,1,0,0,0,30,31,6,3,-1,0,31,32,
        5,3,0,0,32,33,3,4,2,0,33,34,5,4,0,0,34,35,3,2,1,0,35,42,1,0,0,0,
        36,37,5,3,0,0,37,38,3,12,6,0,38,39,5,4,0,0,39,40,3,2,1,0,40,42,1,
        0,0,0,41,30,1,0,0,0,41,36,1,0,0,0,42,47,1,0,0,0,43,44,10,3,0,0,44,
        46,3,2,1,0,45,43,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,
        0,48,7,1,0,0,0,49,47,1,0,0,0,50,51,5,11,0,0,51,9,1,0,0,0,52,53,5,
        10,0,0,53,11,1,0,0,0,54,59,5,5,0,0,55,59,5,6,0,0,56,59,5,7,0,0,57,
        59,5,8,0,0,58,54,1,0,0,0,58,55,1,0,0,0,58,56,1,0,0,0,58,57,1,0,0,
        0,59,13,1,0,0,0,5,16,23,41,47,58
    ]

class lambdaParser ( Parser ):

    grammarFileName = "lambda.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\'", "'->'", "'('", "')'", "'+'", "'-'", 
                     "'*'", "'/'", "'^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "SUM", "SUB", "MUL", "DIV", "POW", "NUM", 
                      "ID", "WS" ]

    RULE_root = 0
    RULE_term = 1
    RULE_abstraction = 2
    RULE_application = 3
    RULE_var = 4
    RULE_atom = 5
    RULE_op = 6

    ruleNames =  [ "root", "term", "abstraction", "application", "var", 
                   "atom", "op" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    SUM=5
    SUB=6
    MUL=7
    DIV=8
    POW=9
    NUM=10
    ID=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lambdaParser.RULE_root

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RegTermContext(RootContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.RootContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(lambdaParser.TermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegTerm" ):
                return visitor.visitRegTerm(self)
            else:
                return visitor.visitChildren(self)


    class NothingContext(RootContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.RootContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EOF(self):
            return self.getToken(lambdaParser.EOF, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNothing" ):
                return visitor.visitNothing(self)
            else:
                return visitor.visitChildren(self)



    def root(self):

        localctx = lambdaParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.state = 16
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 5, 6, 7, 8, 10, 11]:
                localctx = lambdaParser.RegTermContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.term()
                pass
            elif token in [-1]:
                localctx = lambdaParser.NothingContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.match(lambdaParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def abstraction(self):
            return self.getTypedRuleContext(lambdaParser.AbstractionContext,0)


        def application(self):
            return self.getTypedRuleContext(lambdaParser.ApplicationContext,0)


        def var(self):
            return self.getTypedRuleContext(lambdaParser.VarContext,0)


        def atom(self):
            return self.getTypedRuleContext(lambdaParser.AtomContext,0)


        def op(self):
            return self.getTypedRuleContext(lambdaParser.OpContext,0)


        def getRuleIndex(self):
            return lambdaParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = lambdaParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_term)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.abstraction()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.application(0)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 20
                self.var()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 21
                self.atom()
                pass
            elif token in [5, 6, 7, 8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 22
                self.op()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AbstractionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # VarContext
            self.right = None # TermContext

        def var(self):
            return self.getTypedRuleContext(lambdaParser.VarContext,0)


        def term(self):
            return self.getTypedRuleContext(lambdaParser.TermContext,0)


        def getRuleIndex(self):
            return lambdaParser.RULE_abstraction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstraction" ):
                return visitor.visitAbstraction(self)
            else:
                return visitor.visitChildren(self)




    def abstraction(self):

        localctx = lambdaParser.AbstractionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_abstraction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(lambdaParser.T__0)
            self.state = 26
            localctx.left = self.var()
            self.state = 27
            self.match(lambdaParser.T__1)
            self.state = 28
            localctx.right = self.term()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ApplicationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lambdaParser.RULE_application

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class OpAppContext(ApplicationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.ApplicationContext
            super().__init__(parser)
            self.left = None # OpContext
            self.right = None # TermContext
            self.copyFrom(ctx)

        def op(self):
            return self.getTypedRuleContext(lambdaParser.OpContext,0)

        def term(self):
            return self.getTypedRuleContext(lambdaParser.TermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpApp" ):
                return visitor.visitOpApp(self)
            else:
                return visitor.visitChildren(self)


    class ExtAppContext(ApplicationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.ApplicationContext
            super().__init__(parser)
            self.left = None # ApplicationContext
            self.right = None # TermContext
            self.copyFrom(ctx)

        def application(self):
            return self.getTypedRuleContext(lambdaParser.ApplicationContext,0)

        def term(self):
            return self.getTypedRuleContext(lambdaParser.TermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtApp" ):
                return visitor.visitExtApp(self)
            else:
                return visitor.visitChildren(self)


    class AbsAppContext(ApplicationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.ApplicationContext
            super().__init__(parser)
            self.left = None # AbstractionContext
            self.right = None # TermContext
            self.copyFrom(ctx)

        def abstraction(self):
            return self.getTypedRuleContext(lambdaParser.AbstractionContext,0)

        def term(self):
            return self.getTypedRuleContext(lambdaParser.TermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbsApp" ):
                return visitor.visitAbsApp(self)
            else:
                return visitor.visitChildren(self)



    def application(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = lambdaParser.ApplicationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_application, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = lambdaParser.AbsAppContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 31
                self.match(lambdaParser.T__2)
                self.state = 32
                localctx.left = self.abstraction()
                self.state = 33
                self.match(lambdaParser.T__3)
                self.state = 34
                localctx.right = self.term()
                pass

            elif la_ == 2:
                localctx = lambdaParser.OpAppContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 36
                self.match(lambdaParser.T__2)
                self.state = 37
                localctx.left = self.op()
                self.state = 38
                self.match(lambdaParser.T__3)
                self.state = 39
                localctx.right = self.term()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 47
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = lambdaParser.ExtAppContext(self, lambdaParser.ApplicationContext(self, _parentctx, _parentState))
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_application)
                    self.state = 43
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 44
                    localctx.right = self.term() 
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(lambdaParser.ID, 0)

        def getRuleIndex(self):
            return lambdaParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = lambdaParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(lambdaParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(lambdaParser.NUM, 0)

        def getRuleIndex(self):
            return lambdaParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = lambdaParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(lambdaParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lambdaParser.RULE_op

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DivOpContext(OpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.OpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DIV(self):
            return self.getToken(lambdaParser.DIV, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivOp" ):
                return visitor.visitDivOp(self)
            else:
                return visitor.visitChildren(self)


    class MulOpContext(OpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.OpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MUL(self):
            return self.getToken(lambdaParser.MUL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulOp" ):
                return visitor.visitMulOp(self)
            else:
                return visitor.visitChildren(self)


    class SumOpContext(OpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.OpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUM(self):
            return self.getToken(lambdaParser.SUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumOp" ):
                return visitor.visitSumOp(self)
            else:
                return visitor.visitChildren(self)


    class SubOpContext(OpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.OpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(lambdaParser.SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubOp" ):
                return visitor.visitSubOp(self)
            else:
                return visitor.visitChildren(self)



    def op(self):

        localctx = lambdaParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_op)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = lambdaParser.SumOpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(lambdaParser.SUM)
                pass
            elif token in [6]:
                localctx = lambdaParser.SubOpContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(lambdaParser.SUB)
                pass
            elif token in [7]:
                localctx = lambdaParser.MulOpContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.match(lambdaParser.MUL)
                pass
            elif token in [8]:
                localctx = lambdaParser.DivOpContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.match(lambdaParser.DIV)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.application_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def application_sempred(self, localctx:ApplicationContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




