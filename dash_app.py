# Copied from the Dash tutorial documentation at https://dash.plotly.com/layout on 24/05/2021
# Import section modified 10/10/2021 to comply with changes in the Dash library.

# Run this app with `python dash_app.py` and visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
from dash import Output, Input

from airdata import RecyclingData
from chart import RecyclingChart

# Prepare the data set
data = RecyclingData()
area = 'Camden - Bloomsbury'
data.process_data_for_area(area)
# Create the figures
rc = RecyclingChart(data)
fig_rc = rc.create_chart(area)


external_stylesheets = [dbc.themes.MINTY]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame see https://plotly.com/python/px-arguments/ for more options


app.layout = dbc.Container(fluid=True, children=[
    html.Br(),
    # First row here
    dbc.Row(dbc.Col(children=[
        html.H1('Open Air Quality'),
        html.P('PM2.5 & PM10',
           className='lead')
    ])),
    # Second row here
    dbc.Row([
        # This is for the London area selector and the statistics panel.
        dbc.Col(width=3, children=[
            html.H4("Select Area"),
            dcc.Dropdown(id="area-select",
             options=[{"label": x, "value": x} for x in data.area_list],
             value="Camden - Bloomsbury"),
        ]),
        # Add the second column here. This is for the figure.
        dbc.Col(width=9, children=[
            html.H2('Air Quality'),
            dcc.Graph(id='recycle-chart', figure=fig_rc)
        ]),
    ]),
])


@app.callback(
    Output("recycle-chart", "figure"),
    [Input("area-select", "value")])
def render_output_panel(area_select):
    data.process_data_for_area(area_select)
    fig_rc=rc.create_chart(area_select)
    return  fig_rc

if __name__ == '__main__':
    app.run_server(debug = True)
