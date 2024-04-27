from antlr4 import *
from .lambdaLexer import lambdaLexer
from .lambdaParser import lambdaParser

def syntaxInfo(input):
    lexer = lambdaLexer(InputStream(input))
    token_stream = CommonTokenStream(lexer)
    parser = lambdaParser(token_stream)
    tree = parser.root()
    
    numErrors = parser.getNumberOfSyntaxErrors()
    syntaxExpr = tree.toStringTree(recog=parser)
    
    return numErrors, syntaxExpr