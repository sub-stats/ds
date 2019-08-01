import plotly as py
from plotly.graph_objs import *
import urllib.request
import json 

def plotlyfromjson(fpath):
    """Render a plotly figure from a json file"""
    with urllib.request.urlopen(fpath) as url:
        v = json.loads(url.read().decode())

    return v['data']

fig=Figure(data=plotlyfromjson('https://raw.githubusercontent.com/sub-stats/ds/master/network_graph.json'))
fig.show()

if __name__ == '__main__':
    app.run_server(debug=True)
