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
        4,1,11,65,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,3,0,16,8,0,1,1,1,1,1,1,1,1,1,1,5,1,23,8,1,10,1,12,1,26,9,1,
        1,2,1,2,1,2,1,2,1,2,1,2,5,2,34,8,2,10,2,12,2,37,9,2,1,2,1,2,1,2,
        3,2,42,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,56,
        8,3,1,3,1,3,5,3,60,8,3,10,3,12,3,63,9,3,1,3,0,1,6,4,0,2,4,6,0,1,
        1,0,6,8,70,0,15,1,0,0,0,2,17,1,0,0,0,4,41,1,0,0,0,6,55,1,0,0,0,8,
        9,3,6,3,0,9,10,5,0,0,1,10,16,1,0,0,0,11,12,3,2,1,0,12,13,5,0,0,1,
        13,16,1,0,0,0,14,16,5,0,0,1,15,8,1,0,0,0,15,11,1,0,0,0,15,14,1,0,
        0,0,16,1,1,0,0,0,17,18,7,0,0,0,18,19,5,1,0,0,19,24,3,4,2,0,20,21,
        5,2,0,0,21,23,3,4,2,0,22,20,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,
        24,25,1,0,0,0,25,3,1,0,0,0,26,24,1,0,0,0,27,28,5,3,0,0,28,29,3,4,
        2,0,29,30,5,2,0,0,30,35,3,4,2,0,31,32,5,2,0,0,32,34,3,4,2,0,33,31,
        1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,38,1,0,0,0,
        37,35,1,0,0,0,38,39,5,4,0,0,39,42,1,0,0,0,40,42,5,9,0,0,41,27,1,
        0,0,0,41,40,1,0,0,0,42,5,1,0,0,0,43,44,6,3,-1,0,44,45,5,3,0,0,45,
        46,3,6,3,0,46,47,5,4,0,0,47,56,1,0,0,0,48,49,5,5,0,0,49,50,5,8,0,
        0,50,51,5,2,0,0,51,56,3,6,3,4,52,56,5,8,0,0,53,56,5,7,0,0,54,56,
        5,6,0,0,55,43,1,0,0,0,55,48,1,0,0,0,55,52,1,0,0,0,55,53,1,0,0,0,
        55,54,1,0,0,0,56,61,1,0,0,0,57,58,10,5,0,0,58,60,3,6,3,6,59,57,1,
        0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,7,1,0,0,0,63,
        61,1,0,0,0,6,15,24,35,41,55,61
    ]

class lambdaParser ( Parser ):

    grammarFileName = "lambda.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'::'", "'->'", "'('", "')'", "'\\'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "OP", "NUM", "ID", "CAPS", 
                      "WS", "LEXICAL_ERROR" ]

    RULE_root = 0
    RULE_type = 1
    RULE_typeRec = 2
    RULE_term = 3

    ruleNames =  [ "root", "type", "typeRec", "term" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    OP=6
    NUM=7
    ID=8
    CAPS=9
    WS=10
    LEXICAL_ERROR=11

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

        def EOF(self):
            return self.getToken(lambdaParser.EOF, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegTerm" ):
                return visitor.visitRegTerm(self)
            else:
                return visitor.visitChildren(self)


    class TypeTermContext(RootContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.RootContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(lambdaParser.TypeContext,0)

        def EOF(self):
            return self.getToken(lambdaParser.EOF, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeTerm" ):
                return visitor.visitTypeTerm(self)
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
            self.state = 15
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = lambdaParser.RegTermContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.term(0)
                self.state = 9
                self.match(lambdaParser.EOF)
                pass

            elif la_ == 2:
                localctx = lambdaParser.TypeTermContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.type_()
                self.state = 12
                self.match(lambdaParser.EOF)
                pass

            elif la_ == 3:
                localctx = lambdaParser.NothingContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 14
                self.match(lambdaParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Token

        def typeRec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lambdaParser.TypeRecContext)
            else:
                return self.getTypedRuleContext(lambdaParser.TypeRecContext,i)


        def OP(self):
            return self.getToken(lambdaParser.OP, 0)

        def NUM(self):
            return self.getToken(lambdaParser.NUM, 0)

        def ID(self):
            return self.getToken(lambdaParser.ID, 0)

        def getRuleIndex(self):
            return lambdaParser.RULE_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = lambdaParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            localctx.left = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0)):
                localctx.left = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 18
            self.match(lambdaParser.T__0)
            self.state = 19
            self.typeRec()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 20
                self.match(lambdaParser.T__1)
                self.state = 21
                self.typeRec()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeRecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return lambdaParser.RULE_typeRec

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TypeFunctionContext(TypeRecContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TypeRecContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def typeRec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lambdaParser.TypeRecContext)
            else:
                return self.getTypedRuleContext(lambdaParser.TypeRecContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeFunction" ):
                return visitor.visitTypeFunction(self)
            else:
                return visitor.visitChildren(self)


    class TypeValueContext(TypeRecContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TypeRecContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CAPS(self):
            return self.getToken(lambdaParser.CAPS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeValue" ):
                return visitor.visitTypeValue(self)
            else:
                return visitor.visitChildren(self)



    def typeRec(self):

        localctx = lambdaParser.TypeRecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_typeRec)
        self._la = 0 # Token type
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = lambdaParser.TypeFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(lambdaParser.T__2)
                self.state = 28
                self.typeRec()
                self.state = 29
                self.match(lambdaParser.T__1)
                self.state = 30
                self.typeRec()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 31
                    self.match(lambdaParser.T__1)
                    self.state = 32
                    self.typeRec()
                    self.state = 37
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 38
                self.match(lambdaParser.T__3)
                pass
            elif token in [9]:
                localctx = lambdaParser.TypeValueContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(lambdaParser.CAPS)
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


        def getRuleIndex(self):
            return lambdaParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class OpContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OP(self):
            return self.getToken(lambdaParser.OP, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)


    class ApplicationContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lambdaParser.TermContext)
            else:
                return self.getTypedRuleContext(lambdaParser.TermContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApplication" ):
                return visitor.visitApplication(self)
            else:
                return visitor.visitChildren(self)


    class TermParenthesisContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(lambdaParser.TermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermParenthesis" ):
                return visitor.visitTermParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class AbstractionContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TermContext
            super().__init__(parser)
            self.left = None # Token
            self.right = None # TermContext
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(lambdaParser.ID, 0)
        def term(self):
            return self.getTypedRuleContext(lambdaParser.TermContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstraction" ):
                return visitor.visitAbstraction(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(lambdaParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a lambdaParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(lambdaParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = lambdaParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = lambdaParser.TermParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 44
                self.match(lambdaParser.T__2)
                self.state = 45
                self.term(0)
                self.state = 46
                self.match(lambdaParser.T__3)
                pass
            elif token in [5]:
                localctx = lambdaParser.AbstractionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 48
                self.match(lambdaParser.T__4)
                self.state = 49
                localctx.left = self.match(lambdaParser.ID)
                self.state = 50
                self.match(lambdaParser.T__1)
                self.state = 51
                localctx.right = self.term(4)
                pass
            elif token in [8]:
                localctx = lambdaParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                self.match(lambdaParser.ID)
                pass
            elif token in [7]:
                localctx = lambdaParser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 53
                self.match(lambdaParser.NUM)
                pass
            elif token in [6]:
                localctx = lambdaParser.OpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 54
                self.match(lambdaParser.OP)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = lambdaParser.ApplicationContext(self, lambdaParser.TermContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 57
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 58
                    self.term(6) 
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         




