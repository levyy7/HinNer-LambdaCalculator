from antlr4 import *
from .lambdaLexer import lambdaLexer
from .lambdaParser import lambdaParser
from exceptions import SyntaxException

def syntaxInfo(input):
    lexer = lambdaLexer(InputStream(input))
    token_stream = CommonTokenStream(lexer)
    parser = lambdaParser(token_stream)
    parseTree = parser.root()
    
    numErrors = parser.getNumberOfSyntaxErrors()
    syntaxExpr = parseTree.toStringTree(recog=parser)
    
    print(syntaxExpr)
    
    if numErrors > 0:
        raise SyntaxException(numErrors, syntaxExpr)
    
    return parseTree