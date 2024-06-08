# HinNer

*HinNer* is a [Streamlit](https://streamlit.io/) based web app that graphically displays the parsing tree and type inference of a *lambda* expression.


## Project Overview

The app allows as input a *haskell*-like language to codify expressions and types:

```haskell
2 :: N
(+) :: N -> N -> N
\x -> (+) 2 x
```

Those lines define `2` as type `N`, `(+)` as type `N -> N -> N` and finally the expression `\x -> (+) 2 x`. When typing the final expression the app displays the following parsing tree:

![](/img/fig1.png)

If we focus at the root of the tree, we can see that the inferred type of `\x -> (+) 2 x` is `N -> N`.


### Grammar

The file [lambda.g4](src/grammar/lambda.g4) defines the accepted input grammar using [ANTLR4](https://www.antlr.org/). The grammar admits two types of expressions:

- A term expression codified in a *haskell*-like way. A term can be made of abstractions (`λ`), applications (`@`) and terminals (eg. numbers, strings starting by lowecase letters...).
  ```haskell
  2
  x
  (+) 2
  \x -> (+) 2 x
  (\x -> (+) 2 x) 4
  foldl (\x -> \y -> (+) x y) 0 xs
  ```

- A type expression codified in a *haskell*-like way. These expressions consist in a label on the left side (e.g. numbers, strings starting by lowecase letters...) and a type declaration on the right side (in capital letters).
  ```haskell
  2 :: N
  (+) :: N -> N -> N
  map :: (N -> M) -> NL -> ML
  foldl :: (N -> N -> N) -> N -> NL -> N
  ```

### Type Inference

The type inference system is made using a simplified yet powerful version of the *Hindley-Milner* algorithm. 

```python
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
```

The *Hindley-Milner* algorithm tries to unify the current node with its children, in the way that the application or abstraction works. 

```python
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
```

There are lots of ways to perform the unification of variables. The method used in this project is via a *Union-Find* algorithm approach, where all variables start in disjoint components and via unification those components start merging, always being the root the most complex version of the component. 

Credits to [deehzee](https://github.com/deehzee/unionfind) for the *Union-Find* algorithm implementation.


A demonstration of the inference the app is capable of:

![](/img/fig2.png)


## Usage

The app can be used at [webadress](), but in order to execute in at your local pc the following steps must be made:

- Run the [Makefile](/Makefile) file.
  ```bash
  make
  ```
- A window of your local browser should have appeared with the app hosted in Localhost.