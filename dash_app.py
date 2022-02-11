# Copied from the Dash tutorial documentation at https://dash.plotly.com/layout on 24/05/2021
# Import section modified 10/10/2021 to comply with changes in the Dash library.

# Run this app with `python dash_app.py` and visit http://127.0.0.1:8050/ in your web browser.
import math
from datetime import date
import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_daq as daq
from dash import dcc
from dash import html
from dash import Output, Input
from airdata import RecyclingData
from chart import RecyclingChart

# Prepare the data set
data = RecyclingData()
area = ''
start = '2021-1-1'
end = '2021-12-31'
data.process_data_for_area(area, start, end)

# Create the figures

# First map showing the location of cities (mapbox)

df = pd.read_csv("Data/min-max-avg.csv")
# Add your mapbox token here
mapbox_token = "pk.eyJ1Ijoic3RlcGhhbmllMDYyNSIsImEiOiJja3plcDl3NTQwa2xoMzFtcXdtMGx4Z3U4In0.HJZkpBQj0blh5xUoXXR-VA"
fig_mapbox = go.Figure()
fig_mapbox.add_trace(
    go.Scattermapbox(lat=df["Latitude"], lon=df["Longitude"], text=df["Location"],
                     marker=go.scattermapbox.Marker(size=12, color='rgb(255, 0, 0)', opacity=0.7),
                     mode='markers+text', textposition="top center")),

fig_mapbox.add_trace(
    go.Scattermapbox(lat=df["Latitude"], lon=df["Longitude"],
                     marker=go.scattermapbox.Marker(size=6, color='rgb(242, 177, 172)', opacity=0.7),
                     mode='markers', hoverinfo=None)),

fig_mapbox.update_layout(
    width=450, height=410, margin=dict(l=20, r=0, t=25, b=0),
    hovermode='closest', showlegend=False,
    mapbox=dict(accesstoken=mapbox_token,
                center=dict(lat=53.479489, lon=-2.245115), zoom=4.5))

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
        html.H1('Open Air Quality', style={'text-align': 'center'}),
        html.P('Particular matters monitoring dashboard',
               className='lead', style={'text-align': 'center'})
    ])),
    dcc.Tabs(children=[

        dcc.Tab(label='View Locations', children=[

            dbc.Row([
                # This is for the London area selector and the statistics panel.
                dbc.Col(width=6, children=[
                    html.Br(),
                    #html.H5("scatter mapbox"),
                    html.H5('View air quality in various cities in UK:'),
                    html.Br(),
                    dcc.Graph(id='scatter-map', figure=fig_mapbox),
                ]),
                # ]),

                # Add the second column here. This is for the figure.
                dbc.Col(width=6, children=[
                    html.Br(),
                    #html.H5('heat map'),
                    # Second row here
                    dbc.Row([
                        dbc.Col([
                            html.H5('Select date for heat map:'),
                        ]),
                        dbc.Col([
                            dcc.DatePickerSingle(id='map-date-picker-single',
                                                 min_date_allowed=date(
                                                     2021, 1, 1),
                                                 max_date_allowed=date(
                                                     2021, 12, 31),
                                                 initial_visible_month=date(
                                                     2021, 1, 1),
                                                 date=date(2021, 1, 1)
                                                 ),
                        ]),
                        html.Div(
                            id='output-container-date-picker-single', children=[]),
                        html.Br(),
                        dcc.Graph(id='mapbox-heatmap', figure={}),
                    ]),
                ]),
            ]), ]),


        dcc.Tab(label='Daily Matters', children=[
                dbc.Row([
                    dbc.Col(width=4, children=[
                        html.Br(),
                        dbc.Row([
                            html.H6('Select Date'),
                            dcc.DatePickerSingle(
                                id='my-date-picker-single',
                                min_date_allowed=date(2021, 1, 1),
                                max_date_allowed=date(2021, 12, 31),
                                initial_visible_month=date(2021, 1, 1),
                                date=date(2021, 1, 1)
                            ),
                        ]),
                        html.Br(),
                        dbc.Row([
                            html.H6("Select Area"),
                            dcc.Dropdown(id="area-select_d",
                                         options=[{"label": x, "value": x}
                                                  for x in data.area_list],
                                         value="London"),
                        ]),
                        html.Br(),
                        html.Div(id='comment', className="text-info")

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
                        html.Br(),
                        html.H6('Select Period'),
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
                        html.Br(),
                        html.H6("Select Area"),
                        dcc.Dropdown(id="area-select_p",
                                     options=[{"label": x, "value": x}
                                              for x in data.area_list],
                                     value=""),
                    ]),
                    dbc.Col(children=[
                        html.Br(),
                        html.H6("Select Particular Matter"),
                        dcc.Dropdown(id="matter-select_p",
                                     options=[{"label": x, "value": x}
                                              for x in airtype_list],
                                     value="PM2.5"),
                    ]),
                    dcc.Graph(id='recycle-chart', figure=fig_rc)
                ])
                ]),
    ])
])


