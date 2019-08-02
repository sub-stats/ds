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


def get_url(source):
    url = {'post_day':'https://raw.githubusercontent.com/sub-stats/ds/master/past_90_days_post_per_day.csv', 
           'comment_day':'https://raw.githubusercontent.com/sub-stats/ds/master/past_90_days_comments_per_day.csv',
           'post_week':'https://raw.githubusercontent.com/sub-stats/ds/master/posts_by_day_of_week.csv',
           'post_hour':'https://raw.githubusercontent.com/sub-stats/ds/master/posts_by_hour.csv',
           'comment_post':'https://raw.githubusercontent.com/sub-stats/ds/master/comments_per_post.csv',
           'users_day':'https://raw.githubusercontent.com/sub-stats/ds/master/past_90_days_unique_users_per_day.csv'
          }
    return url[source]


def get_data(subreddit, start, end, source):
    # Iterate over file in small chunks to save memory and select relevent sub
    iter_csv = pd.read_csv(get_url(source), iterator=True, chunksize=100)
    df = pd.concat([chunk[chunk['subreddit'] == subreddit] for chunk in iter_csv])

    df['date'] = pd.to_datetime(df['date'])
    df = df[(df['date'] > start) & (df['date'] < end)]

    return df


def get_fig(graph_options, labels=('title','x_label','y_label'), source, need_days=False):
    df = get_data(graph_options['subreddit'], graph_options['start'], graph_options['end'], source)

    fig = go.Figure(layout=Layout(paper_bgcolor='rgba(0,0,0,0)',
                                  plot_bgcolor='rgba(0,0,0,0)'))

    # X and Y in the df must be in column positions 0 and 1
    fig.add_trace(go.Scatter(x=df.iloc[:, 0], y=df.iloc[:, 1],
                             mode='lines',
                             name='lines',
                             line_shape='spline',
                             line=dict(color='#24A0ED', width=12)
                             ))

    fig.update_layout(
        title=go.layout.Title(
            text=labels[0],
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
                text=labels[1],
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="#FF4500"
                )
            )
        ),
        yaxis=go.layout.YAxis(
            title=go.layout.yaxis.Title(
                text=labels[2],
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

    if need_days:
        fig.update_xaxes(
            ticktext=["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"],
            tickvals=[0, 1, 2, 3, 4, 5, 6],
        )

    return fig


def plotlyfromjson(fpath):
    """Render a plotly figure from a json file"""
    with urllib.request.urlopen(fpath) as url:
        v = json.loads(url.read().decode())

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

        if queries.find('&') > 0:
            queries_list = queries.split('&')

            if len(queries_list) > 0:
                for i in range(len(queries_list)):
                    new_item = queries_list[i].split('=')
                    query_dict[new_item[0]] = new_item[1]

        elif len(queries) > 1:
            new_item = queries.split('=')
            query_dict[new_item[0]] = new_item[1]
        

    if pathname != None:
        if pathname == '/submissions-per-day':
            return get_fig(query_dict, ('Posts per Day Over Time', 'Date', 'Posts per Day'), 'post_day')
        elif pathname == '/comments-per-day':
            return get_fig(query_dict, ('Comments per Day Over Time', 'Date', 'Comments per Day'), 'comment_day')
        elif pathname == '/day-of-week':
            return get_fig(query_dict, ('Posts by Day of Week (UTC)', 'Date', 'Posts'), 'post_week', True)
        elif pathname == '/hour-of-day':
            return get_fig(query_dict, ('Posts by Time of Day (UTC)', 'Hour of Day', 'Posts'), 'post_hour')
        elif pathname == '/comments-per-post':
            return get_fig(query_dict, ('Average Comments Per Post', 'Date', 'Comments Per Post'), 'comment_post')
        elif pathname == '/unique-users-per-day':
            return get_fig(query_dict, ('Unique Users Per Day', 'Date', 'Unique Users'), 'users_day')
        elif pathname == '/subreddit-similarity':
            return plotlyfromjson('https://raw.githubusercontent.com/sub-stats/ds/master/network_graph.json')


if __name__ == '__main__':
    app.run_server(debug=True)