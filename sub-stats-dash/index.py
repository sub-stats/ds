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
import urllib
import json

from app import app, server
def submissions_per_day(graph_options):
    subreddit = graph_options['subreddit']
    start = graph_options['start']
    end = graph_options['end']
    df = pd.read_csv('https://raw.githubusercontent.com/sub-stats/ds/master/past_90_days_post_per_day.csv')

    df = df[df['subreddit'] == subreddit]
    df['date'] = pd.to_datetime(df['date'])
    df = df[(df['date'] > start) & (df['date'] < end)]

    layout = Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    fig = go.Figure(layout=layout)
    fig.add_trace(go.Scatter(x=df['date'], y=df['posts_count'],
                        mode='lines',
                        name='lines',
                        line_shape='spline',
                        line=dict(color='#24A0ED', width=12)
                        ))

    fig.update_layout(
        title=go.layout.Title(
            text="Posts per Day Over Time",
            xref="paper",
            x=0.5,
            font=dict(
            family="Courier New, monospace",
            size=18,
            color="#FF4500"
            )

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
    fig.update_xaxes(showgrid=True, gridcolor='white', zeroline=False, showline=True,
                linewidth=1, linecolor='black')

    fig.update_yaxes(showgrid=True, gridcolor='white', zeroline=False, showline=True,
                linewidth=1, linecolor='black')

    return fig

def comments_per_day(graph_options):
    df = pd.read_csv('https://raw.githubusercontent.com/sub-stats/ds/master/past_90_days_comments_per_day.csv')

    subreddit = graph_options['subreddit']
    start = graph_options['start']
    end = graph_options['end']

    print(subreddit)
    print(start)

    df = df[df['subreddit'] == subreddit]

    df['date'] = pd.to_datetime(df['date'])
    df = df[(df['date'] > start) & (df['date'] < end)]
    print(df.shape)
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
                        line_shape='spline',
                        line=dict(color='#24A0ED', width=12)
                        ))


    fig.update_layout(
        title=go.layout.Title(
            text="Comments per Day Over Time",
            xref="paper",
            x=0.5,
            font=dict(
            family="Courier New, monospace",
            size=18,
            color="#FF4500"
            )

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

    fig.update_xaxes(showgrid=True, gridcolor='white', zeroline=False, showline=True,
                    linewidth=1, linecolor='black')

    fig.update_yaxes(showgrid=True, gridcolor='white', zeroline=False, showline=True,
                    linewidth=1, linecolor='black')

    return fig



def day_of_week(graph_options):
    subreddit = graph_options['subreddit']

    df = pd.read_csv('https://raw.githubusercontent.com/sub-stats/ds/master/posts_by_day_of_week.csv')

    df = df[df['subreddit'] == subreddit]

    #df = df[(df['date'] > start) & (df['date'] < end)]

    layout = Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)


    fig = go.Figure(layout=layout)
    fig.add_trace(go.Scatter(x=df['day'], y=df['posts_count'],
                        mode='lines',
                        name='lines',
                        line_shape='spline',
                        line=dict(color='#24A0ED', width=12)
                        ))


    fig.update_layout(
        title=go.layout.Title(
            text="Posts by Day of Week (UTC)",
            xref="paper",
            x=0.5,
            font=dict(
            family="Courier New, monospace",
            size=18,
            color="#FF4500"
            )

        ),
        xaxis=go.layout.XAxis(
            title=go.layout.xaxis.Title(
                text="Day of Week",
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="#FF4500"
                )
            )
        ),
        yaxis=go.layout.YAxis(
            title=go.layout.yaxis.Title(
                text="Posts",
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="#FF4500"
                )
            )
        )
    )

    fig.update_xaxes(showgrid=True, gridcolor='white', zeroline=False, showline=True,
                    linewidth=1, linecolor='black')

    fig.update_yaxes(showgrid=True, gridcolor='white', zeroline=False, showline=True,
                    linewidth=1, linecolor='black')

    fig.update_xaxes(
        ticktext=["Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"],
        tickvals=[0, 1, 2, 3, 4, 5, 6],
    )

    return fig

def hour_of_day(graph_options):
    subreddit = graph_options['subreddit']

    df = pd.read_csv('https://raw.githubusercontent.com/sub-stats/ds/master/posts_by_hour.csv')

    df = df[df['subreddit'] == subreddit]

    #df = df[(df['date'] > start) & (df['date'] < end)]

    layout = Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)


    fig = go.Figure(layout=layout)
    fig.add_trace(go.Scatter(x=df['hour'], y=df['doc_count'],
                        mode='lines',
                        name='lines',
                        line_shape='spline',
                        line=dict(color='#24A0ED', width=12)
                        ))


    fig.update_layout(
        title=go.layout.Title(
            text="Posts by Time of Day (UTC)",
            xref="paper",
            x=0.5,
            font=dict(
            family="Courier New, monospace",
            size=18,
            color="#FF4500"
            )

        ),
        xaxis=go.layout.XAxis(
            title=go.layout.xaxis.Title(
                text="Hour of Day",
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="#FF4500"
                )
            )
        ),
        yaxis=go.layout.YAxis(
            title=go.layout.yaxis.Title(
                text="Posts",
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="#FF4500"
                )
            )
        )
    )

    fig.update_xaxes(showgrid=True, gridcolor='white', zeroline=False, showline=True,
                    linewidth=1, linecolor='black')

    fig.update_yaxes(showgrid=True, gridcolor='white', zeroline=False, showline=True,
                    linewidth=1, linecolor='black')

    return fig

