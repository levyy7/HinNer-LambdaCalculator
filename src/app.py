import streamlit as st
from grammar.syntaxAnalyzer import syntaxInfo
from visitor.LambdaVisitorExpanded import LambdaVisitorExpanded
from visitor.SemanticTree import SemanticTree

st.title("HinNer - Lambda Calculator")

user_input = st.text_input("Lambda Expression:", "")

parseTree, numErrors, syntaxExpr = syntaxInfo(user_input)

if numErrors > 0:
    st.write("Syntax Errors:", numErrors)
    st.write("Syntax Parsing:", syntaxExpr)
else:
    visitor = LambdaVisitorExpanded()
    semTree = visitor.visit(parseTree)
    
    dotTree = semTree.toDOT()
    st.graphviz_chart(dotTree)