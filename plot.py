import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
import numpy as np

X = deque(maxlen=20)
X.append(1)

Y = deque(maxlen=20)
Y.append(1)

Z = deque(maxlen=20)
Z.append(1)

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1000,
            n_intervals=0
        ),
    ]
)


@app.callback(
    Output('live-graph', 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def update_graph_scatter(n):
    X.append(X[-1] + 1)
    Y.append(Y[-1] + Y[-1] * random.uniform(-0.1, 0.1))
    Z.append([random.uniform(-1, 1) for _ in range(20)])
    
    print(x, y,)

    data = [
        go.Surface(
            x=list(X),
            y=list(range(20)),
            z=list(Z),
            colorscale='Viridis',
            showscale=False
        ),
    ]

    return {
        'data': data,
        'layout': go.Layout(
            title='Live 2D Surface Map',
            scene=dict(
                xaxis=dict(title='X'),
                yaxis=dict(title='Y'),
                zaxis=dict(title='Z'),
            ),
            autosize=True,
            margin=dict(l=65, r=50, b=65, t=90),
        )
    }


if __name__ == '__main__':
    app.run_server()
