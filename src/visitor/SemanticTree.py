from dataclasses import dataclass, field
from typing import Union, List
from enum import Enum
from UnionFind import UnionFind


# Type Classes


@dataclass
class TypeValue:
    value: str
    isDefined: bool
    
    def __hash__(self):
        print(hash(str(self)))
        return hash(str(self))

    def __eq__(self,other):
        return hash(str(self)) == hash(str(other))
    
    
    def toString(self):
        return self.value
    

@dataclass 
class TypeFunction:
    arg: Union['TypeFunction', TypeValue]
    body: Union['TypeFunction', TypeValue]
    
    
    def __hash__(self):
        print(hash(str(self)))
        return hash(str(self))

    def __eq__(self,other):
        return hash(str(self)) == hash(str(other))
    
    
    @classmethod
    def fromList(self, lst : list, typeDict : dict = None):
        if len(lst) == 0: 
            return None
        if len(lst) == 1:
            return dict[lst[0]]
        elif (len(lst) >= 2):
            arg = TypeFunction.fromList(lst[0], typeDict)
            body = TypeFunction.fromList(lst[1:], typeDict)
            return TypeFunction(arg, body)
        
    
    def toList(self):
        argl = self.arg.toList() if type(self.arg) is TypeFunction else self.arg.value
        bodyl = self.body.toList() if type(self.body) is TypeFunction else [self.body.value]
        
        return [argl] + bodyl
    
    def toString(self):
        str1 = self.arg.toString()
        str2 = self.body.toString()
        return '(' + str1 + ' -> ' + str2  + ')'
    
    def copy(self):
        return TypeFunction(self.arg.copy(), self.body.copy())
        
 
   
TypeGeneric = TypeValue | TypeFunction


# Lambda Classes

class ArithmeticOP(Enum):
    SUM = '(+)'
    SUB = '(-)'
    MUL = '(*)'
    DIV = '(/)'

@dataclass
class Terminal:
    val: int
    tipus: TypeGeneric = field(default=TypeValue('-1', False))
    
    def toString(self):
        return f'{str(self.val)} \n {self.tipus.toString()}'

@dataclass
class Operator:
    op: ArithmeticOP
    tipus: TypeGeneric = field(default=TypeValue('-1', False))
    
    def toString(self):
        return f'{self.op.value} \n {self.tipus.toString()}'

@dataclass
class Variable:
    id: str
    tipus: TypeGeneric = field(default=TypeValue('-1', False))
    
    def toString(self):
        return f'{self.id} \n {self.tipus.toString()}'

@dataclass
class Application:
    function: Union['Operator','Application']
    argument: 'Term'
    tipus: TypeGeneric = field(default=TypeValue('-1', False))
    
    def toString(self):
        return f'@ \n {self.tipus.toString()}'
  
@dataclass
class Abstraction:
    input: 'Variable'
    output: 'Term'
    tipus: TypeGeneric = field(default=TypeValue('-1', False))
    
    def toString(self):
        return f'λ \n {self.tipus.toString()}'

Term = Terminal | Operator | Variable | Application | Abstraction



#SemanticTree Class

