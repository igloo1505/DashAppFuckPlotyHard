from dash import Dash, dcc, html, Input, Output, callback
from pages import MatrixInMotion, SphericalRebound
app = Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


index_page = html.Div(
    [
        dcc.Link("Go to Page 1", href="/page-1"),
        html.Br(),
        dcc.Link("Go to Page 2", href="/page-2"),
    ]
)







# Update the index
@callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/matrixInMotion":
        return MatrixInMotion
    elif pathname == "/reboundForce":
        return SphericalRebound
    else:
        return index_page
    # You could also return a 404 "URL not found" page here


if __name__ == "__main__":
    app.run_server(debug=True)
