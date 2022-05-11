from dash import Dash, dcc, html, Input, Output, dash_table
import numpy as np
import pandas as pd

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])
    
    

def generateDashTable(df):
    cols = []
    vals = []
    edf = df.describe().to_dict()
    for j in edf:
        cols.append(j)
        vals.append(edf[j])
        print(vals)
    return html.Div([  
        dash_table.DataTable(vals, columns=cols )
    ])
    
    
    
    
    
    #     return dash_table.DataTable(*list((pd.DataFrame(df.describe()).to_dict())), style_header={
    #     'backgroundColor': 'rgb(30, 30, 30)',
    #     'color': 'white'
    # },
    # style_data={
    #     'backgroundColor': 'rgb(50, 50, 50)',
    #     'color': 'white'
    # })