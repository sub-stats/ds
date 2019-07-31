import os
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

from app import app, server

def display_plot():
    df = pd.read_csv(
    'https://raw.githubusercontent.com/sub-stats/ds/master/past_90_days_post_per_day.csv')

    df = df[df['subreddit'] == 'askreddit']

    fig = px.line(df, x='date', y='posts_count')
    return fig

fig = display_plot()
app.layout = html.Div([
    dcc.Graph(id='submissions-per-day',
              figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)