class SemanticTree:
    
    def __init__(self, t : Term):
        self.root = t
        self.unfi = UnionFind()
    
    
    def inferTypes(self, typeDict):
        self.count = 0
        labelDict = {}
        
        self.initializeTypes(self.root, typeDict, labelDict)
        
        #self.hindleyMilner(self.root, typeDict, labelDict)

        
    def initializeTypes(self, node, typeDict, labelDict):
        match node:
            case Abstraction(inp, out):
                label = chr(ord('a') + self.count)
                node.tipus = TypeValue(label, False)
                
                self.count = self.count + 1
                self.unfi.add(node.tipus)
                
                self.initializeTypes(inp, typeDict, labelDict)
                self.initializeTypes(out, typeDict, labelDict)
                
            case Application(func, arg):
                label = chr(ord('a') + self.count)
                node.tipus = TypeValue(label, False)
                
                self.count = self.count + 1
                self.unfi.add(node.tipus)
                
                self.initializeTypes(func, typeDict, labelDict)
                self.initializeTypes(arg, typeDict, labelDict)
                
            case Variable(iden):
                if iden in typeDict:
                    lst = typeDict[iden]
                    node.tipus = TypeFunction.fromList(lst) if len(lst) >= 2 else TypeValue(lst[0], True)
                elif iden in labelDict:
                    node.tipus = labelDict[iden]
                else:
                    label = chr(ord('a') + self.count)
                    node.tipus = TypeValue(label, False)
                    labelDict[iden] = node.tipus
                    
                    self.unfi.add(node.tipus)
                    self.count = self.count + 1

            case Operator(op):
                opID = op.value
                if opID in typeDict:
                    lst = typeDict[opID]
                    node.tipus = TypeFunction.fromList(lst) if len(lst) >= 2 else TypeValue(lst[0], True)
                elif opID in labelDict:
                    node.tipus = labelDict[opID]
                else:
                    label = chr(ord('a') + self.count)
                    node.tipus = TypeValue(label, False)
                    labelDict[opID] = node.tipus
                    
                    self.count = self.count + 1
                    self.unfi.add(node.tipus)
                    
            case Terminal(val):
                valID = str(val)
                if valID in typeDict:
                    lst = typeDict[valID]
                    node.tipus = TypeFunction.fromList(lst) if len(lst) >= 2 else TypeValue(lst[0], True)
                elif valID in labelDict:
                    node.tipus = labelDict[valID]
                else:
                    label = chr(ord('a') + self.count)
                    node.tipus = TypeValue(label, False)
                    labelDict[valID] = node.tipus
                    
                    self.count = self.count + 1
                    self.unfi.add(node.tipus)
    
    def hindleyMilner(self, node, typeDict, labelDict):
        match node:
            #case Abstraction(inp, out):
                #nodeLeft = self.hindleyMilner(inp, typeDict, labelDict)
                #nodeRight = self.hindleyMilner(out, typeDict, labelDict)
                
                #label = chr(ord('a') + self.count)
                #node.tipus = UndefinedType(label)
                #self.count = self.count + 1
                
                
                
            case Application(func, arg):
                self.hindleyMilner(func, typeDict, labelDict)
                self.hindleyMilner(arg, typeDict, labelDict)
                
                self.unify(TypeFunction(arg.tipus, node.tipus), func.tipus)
                
                
            case Variable(iden):
                return

            case Operator(op):
                return
                    
            case Terminal(val):
                return
                
                
    #Tratara de unificar los dos terminos, modificando el de la derecha
    def unify(self, t1, t2):
        match (t1, t2):
            case (TypeValue(), TypeValue()):
                if t1.isDefined: self.propagate(t1, t2)
                elif t2.isDefined: self.propagate(t2, t1)
            case (TypeValue(), TypeFunction()):
                self.unify(t2, t1)
            case(TypeFunction(), TypeValue()):
                self.propagate(t1, t2)
            case (TypeFunction(), TypeFunction()):
                t1l = t1.toList()
                t2l = t2.toList()
                
                if len(t1l) != len(t2l): return "error"
                
                for (subTerm1, subTerm2) in zip(t1l, t2l):
                    self.unify(subTerm1, subTerm2)
                

    def propagate(self, toBePropagated : TypeGeneric, propagateTo : TypeGeneric):
        tbl = toBePropagated.toList()
        
        for t in self.unfi.component(propagateTo):
            tl = t.toList()
            
            #HACE FALTA TRATAR ERRORES
            #utulizar diccionaro labelDict para ver el tipo actual y cambiarlo
            
            """
            if toBePropagated.isDefined and t.isDefined:
                if len(tbl) != len(tl): return "error"
                for (tbi, ti) in zip(tbl, tl): 
                    if tbi != ti: return "error"
            """
                
                 
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