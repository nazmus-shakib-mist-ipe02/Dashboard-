import dash
from dash.dependencies import Input, Output
import dash_html_co
mponents as html
import dash_core_components as dcc
from collections import defaultdict
import pandas as pd
import json
from json import dumps, loads, JSONEncoder, JSONDecoder
import pickle

df =pd.read_csv(‘https://gist.githubusercontent.com/jbrav/f281e0063418dd62ad63004671cf96ec/raw/bab2df8189cd39099eaf4ecceb82cbf37762dc99/coma.csv 3’)
dataframe=json.loads(df.to_json())

print df
app = dash.Dash()
app.config.suppress_callback_exceptions=True

available_funds = df[‘FUNDS’].unique()

app.layout = html.Div([
html.Div([
html.Div([
html.H1(‘Evolucion rentabilidades’),
dcc.Checklist(
id=‘mychecklist’,
options= [{‘label’: i, ‘value’: i} for i in available_funds]),
dcc.Graph(id=‘mygraph1’)
]),
html.Div([
html.H1(‘Evolucion 2’),
dcc.Checklist(
id=‘mychecklist2’,
options=[{‘label’: i, ‘value’: i} for i in available_funds]),
dcc.Graph(id=‘mygraph2’)
]),

    html.Div([
       html.H1('Evolucion 3'),
       dcc.Checklist(
           id='mychecklist3',
           options=[{'label': i, 'value': i} for i in available_funds]),
       dcc.Graph(id='mygraph3')
       ]),
])])

@app.callback(
dash.dependencies.Output(‘mygraph1’,‘figure’), [dash.dependencies.Input(‘mychecklist’, ‘value’)])
def update_graph(selected_checklist_value):
dff = df[df[‘Year’] == hoverData[‘points’][0][‘customdata’]]
dff = dff[dff[‘FUNDS’] == yaxis_column_name]
return figure(dff, yaxis_column_name)

if name == ‘main’:
app.run_server(debug=True, port=7896)