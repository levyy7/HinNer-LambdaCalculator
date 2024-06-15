import streamlit as st
from grammar.syntaxAnalyzer import syntaxInfo
from visitor.LambdaVisitorExpanded import LambdaVisitorExpanded
from visitor.SemanticTree import SemanticTree
from type.typeTable import createTypeTable, addRowsTable
from pickle import dumps, loads
from exceptions import *

st.title("HinNer - Lambda Calculator")

# If
if 'typeDict' not in st.session_state:
    st.session_state['typeDict'] = dumps({})
if 'exprTree' not in st.session_state:
    st.session_state['exprTree'] = dumps(SemanticTree(None))

user_input = st.text_input("Lambda Expression:", "")


try:
    parseTree = syntaxInfo(user_input)

    visitor = LambdaVisitorExpanded()
    expr = visitor.visit(parseTree)

    # Recover type table:
    typeDict = loads(st.session_state['typeDict'])

    if isinstance(expr, SemanticTree):
        st.session_state['exprTree'] = dumps(expr)
    else:
        typeDict.update(expr)

    exprTree = loads(st.session_state['exprTree'])

    exprTree.initializeTypes(typeDict)
    dotTreeInitialized = exprTree.toDOT()

    exprTree.inferTypes()
    dotTreeInferred = exprTree.toDOT()
    labelTypeInferred = exprTree.inferredDict

    # Write tables and trees
    cols = st.columns(2)
    with cols[1]:
        cols2 = st.columns(2)
        with cols2[0]:
            st.write("Defined Type Table")
            createTypeTable(list(typeDict.keys()), list(typeDict.values()))
        with cols2[1]:
            st.write("Label Type Table")
            createTypeTable(list(labelTypeInferred.keys()),
                            list(labelTypeInferred.values()))

        on = st.toggle("Display Inferred Tree", value=True)
    with cols[0]:
        if on:
            st.graphviz_chart(dotTreeInferred)
        else:
            st.graphviz_chart(dotTreeInitialized)

    # Store typeDict
    st.session_state['typeDict'] = dumps(typeDict)

except SyntaxException as inst:
    st.write("Syntax Error: " + inst.message)
    # st.write("Num Errors: " + str(inst.numErrors))
    st.write("Syntax Expression: " + inst.syntaxExpr)
except TypeException as inst:
    st.write("Type Error: " + inst.message)
    st.write(inst.typeA + ' vs ' + inst.typeB)
