import dash
import dash_labs as dl
import dash_bootstrap_components as dbc
from components.Sidebar import sidebar
from components.Navbar import Navbar
mathjax = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML'


app = dash.Dash(
    __name__, 
    plugins=[dl.plugins.pages],
    external_stylesheets=[dbc.themes.CYBORG]
)





app.layout = dbc.Container(
    [sidebar(), Navbar(), dl.plugins.page_container],
    fluid=True,
)


app.scripts.append_script({ 'external_url' : mathjax })
app.config.suppress_callback_exceptions = True

if __name__ == "__main__":
    app.run_server(debug=True)