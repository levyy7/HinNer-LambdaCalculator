from dataclasses import dataclass, field
from typing import Union
from UnionFind import UnionFind
from exceptions import TypeException


def typeListToString(typeList):
    if type(typeList) is list:
        l = [typeListToString(tl) for tl in typeList]
        return '(' + (" -> ".join(l)) + ')'
    else:
        return typeList


def listify(arg):
    return arg if isinstance(arg, list) else [arg]

# Redefine UnionFind


class UnionFindST(UnionFind):

    def union(self, x: 'TypeGeneric', y: 'TypeGeneric'):
        """Merge the components of the two given elements into one.

        Parameters
        ----------
        x : immutable object
        y : immutable object

        Returns
        -------
        None

        """
        # Initialize if they are not already in the collection
        for elt in [x, y]:
            if elt not in self:
                self.add(elt)

        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return

        typeX = self._elts[xroot]
        typeY = self._elts[yroot]

        # Check for errors

        if not compatibleTypes(typeX, typeY):
            raise TypeException(typeX.toString(), typeY.toString())

        if typeY.isMoreComplexThan(typeX) == 1:
            self._par[xroot] = yroot
            self._siz[yroot] += self._siz[xroot]
        else:
            self._par[yroot] = xroot
            self._siz[xroot] += self._siz[yroot]
        self.n_comps -= 1


# Type Classes


@dataclass
class TypeValue:
    value: str
    isDefined: bool

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return hash(str(self)) == hash(str(other))

    def toString(self):
        return self.value

    def isMoreComplexThan(self, y):
        match self, y:
            case (TypeValue(), TypeValue()):
                if self.isDefined:
                    return 1
                elif y.isDefined:
                    return 0
                else:
                    return -1

            case (TypeFunction(), TypeValue()): return 1

            case (TypeValue(), TypeFunction()): return 0

            case (TypeFunction(), TypeFunction()):
                argXisMoreComplexThanY = self.arg.isMoreComplexThan(y.arg)

                if argXisMoreComplexThanY != -1:
                    return argXisMoreComplexThanY
                else:
                    bodyXisMoreComplexThanY = self.body.isMoreComplexThan(
                        y.body)
                    if bodyXisMoreComplexThanY != -1:
                        return bodyXisMoreComplexThanY

                return -1


@dataclass
class TypeFunction:
    arg: Union['TypeFunction', TypeValue]
    body: Union['TypeFunction', TypeValue]

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return hash(str(self)) == hash(str(other))

    @classmethod
    def fromList(self, lst: list):
        if len(lst) == 0:
            return None
        if len(lst) == 1:
            return TypeValue(lst[0], True)
        elif (len(lst) >= 2):
            arg = TypeFunction.fromList(listify(lst[0]))
            body = TypeFunction.fromList(listify(lst[1:]))
            return TypeFunction(arg, body)

    def toList(self):
        argl = [self.arg.toList()] if isinstance(
            self.arg, TypeFunction) else [self.arg.value]
        bodyl = self.body.toList() if isinstance(
            self.body, TypeFunction) else [self.body.value]

        return argl + bodyl

    def toString(self):
        typeList = self.toList()

        return typeListToString(typeList)[1:-1]

    def copy(self):
        return TypeFunction(self.arg.copy(), self.body.copy())

    def isMoreComplexThan(self, y):
        match self, y:
            case (TypeValue(), TypeValue()):
                if self.isDefined:
                    return 1
                elif y.isDefined:
                    return 0
                else:
                    return -1

            case (TypeFunction(), TypeValue()): return 1

            case (TypeValue(), TypeFunction()): return 0

            case (TypeFunction(), TypeFunction()):
                argXisMoreComplexThanY = self.arg.isMoreComplexThan(y.arg)

                if argXisMoreComplexThanY != -1:
                    return argXisMoreComplexThanY
                else:
                    bodyXisMoreComplexThanY = self.body.isMoreComplexThan(
                        y.body)
                    if bodyXisMoreComplexThanY != -1:
                        return bodyXisMoreComplexThanY

                return -1


TypeGeneric = TypeValue | TypeFunction

# Type Functions


def compatibleTypes(t1, t2):
    match (t1, t2):
        case (TypeValue(), TypeValue()):
            if t1.isDefined and t2.isDefined:
                return t1.value == t2.value
            else:
                return True
        case (TypeValue(), TypeFunction()):
            if t1.isDefined or isInFunction(t1, t2):
                return False
            else:
                return True
        case(TypeFunction(), TypeValue()):
            return compatibleTypes(t2, t1)
        case (TypeFunction(), TypeFunction()):
            argCompatible = compatibleTypes(t1.arg, t2.arg)
            bodyCompatible = compatibleTypes(t1.body, t2.body)
            return argCompatible and bodyCompatible


def isInFunction(t1: TypeValue, t2: TypeFunction):
    if isinstance(t2.arg, TypeValue):
        inArg = t1.value == t2.arg.value
    else:
        inArg = isInFunction(t1, t2.arg)

    if isinstance(t2.body, TypeValue):
        inBody = t1.value == t2.body.value
    else:
        inBody = isInFunction(t1, t2.body)

    return inArg or inBody


# Lambda Classes

@dataclass
class Variable:
    id: str
    tipus: TypeGeneric = field(default=TypeValue('-1', False))

    def toString(self):
        return f'{self.id} \n {self.tipus.toString()}'


