# -*- coding: utf-8 -*-
import dash
import datetime
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio
from dash.dependencies import Input, Output
from plotly.graph_objs import *

#Code is basically exactly the same for comments over time



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(
    'https://raw.githubusercontent.com/sub-stats/ds/master/past_90_days_post_per_day.csv')


available_indicators = df['subreddit'].unique()

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='askreddit'
            ),

        ],style={'width': '48%', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic'),

])

@app.callback(
    Output('indicator-graphic', 'figure'),
    [
     Input('yaxis-column', 'value'),

     ])
def update_graph(yaxis_column_name
                 ):
    dff = df[df['subreddit'] == yaxis_column_name]

    return {
        'data': [go.Scatter(
            x=pd.to_datetime(dff['date']),
            y=dff['posts_count'],
            mode='lines',
            name='lines',
            line_shape='spline'
        )],
        'layout': go.Layout(
            xaxis={
                'title': "Date",
            },
            yaxis={
                'title': "Posts per Day",
            },

            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)