def comments_per_post(graph_options):
    subreddit = graph_options['subreddit']
    start = graph_options['start']
    end = graph_options['end']

    df = pd.read_csv('https://raw.githubusercontent.com/sub-stats/ds/master/comments_per_post.csv')

    df = df[df['subreddit'] == subreddit]
    df['date'] = pd.to_datetime(df['date'])
    df = df[(df['date'] > start) & (df['date'] < end)]

    layout = Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    fig = go.Figure(layout=layout)
    fig.add_trace(go.Scatter(x=df['date'], y=df['comments_per_post'],
                        mode='lines',
                        name='lines',
                        line_shape='spline',
                        line=dict(color='#24A0ED', width=12)
                        ))


    fig.update_layout(
        title=go.layout.Title(
            text="Average Comments Per Post",
            xref="paper",
            x=0.5,
            font=dict(
            family="Courier New, monospace",
            size=18,
            color="#FF4500"
            )

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
                text="Comments Per Post",
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="#FF4500"
                )
            )
        )
    )

    fig.update_xaxes(showgrid=True, gridcolor='white', zeroline=False, showline=True,
                    linewidth=1, linecolor='black')

    fig.update_yaxes(showgrid=True, gridcolor='white', zeroline=False, showline=True,
                    linewidth=1, linecolor='black')

    return fig

def unique_users_per_day(graph_options):
    df = pd.read_csv('https://raw.githubusercontent.com/sub-stats/ds/master/past_90_days_unique_users_per_day.csv')

    subreddit = graph_options['subreddit']
    start = graph_options['start']
    end = graph_options['end']

    # print(subreddit)
    # print(start)

    df = df[df['subreddit'] == subreddit]

    df['date'] = pd.to_datetime(df['date'])
    df = df[(df['date'] > start) & (df['date'] < end)]
    # print(df.shape)
    ##Can do it this way to display all subs on 1 graph
    # fig = px.line(df, x='date', y='posts_count', color='subreddit', template="plotly_dark",
    #     line_shape="spline")

    layout = Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    fig = go.Figure(layout=layout)
    fig.add_trace(go.Scatter(x=df['date'], y=df['unique_users'],
                        mode='lines',
                        name='lines',
                        line_shape='spline',
                        line=dict(color='#24A0ED', width=12)
                        ))


    fig.update_layout(
        title=go.layout.Title(
            text="Unique Users Per Day",
            xref="paper",
            x=0.5,
            font=dict(
            family="Courier New, monospace",
            size=18,
            color="#FF4500"
            )

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
                text="Unique Users",
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="#FF4500"
                )
            )
        )
    )

    fig.update_xaxes(showgrid=True, gridcolor='white', zeroline=False, showline=True,
                    linewidth=1, linecolor='black')

    fig.update_yaxes(showgrid=True, gridcolor='white', zeroline=False, showline=True,
                    linewidth=1, linecolor='black')

    return fig

def plotlyfromjson(fpath):
    """Render a plotly figure from a json file"""
    with urllib.request.urlopen(fpath) as url:
        v = json.loads(url.read().decode())

    # v['data']
    for i in range(2, len(v['data'])):
        v['data'][i]['x'] = [0]
        v['data'][i]['y'] = [0]
    layout = Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )

    fig=Figure(data=v['data'],
        layout=layout)

    fig.update_xaxes(showline=True, linewidth=1, linecolor='black')
    fig.update_yaxes(showline=True, linewidth=1, linecolor='black')
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
        elif len(queries) > 1:
            print('one item')
            new_item = queries.split('=')
            query_dict[new_item[0]] = new_item[1]
        print(query_dict)
    if pathname != None:
        if pathname == '/submissions-per-day':
            return submissions_per_day(query_dict)
        elif pathname == '/comments-per-day':
            return comments_per_day(query_dict)
        elif pathname == '/day-of-week':
            return day_of_week(query_dict)
        elif pathname == '/hour-of-day':
            return hour_of_day(query_dict)
        elif pathname == '/comments-per-post':
            return comments_per_post(query_dict)
        elif pathname == '/subreddit-similarity':
            return plotlyfromjson('https://raw.githubusercontent.com/sub-stats/ds/master/network_graph.json')
        elif pathname == '/unique-users-per-day':
            return unique_users_per_day(query_dict)

if __name__ == '__main__':
    app.run_server(debug=True)