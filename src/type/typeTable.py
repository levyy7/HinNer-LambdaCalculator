import pandas as pd
import streamlit as st


def createTypeTable(keys, values):
    
    df = pd.DataFrame(
        {
            "symbol": keys,
            "type": values
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