@dataclass
class Application:
    function: 'Term'
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


Term = Variable | Application | Abstraction


# SemanticTree Class

class SemanticTree:

    def __init__(self, t: Term):
        self.root = t
        self.unfi = UnionFindST()
        self.count = 0
        self.inferredDict = {}

    def initializeTypes(self, typeDict):
        self.count = 0
        labelDict = {}

        self.initializeTypesRec(self.root, typeDict, labelDict)

    def initializeTypesRec(self, node, typeDict, labelDict):
        match node:
            case Abstraction(inp, out):
                label = chr(ord('a') + self.count)
                node.tipus = TypeValue(label, False)

                self.count = self.count + 1
                self.unfi.add(node.tipus)

                self.initializeTypesRec(inp, typeDict, labelDict)
                self.initializeTypesRec(out, typeDict, labelDict)

            case Application(func, arg):
                label = chr(ord('a') + self.count)
                node.tipus = TypeValue(label, False)

                self.count = self.count + 1
                self.unfi.add(node.tipus)

                self.initializeTypesRec(func, typeDict, labelDict)
                self.initializeTypesRec(arg, typeDict, labelDict)

            case Variable(iden):
                if iden in typeDict:
                    lst = typeDict[iden]
                    node.tipus = TypeFunction.fromList(lst) if len(
                        lst) >= 2 else TypeValue(lst[0], True)
                    self.unfi.add(node.tipus)
                elif iden in labelDict:
                    node.tipus = labelDict[iden]
                else:
                    label = chr(ord('a') + self.count)
                    node.tipus = TypeValue(label, False)
                    labelDict[iden] = node.tipus

                    self.unfi.add(node.tipus)
                    self.count = self.count + 1

    def inferTypes(self):

        self.unfi.add(TypeValue('z', True))

        self.hindleyMilner(self.root)

        for component in self.unfi.components():
            root = self.unfi[self.unfi.find(list(component)[0])]
            self.propagateTypes(root)

        for component in self.unfi.components():
            for element in component:
                if isinstance(element, TypeValue) and not element.isDefined:
                    root = self.unfi[self.unfi.find(element)]
                    self.inferredDict[element.value] = root.toList() if isinstance(
                        root, TypeFunction) else [root.value]

        self.inferredDict = dict(sorted(self.inferredDict.items()))

    def hindleyMilner(self, node):
        match node:
            case Abstraction(inp, out):
                self.hindleyMilner(inp)
                self.hindleyMilner(out)

                self.unify(node.tipus, TypeFunction(inp.tipus, out.tipus))

            case Application(func, arg):
                self.hindleyMilner(func)
                self.hindleyMilner(arg)

                self.unify(TypeFunction(arg.tipus, node.tipus), func.tipus)
            case Variable(iden):
                return

    def propagateTypes(self, t):
        nType = self.propagateTypesRec(t)
        self.unfi.union(t, nType)

    def propagateTypesRec(self, t):
        if not t in self.unfi:
            return t
        tRoot = self.unfi[self.unfi.find(t)]
        match tRoot:
            case TypeValue():
                return tRoot
            case TypeFunction():
                arg = self.propagateTypesRec(tRoot.arg)
                body = self.propagateTypesRec(tRoot.body)
                return TypeFunction(arg, body)

    # Tratara de unificar los dos terminos, modificando el de la derecha

    def unify(self, t1, t2):
        t1root = self.unfi[self.unfi.find(t1)] if t1 in self.unfi else t1
        t2root = self.unfi[self.unfi.find(t2)] if t2 in self.unfi else t2

        match (t1root, t2root):
            case (TypeValue(), TypeValue()):
                self.unfi.union(t1root, t2root)
            case (TypeValue(), TypeFunction()):
                self.unfi.union(t1root, t2root)
            case(TypeFunction(), TypeValue()):
                self.unfi.union(t1root, t2root)
            case (TypeFunction(), TypeFunction()):
                self.unify(t1root.arg, t2root.arg)
                self.unify(t1root.body, t2root.body)

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

                nodeRoot = self.unfi[self.unfi.find(node.tipus)]
                dot.append(f'   {nodeID} [label="λ \n {nodeRoot.toString()}"]')

                child1ID = self.count

                self.toDOTRecursive(inp, dot)

                child2ID = self.count

                self.toDOTRecursive(out, dot)

                dot.append(f'   {nodeID} -- {child1ID}')
                dot.append(f'   {nodeID} -- {child2ID}')

            case Application(func, arg):
                nodeID = self.count
                self.count = self.count + 1

                nodeRoot = self.unfi[self.unfi.find(node.tipus)]
                dot.append(f'   {nodeID} [label="@ \n {nodeRoot.toString()}"]')

                child1ID = self.count

                self.toDOTRecursive(func, dot)

                child2ID = self.count

                self.toDOTRecursive(arg, dot)

                dot.append(f'   {nodeID} -- {child1ID}')
                dot.append(f'   {nodeID} -- {child2ID}')

            case Variable(iden):
                nodeID = self.count
                self.count = self.count + 1

                nodeRoot = self.unfi[self.unfi.find(node.tipus)]
                dot.append(
                    f'   {nodeID} [label="{iden} \n {nodeRoot.toString()}"]')
