from dataclasses import dataclass, field
from typing import Union
from enum import Enum

class ArithmeticOP(Enum):
    SUM = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'

@dataclass
class Terminal:
    val: int

@dataclass
class Operator:
    op: ArithmeticOP

@dataclass
class Variable:
    id: str

@dataclass
class Application:
    function: Union['Operator','Application']
    argument: 'Term'
  
@dataclass
class Abstraction:
    input: 'Variable'
    output: 'Term'


Term = Terminal | Operator | Variable | Application | Abstraction
    
def termToString(f):
    match f:
        case Abstraction(inp, out):
            return 'λ'
        case Application(func, arg):
            return '@'
        case Variable(iden):
            return iden
        case Operator(op):
            return op.value
        case Terminal(val):
            return str(val)



@dataclass 
class SemanticTree:
    root: Term
    count: int = field(default=0)
    
    def toDOT(self):
        dot = ["graph {"]

        self.toDOTRecursive(self.root, dot)
        
        dot.append("}")

        return "\n".join(dot)

    
    def toDOTRecursive(self, node, dot):
        match node:
            case Abstraction(inp, out):
                nodeID = self.count
                self.count = self.count + 1
                    
                dot.append(f'   {nodeID} [label="{termToString(node)}"]')
                
                child1ID = self.count
                
                self.toDOTRecursive(inp, dot)
                
                child2ID = self.count
                
                self.toDOTRecursive(out, dot)
                
                dot.append(f'   {nodeID} -- {child1ID}')
                dot.append(f'   {nodeID} -- {child2ID}')
                
            case Application(func, arg):
                nodeID = self.count
                self.count = self.count + 1
                    
                dot.append(f'   {nodeID} [label="{termToString(node)}"]')
                
                child1ID = self.count
                
                self.toDOTRecursive(func, dot)
                
                child2ID = self.count
                
                self.toDOTRecursive(arg, dot)
                
                dot.append(f'   {nodeID} -- {child1ID}')
                dot.append(f'   {nodeID} -- {child2ID}')
                
            case Variable(iden):
                nodeID = self.count
                self.count = self.count + 1
                    
                dot.append(f'   {nodeID} [label="{termToString(node)}"]')
            case Operator(op):
                nodeID = self.count
                self.count = self.count + 1
                    
                dot.append(f'   {nodeID} [label="{termToString(node)}"]')
            case Terminal(val):
                nodeID = self.count
                self.count = self.count + 1
                    
                dot.append(f'   {nodeID} [label="{termToString(node)}"]')
                
        
        

#https://stackoverflow.com/questions/2461170/tree-implementation-in-python
#tree = SemanticTree(Abstraction(Variable('x'), Application(Operator(ArithmeticOP.SUM), Variable('x'))))

#print(tree.toDOT())