from dash import html, dcc
import dash
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
sys.path.append(module_path)
from textContent.HomeText import definitionText
dash.register_page(__name__, path="/", top_nav=True)


textDivs = []

for i, t in enumerate(definitionText):
    j = dcc.Markdown([
        t
    ], id=f"definition-markdown-{i}", className="markdown-definition", mathjax=True)
    textDivs.append(j)

layout = html.Div([
html.Div([
    html.H4(['Definitions',
    html.Div([], id="title-text-underline"),
             ], id="definition-title-container"),
    html.Div([
    *textDivs
    ], id="home-page-text-container")
    ], id="home-page-definition-container")
    ], id="home-page-container") 
