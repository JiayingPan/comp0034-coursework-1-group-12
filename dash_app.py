# Copied from the Dash tutorial documentation at https://dash.plotly.com/layout on 24/05/2021
# Import section modified 10/10/2021 to comply with changes in the Dash library.

# Run this app with `python dash_app.py` and visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import datetime
import dash_daq as daq
from dash import dcc
from dash import html
from dash import Output, Input
from datetime import date
from airdata import RecyclingData
from chart import RecyclingChart

# Prepare the data set
data = RecyclingData()
area = ''
start = '2021-1-1'
end = '2021-12-31'
data.process_data_for_area(area, start, end)
# Create the figures
rc = RecyclingChart(data)
airtype_list = ['PM2.5', 'PM10']
airtype = 'PM2.5'
fig_rc = rc.create_chart(area, airtype)


external_stylesheets = [dbc.themes.MINTY]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame see https://plotly.com/python/px-arguments/ for more options
app.layout = html.Div([
    html.Br(),
    # First row here
    dbc.Row(dbc.Col(children=[
        html.H1('Open Air Quality'),
        html.P('PM2.5 & PM10',
               className='lead')
    ])),
    dcc.Tabs(children=[
        dcc.Tab(label='Daily Matters', children=[
                dbc.Row([
                    dbc.Col(width=4, children=[
                        html.H5('Select Date'),
                        dcc.DatePickerSingle(
                            id='my-date-picker-single',
                            min_date_allowed=date(2021, 1, 1),
                            max_date_allowed=date(2021, 12, 31),
                            initial_visible_month=date(2021, 1, 1),
                            date=date(2021, 1, 1)
                        ),
                        html.H5("Select Area"),
                        dcc.Dropdown(id="area-select_d",
                                     options=[{"label": x, "value": x}
                                              for x in data.area_list],
                                     value="London"),
                        html.H5("Select Particular Matter"),
                        dcc.Dropdown(id="matter-select_d",
                                     options=[{"label": x, "value": x}
                                              for x in airtype_list],
                                     value="PM2.5"),
                    ]),
                    dbc.Col(children=[
                        html.Div(id='card')
                    ]),
                ])
                ]),
        dcc.Tab(label='Past Data', children=[
                dbc.Row([
                    # This is for the London area selector and the statistics panel.
                    dbc.Col(children=[
                        html.H5('Select Period'),
                        dcc.DatePickerRange(
                            id='my-date-picker-range',
                            min_date_allowed=date(2021, 1, 1),
                            max_date_allowed=date(2021, 12, 31),
                            initial_visible_month=date(2021, 1, 1),
                            start_date=date(2021, 1, 1),
                            end_date=date(2021, 12, 31)
                        ),
                    ]),
                    dbc.Col(children=[
                        html.H5("Select Area"),
                        dcc.Dropdown(id="area-select_p",
                                     options=[{"label": x, "value": x}
                                              for x in data.area_list],
                                     value=""),
                    ]),
                    dbc.Col(children=[
                        html.H5("Select Particular Matter"),
                        dcc.Dropdown(id="matter-select_p",
                                     options=[{"label": x, "value": x}
                                              for x in airtype_list],
                                     value="PM2.5"),
                    ]),
                    dcc.Graph(id='recycle-chart', figure=fig_rc)
                    # Add the second column here. This is for the figure.
                ])
                ]),
        dcc.Tab(label='Tab three', children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [2, 4, 3],
                            'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [5, 4, 3],
                         'type': 'bar', 'name': u'Montréal'},
                    ]
                }
            )
        ]),
    ])
])


@ app.callback(
    Output("recycle-chart", "figure"),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
    Input("area-select_p", "value"),
    Input("matter-select_p", "value"),
)
def update_output(start_date, end_date, area_select, matter_select):
    if start_date and area_select and matter_select is not None:
        data.process_data_for_area(
            area_select, start_date, end_date)
    fig_rc = rc.create_chart(area_select, matter_select)
    return fig_rc


@app.callback(
    Output('card', 'children'),
    Input('my-date-picker-single', 'date'),
    Input("area-select_d", "value"),
    Input("matter-select_d", "value")
)
def update_output(date_value, area, matter):
    if date_value and area and matter is not None:
        date_object = date.fromisoformat(date_value)
        date_string = date_object.strftime('%B %d, %Y')
        data.process_data_for_single_day(area, date_value)
        ####
        card = dbc.Card(className="card border-light mb-3", children=[
            dbc.CardBody([
                dbc.Col(width=4, children=[
                    html.H4(area, id="card-name", className="card-title"),
                    html.Br(),
                    daq.Gauge(id='chart',
                              color={"gradient": True, "ranges": {
                                  "green": [0, 12], "yellow":[12, 35], "red":[35, 55]}},
                        value=data.day_data[matter].mean(),
                        label=matter,
                        max=100,
                        min=0,
                              ),
                ]),
                dbc.Col(children=[
                    html.H6("Maximum"+matter, className="card-title"),
                    html.H4(data.day_data[matter].max(),
                        className="card-text text-dark"),
                    html.H6("Minimum"+matter, className="card-title"),
                    html.H4(data.day_data[matter].min(),
                        className="card-text text-dark"),
                    html.H6("Mean", className="card-title"),
                    html.H4("{:,.0f}".format(
                        data.day_data[matter].mean()), className="card-text text-dark"),
                ]),
            ]),
        ])
        return card


if __name__ == '__main__':
    app.run_server(debug=True)
