import streamlit as st
from grammar.syntaxAnalyzer import syntaxInfo
from visitor.LambdaVisitorExpanded import LambdaVisitorExpanded
from visitor.SemanticTree import SemanticTree
from type.typeTable import createTypeTable, addRowsTable

st.title("HinNer - Lambda Calculator")

typeDict = {
    '2'  : 'N',
    '(+)': 'N -> N -> N'
}




user_input = st.text_input("Lambda Expression:", "")

parseTree, numErrors, syntaxExpr = syntaxInfo(user_input)

if numErrors > 0:
    st.write("Syntax Errors:", numErrors)
    st.write("Syntax Parsing:", syntaxExpr)
else:
    visitor = LambdaVisitorExpanded()
    expr = visitor.visit(parseTree)
    dotTree = SemanticTree(None).toDOT()
    
    if type(expr) is SemanticTree:
        dotTree = expr.toDOT()
    else:
        print('llego')
        print(next(iter( expr.items() )))
        typeDict.update(expr)
        
    cols = st.columns(2)
    with cols[0]:
        st.graphviz_chart(dotTree)
    with cols[1]:
        createTypeTable(list(typeDict.keys()), list(typeDict.values()))
    