# Second map showing the AQI of cities (heat map)
@app.callback(
    [Output(component_id='output-container-date-picker-single', component_property='children'),
     Output(component_id='mapbox-heatmap', component_property='figure')],
    [Input('map-date-picker-single', component_property='date')])
def update_map(date_slctd):
    container = ''
    #"You have selected the date: {}".format(date_slctd)
    dff = df.copy()
    dff = dff[dff["utc"] == date_slctd]
    fig_heatmap = px.density_mapbox(
        data_frame=dff,
        # template='plotly_dark',
        lat='Latitude',
        lon='Longitude',
        z='Total (avg)',
        radius=20,
        range_color=[0, 55],
        center=dict(lat=53.479489, lon=-2.245115),
        zoom=4.5,
        mapbox_style='stamen-watercolor')
    fig_heatmap.update_layout(width=450, height=400,
                              margin=dict(l=0, r=10, t=10, b=0),)
    return container, fig_heatmap


@app.callback(
    Output('card', 'children'),
    Input('my-date-picker-single', 'date'),
    Input("area-select_d", "value"),
)
def update_card(date_value_card, area_card):
    if date_value_card and area_card is not None:
        data.process_data_for_single_day(area_card, date_value_card)
        ####
        card = dbc.Card(className="card border-light mb-3", children=[
            dbc.CardBody([
                dbc.Row([
                    html.H4(area_card, id="card-name", className="card-title"),
                    html.Br(),
                    dbc.Col(width=6, children=[
                        daq.Gauge(id='chart1',
                                  color={"gradient": True, "ranges": {
                                      "green": [0, 12], "yellow":[12, 35], "red":[35, 55]}},
                                  value=data.day_data['PM2.5'].mean(),
                                  label='PM2.5',
                                  max=80,
                                  min=0,
                                  ),
                        html.H6("Maximum PM2.5", className="card-title"),
                        html.H4(data.day_data['PM2.5'].max(),
                                className="card-text text-dark"),
                        html.H6("Minimum PM2.5", className="card-title"),
                        html.H4(data.day_data['PM2.5'].min(),
                                className="card-text text-dark"),
                        html.H6("Mean", className="card-title"),
                        html.H4("{:,.0f}".format(
                            data.day_data['PM2.5'].mean()), className="card-text text-dark"),
                    ]),

                    dbc.Col(width=6, children=[
                        daq.Gauge(id='chart2',
                                  color={"gradient": True, "ranges": {
                                      "green": [0, 12], "yellow": [12, 35], "red": [35, 55]}},
                                  value=data.day_data['PM10'].mean(),
                                  label='PM10',
                                  max=80,
                                  min=0,
                                  ),
                        html.H6("Maximum PM10", className="card-title"),
                        html.H4(data.day_data['PM10'].max(),
                                className="card-text text-dark"),
                        html.H6("Minimum PM10", className="card-title"),
                        html.H4(data.day_data['PM10'].min(),
                                className="card-text text-dark"),
                        html.H6("Mean", className="card-title"),
                        html.H4("{:,.0f}".format(
                            data.day_data['PM10'].mean()), className="card-text text-dark"),
                    ]),
                ]),
            ]),
        ])
        return card


@app.callback(
    Output('comment', 'children'),
    Input('my-date-picker-single', 'date'),
    Input("area-select_d", "value"),
)
def update_comment(date_value_comment, area_comment):
    if date_value_comment and area_comment is not None:
        data.process_data_for_single_day(area_comment, date_value_comment)

        if data.day_data['PM2.5'].mean() + data.day_data['PM10'].mean() < 20:
            return "The air is so good! Let's take a fresh walk!~"

        if 20 <= data.day_data['PM2.5'].mean() + data.day_data['PM10'].mean() < 40:
            return "Good air quality! What about going outside? "

        if 40 <= data.day_data['PM2.5'].mean() + data.day_data['PM10'].mean() < 60:
            return "Overall good quality. Slight pollutants in the air but don't worry about it!"

        if 60 <= data.day_data['PM2.5'].mean() + data.day_data['PM10'].mean() < 80:
            return "Ummm...Seems there is some pollution in the air. "

        if math.isnan(data.day_data['PM2.5'].mean() + data.day_data['PM10'].mean()):
            return "There is no data about this day."

        else:
            return "Be careful about the pollution, you can wear a mask to protect yourself!"



@ app.callback(
    Output("recycle-chart", "figure"),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
    Input("area-select_p", "value"),
    Input("matter-select_p", "value"),
)
def update_line_chart(start_date, end_date, area_select, matter_select):
    if start_date and area_select and matter_select is not None:
        data.process_data_for_area(
            area_select, start_date, end_date)
    fig_rc = rc.create_chart(area_select, matter_select)
    return fig_rc


if __name__ == '__main__':
    app.run_server(debug=True)
