class SyntaxException(Exception):

    def __init__(self, numErrors, syntaxExpr, message="Syntactic error found in input lambda expression"):
        self.message = message
        self.numErrors = numErrors
        self.syntaxExpr = syntaxExpr
        super().__init__(self.message)


class TypeException(Exception):
    
    def __init__(self, typeA, typeB, message="Type error between explicit type and inferred type"):
        self.message = message
        self.typeA = typeA
        self.typeB = typeB
        super().__init__(self.message)