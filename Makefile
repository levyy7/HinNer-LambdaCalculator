run: grammar
	streamlit run ./src/app.py

grammar:
	antlr4 -Dlanguage=Python3 -no-listener -visitor ./src/grammar/lambda.g4
