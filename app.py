# import dash
# dash.register_page(__name__, path="/")
# from dash import Dash, dcc, html, Input, Output, callback
# from pages import MatrixInMotion, SphericalRebound
# from pages.MatrixInMotion import MatrixInMotion
# import dash_labs as dl
# import dash_bootstrap_components as dbc   
import dash
import dash_labs as dl
import dash_bootstrap_components as dbc
from components.Sidebar import sidebar
from components.Navbar import Navbar

app = dash.Dash(
    __name__, 
    plugins=[dl.plugins.pages],
    external_stylesheets=[dbc.themes.CYBORG],
)



app.layout = dbc.Container(
    [sidebar(), Navbar(), dl.plugins.page_container],
    fluid=True,
)


app.config.suppress_callback_exceptions = True

if __name__ == "__main__":
    app.run_server(debug=True)