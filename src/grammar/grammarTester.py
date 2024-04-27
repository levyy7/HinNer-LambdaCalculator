from antlr4 import *
from lambdaLexer import lambdaLexer
from lambdaParser import lambdaParser
input_stream = InputStream(input('? '))
lexer = lambdaLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = lambdaParser(token_stream)
tree = parser.root()
print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
print(tree.toStringTree(recog=parser))