from dash import Dash, dcc, html, Input, Output, dash_table
import numpy as np
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

def generate_table(dataframe, max_rows=10, describe=False):
    d = dataframe.columns
    b = []
    extraCols = [
"n",
"count",
"mean",
"std",
"min",
"25\%",
"50\%",
"75\%",
"max",
"max",
"max",
    ]
    describe_num_df = dataframe.describe(include=["int64","float64"])
    describe_num_df.reset_index(inplace=True)
    # To remove any variable from plot
    describe_num_df = describe_num_df[describe_num_df["index"] != "count"]
    newVals = []
    total_columns = dataframe.columns
# store numerical and categorical column in two different variables. It comes handy during visualizaion.
    num_col = dataframe._get_numeric_data().columns
    cat_col = list(set(total_columns)-set(num_col))
    for i in num_col:
        if i in ["index"]:
            continue
        print(describe_num_df)
        # print(dataframe.iloc[i])
            
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in d], id="genTableRowHead")
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ], "tableRowBody") for i in range(min(len(dataframe + 1), max_rows))
        ])
    ])
    
    

def generateDashTable(df):
    cols = []
    vals = []
    # edf = df.describe().to_dict()
    edf = df
    for j in edf:
        cols.append(j)
        vals.append(edf[j])
        # print(vals)
    return dash_table.DataTable(df.to_dict())
    # _df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
    # return dash_table.DataTable(_df.to_dict('records'), [{"name": i, "id": i} for i in _df.columns]),
    
    
    
    
    
# def bokehTable(df):
#     source = ColumnDataSource(df)
