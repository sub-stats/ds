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
import pandas as pd
from plotly.graph_objs import *

from app import app, server

def submissions_per_day(subreddit="askreddit"):
    df = pd.read_csv('https://raw.githubusercontent.com/sub-stats/ds/master/past_90_days_post_per_day.csv')

    df = df[df['subreddit'] == subreddit]

    layout = Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )


    fig = go.Figure(layout=layout)
    fig.add_trace(go.Scatter(x=df['date'], y=df['posts_count'],
                        mode='lines',
                        name='lines',
                        line_shape='spline'
                        ))


    fig.update_layout(
        title=go.layout.Title(
            text="Posts per Day Over Time",
            xref="paper",
            x=0.5

        ),
        xaxis=go.layout.XAxis(
            title=go.layout.xaxis.Title(
                text="Date",
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="#FF4500"
                )
            )
        ),
        yaxis=go.layout.YAxis(
            title=go.layout.yaxis.Title(
                text="Posts per Day",
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="#FF4500"
                )
            )
        )
    )
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=False, zeroline=False)

    return fig

def comments_per_day(subreddit='askreddit'):
    df = pd.read_csv('https://raw.githubusercontent.com/sub-stats/ds/master/past_90_days_comments_per_day.csv')


    df = df[df['subreddit'] == subreddit]


    ##Can do it this way to display all subs on 1 graph
    # fig = px.line(df, x='date', y='posts_count', color='subreddit', template="plotly_dark",
    #     line_shape="spline")

    layout = Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )


    fig = go.Figure(layout=layout)
    fig.add_trace(go.Scatter(x=df['date'], y=df['comments_count'],
                        mode='lines',
                        name='lines',
                        line_shape='spline'
                        ))


    fig.update_layout(
        title=go.layout.Title(
            text="Comments per Day Over Time",
            xref="paper",
            x=0.5

        ),
        xaxis=go.layout.XAxis(
            title=go.layout.xaxis.Title(
                text="Date",
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="#FF4500"
                )
            )
        ),
        yaxis=go.layout.YAxis(
            title=go.layout.yaxis.Title(
                text="Comments per Day",
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="#FF4500"
                )
            )
        )
    )

    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=False, zeroline=False)

    return fig

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Graph(id='graph')
])

@app.callback(Output('graph', 'figure'),
              [Input('url', 'pathname'), Input('url', 'search')])
def display_graph(pathname, search):
    queries_list = []
    query_dict = {}
    if search != None:
        queries = search[1:]
        print(queries)
        if queries.find('&') > 0:
            queries_list = queries.split('&')
            
            if len(queries_list) > 0:
                for i in range(len(queries_list)):
                    new_item = queries_list[i].split('=')
                    print('adding item')
                    query_dict[new_item[0]] = new_item[1]
        else:
            print('one item')
            new_item = queries.split('=')
            query_dict[new_item[0]] = new_item[1]
        print(query_dict)
    if pathname != None:
        split_path = pathname.split('/')
        graph_name = split_path[1]
        if len(split_path) > 2:
            subreddit = split_path[2]
            print(subreddit)
            if graph_name == 'submissions-per-day':
                return submissions_per_day(subreddit)
            elif graph_name == 'comments-per-day':
                return comments_per_day(subreddit)
        if graph_name == 'submissions-per-day':
            return submissions_per_day()
        elif graph_name == 'comments-per-day':
            return comments_per_day()

if __name__ == '__main__':
    app.run_server(debug=True)
