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

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(
    'https://raw.githubusercontent.com/sub-stats/ds/master/posts_by_day_of_week.csv')


df = df[df['subreddit'] == "askreddit"]


##Can do it this way to display all subs on 1 graph
# fig = px.line(df, x='date', y='posts_count', color='subreddit', template="plotly_dark",
#     line_shape="spline")

layout = Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)


fig = go.Figure(layout=layout)
fig.add_trace(go.Scatter(x=df['day'], y=df['posts_count'],
                    mode='lines',
                    name='lines',
                    line_shape='spline'
                    ))


fig.update_layout(
    title=go.layout.Title(
        text="Posts by Day of Week (UTC)",
        xref="paper",
        x=0.5

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

fig.update_xaxes(showgrid=False, zeroline=False)
fig.update_yaxes(showgrid=False, zeroline=False)

fig.update_xaxes(
    ticktext=["Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"],
    tickvals=[0, 1, 2, 3, 4, 5, 6],
)

fig.show()




if __name__ == '__main__':
    app.run_server(debug=True)
