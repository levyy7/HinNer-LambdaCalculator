import pandas as pd
import streamlit as st


def createTypeTable(keys, values):
    
    aux = values
    for i in range(len(aux)):
        aux[i] = " -> ".join(aux[i])
        #reduce((lambda x,y : x + ' -> ' + y), aux[i][1:], aux[i][0])
    
    df = pd.DataFrame(
        {
            "symbol": keys,
            "type": aux
        }
    )
    
    table = st.dataframe(
        df,
        column_config={
            "symbol": "Symbol",
            "type": "Type",
        },
        hide_index=True
    )
    
    return table
    


def addRowsTable(table, symbol, tipus):
    table.add_rows(pd.DataFrame(
        {
            "symbol": [symbol],
            "type": [tipus]
        }
    ))