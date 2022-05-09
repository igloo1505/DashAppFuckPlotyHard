from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from state.settings import style

def sliderSwitcher(df, dfKey, step, extraSliderStyles={}):
    html.Div(
    [
        dbc.RadioItems(
            id="slider-switcher-select",
            className="btn-group",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "Range", "value": "Range"},
                {"label": "Single Value", "value": "Value"},
            ],
            value=1,
        ),
         html.Div(dcc.Slider(
        df[dfKey].min(),
        df[dfKey].max(),
        step=None,
        id='switchable-slider',
        value=df[dfKey].max(),
        marks={str(j): str(j) for j in df[dfKey].unique()}
    ), style=extraSliderStyles)
    ],
    className="radio-group",
    )

    
    