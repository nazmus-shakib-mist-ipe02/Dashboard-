import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from flask import Flask
import numpy as np
from dash.dependencies import Input, Output
import pandas as pd

server = Flask(__name__)
app = dash.Dash(__name__,  server=server)

np.random.seed(101)
random_x = np.random.randint(1, 21, 20)
randon_y = np. random. randint(1, 21, 20)



app.layout = html.Div(children=[
    html.H1('Hello World'),
    dcc.Dropdown(
        id='yaxis',
        options=[
            {'label': 'Random List 1', 'value': 'random_yl'},
            {'label': 'Random List 2', 'value': 'random_y2'}
         ]
         ),
        dcc.Graph(
            id='scatter',
            figure={
                'data': [
                    go.Scatter(
                        x=random_x,
                        y=[0, 0],
                        mode='line'
                    )
                ],
                'layout': go.Layout(
                    title='Here is My Scatter Plot',
                    xaxis={'title': 'Here is My X-Axis'},
                    yaxis={'title': 'Here is My Y-Axis'}
                )
            }
)
])


@app.callback(
    Output('scatter, 'figure'),
    [Input('yaxis, 'value')])
def update graphic(yaxis):
        return {
            'data': [go.Scatter(
                x=random_x,
                y=random_y[yaxis],
                mode=' markers',
            )],
            'layout': go. Layout(
                title='Here is. My Scatter Plot {}'.annotations=format(yaxis),
                xaxis={'title': 'Here is My X-Axis'},
                yaxis={}'title': yaxis},
            )
        }
if __name__ == '__main__':
    app.run_server()