from dataclasses import dataclass, field
from typing import Union, List
from enum import Enum

#Type classes
@dataclass
class UndefinedType:
    id: str
    
    def toString(self):
        return self.id

@dataclass 
class DefinedType:
    tipus: List[str]
    
    def toString(self):
        return " -> ".join(self.tipus)
    
VarType = DefinedType | UndefinedType



class ArithmeticOP(Enum):
    SUM = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'

@dataclass
class Terminal:
    val: int
    tipus: VarType = field(default=UndefinedType('-1'))
    
    def toString(self):
        return f'{str(self.val)} \n {self.tipus.toString()}'

@dataclass
class Operator:
    op: ArithmeticOP
    tipus: VarType = field(default=UndefinedType('-1'))
    
    def toString(self):
        return f'{self.op.value} \n {self.tipus.toString()}'

@dataclass
class Variable:
    id: str
    tipus: VarType = field(default=UndefinedType('-1'))
    
    def toString(self):
        return f'{self.id} \n {self.tipus.toString()}'

@dataclass
class Application:
    function: Union['Operator','Application']
    argument: 'Term'
    tipus: VarType = field(default=UndefinedType('-1'))
    
    def toString(self):
        return f'@ \n {self.tipus.toString()}'
  
@dataclass
class Abstraction:
    input: 'Variable'
    output: 'Term'
    tipus: VarType = field(default=UndefinedType('-1'))
    
    def toString(self):
        return f'λ \n {self.tipus.toString()}'



Term = Terminal | Operator | Variable | Application | Abstraction


@dataclass 
class SemanticTree:
    root: Term
    count: int = field(default=0)
    
    
    def inferTypes(self, typeDict):
        self.count = 0
        labelDict = {}
        
        self.initializeTypes(self.root, typeDict, labelDict)

        
    def initializeTypes(self, node, typeDict, labelDict):
        match node:
            case Abstraction(inp, out):
                label = chr(ord('a') + self.count)
                node.tipus = UndefinedType(label)
                self.count = self.count + 1
                
                self.initializeTypes(inp, typeDict, labelDict)
                self.initializeTypes(out, typeDict, labelDict)
                
            case Application(func, arg):
                label = chr(ord('a') + self.count)
                node.tipus = UndefinedType(label)
                self.count = self.count + 1
                
                self.initializeTypes(func, typeDict, labelDict)
                self.initializeTypes(arg, typeDict, labelDict)
                
            case Variable(iden):
                if iden in typeDict:
                    node.tipus = DefinedType(typeDict[iden])
                elif iden in labelDict:
                    node.tipus = UndefinedType(labelDict[iden])
                else:
                    label = chr(ord('a') + self.count)
                    node.tipus = UndefinedType(label)
                    labelDict[iden] = label
                    self.count = self.count + 1

            case Operator(op):
                opID = op.value
                if opID in typeDict:
                    node.tipus = DefinedType(typeDict[opID])
                elif opID in labelDict:
                    node.tipus = UndefinedType(labelDict[opID])
                else:
                    label = chr(ord('a') + self.count)
                    node.tipus = UndefinedType(label)
                    labelDict[opID] = label
                    self.count = self.count + 1
                    
            case Terminal(val):
                valID = str(val)
                if valID in typeDict:
                    node.tipus = DefinedType(typeDict[valID])
                elif valID in labelDict:
                    node.tipus = UndefinedType(labelDict[valID])
                else:
                    label = chr(ord('a') + self.count)
                    node.tipus = UndefinedType(label)
                    labelDict[valID] = label
                    self.count = self.count + 1
    
    
    
    def toDOT(self):
        self.count = 0
        dot = ["graph {"]

        self.toDOTRecursive(self.root, dot)
        
        dot.append("}")

        return "\n".join(dot)

    
    def toDOTRecursive(self, node, dot):
        match node:
            case Abstraction(inp, out):
                nodeID = self.count
                self.count = self.count + 1
                    
                dot.append(f'   {nodeID} [label="{node.toString()}"]')
                
                child1ID = self.count
                
                self.toDOTRecursive(inp, dot)
                
                child2ID = self.count
                
                self.toDOTRecursive(out, dot)
                
                dot.append(f'   {nodeID} -- {child1ID}')
                dot.append(f'   {nodeID} -- {child2ID}')
                
            case Application(func, arg):
                nodeID = self.count
                self.count = self.count + 1
                    
                dot.append(f'   {nodeID} [label="{node.toString()}"]')
                
                child1ID = self.count
                
                self.toDOTRecursive(func, dot)
                
                child2ID = self.count
                
                self.toDOTRecursive(arg, dot)
                
                dot.append(f'   {nodeID} -- {child1ID}')
                dot.append(f'   {nodeID} -- {child2ID}')
                
            case Variable(iden):
                nodeID = self.count
                self.count = self.count + 1
                    
                dot.append(f'   {nodeID} [label="{node.toString()}"]')
            case Operator(op):
                nodeID = self.count
                self.count = self.count + 1
                    
                dot.append(f'   {nodeID} [label="{node.toString()}"]')
            case Terminal(val):
                nodeID = self.count
                self.count = self.count + 1
                    
                dot.append(f'   {nodeID} [label="{node.toString()}"]')
                
        
        

#https://stackoverflow.com/questions/2461170/tree-implementation-in-python
#tree = SemanticTree(Abstraction(Variable('x'), Application(Operator(ArithmeticOP.SUM), Variable('x'))))

#print(tree.toDOT())