# Generated from ./src/grammar/lambda.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,12,63,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,1,1,
        1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,
        9,4,9,46,8,9,11,9,12,9,47,1,10,1,10,5,10,52,8,10,10,10,12,10,55,
        9,10,1,11,4,11,58,8,11,11,11,12,11,59,1,11,1,11,0,0,12,1,1,3,2,5,
        3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,1,0,3,1,0,48,57,
        4,0,48,57,65,90,95,95,97,122,3,0,9,10,13,13,32,32,65,0,1,1,0,0,0,
        0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,
        1,0,0,0,1,25,1,0,0,0,3,27,1,0,0,0,5,30,1,0,0,0,7,32,1,0,0,0,9,34,
        1,0,0,0,11,36,1,0,0,0,13,38,1,0,0,0,15,40,1,0,0,0,17,42,1,0,0,0,
        19,45,1,0,0,0,21,49,1,0,0,0,23,57,1,0,0,0,25,26,5,92,0,0,26,2,1,
        0,0,0,27,28,5,45,0,0,28,29,5,62,0,0,29,4,1,0,0,0,30,31,5,40,0,0,
        31,6,1,0,0,0,32,33,5,41,0,0,33,8,1,0,0,0,34,35,5,43,0,0,35,10,1,
        0,0,0,36,37,5,45,0,0,37,12,1,0,0,0,38,39,5,42,0,0,39,14,1,0,0,0,
        40,41,5,47,0,0,41,16,1,0,0,0,42,43,5,94,0,0,43,18,1,0,0,0,44,46,
        7,0,0,0,45,44,1,0,0,0,46,47,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,
        48,20,1,0,0,0,49,53,2,97,122,0,50,52,7,1,0,0,51,50,1,0,0,0,52,55,
        1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,22,1,0,0,0,55,53,1,0,0,0,
        56,58,7,2,0,0,57,56,1,0,0,0,58,59,1,0,0,0,59,57,1,0,0,0,59,60,1,
        0,0,0,60,61,1,0,0,0,61,62,6,11,0,0,62,24,1,0,0,0,4,0,47,53,59,1,
        6,0,0
    ]

class lambdaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    SUM = 5
    SUB = 6
    MUL = 7
    DIV = 8
    POW = 9
    NUM = 10
    ID = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\'", "'->'", "'('", "')'", "'+'", "'-'", "'*'", "'/'", "'^'" ]

    symbolicNames = [ "<INVALID>",
            "SUM", "SUB", "MUL", "DIV", "POW", "NUM", "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "SUM", "SUB", "MUL", "DIV", 
                  "POW", "NUM", "ID", "WS" ]

    grammarFileName = "lambda.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


