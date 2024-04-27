import streamlit as st
from grammar.syntaxAnalyzer import syntaxInfo

st.title("HinNer - Lambda Calculator")

user_input = st.text_input("Lambda Expression:", "")

numErrors, syntaxExpr = syntaxInfo(user_input)

st.write("Syntax Errors:", numErrors)
st.write("Syntax Parsing:", syntaxExpr)