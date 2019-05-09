import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

# Boostrap CSS.
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})  # noqa: E501

app.layout = html.Div(
    html.Div([
        html.Div([
            html.H1(children='Dashboard',
                    className='nine columns'),
            html.Div(children='Our DashBoard for Decision Support System ',
                        className='nine columns')
        ] ,  className="row"
        ),

        
        html.Div([

            html.Div([

                dcc.Graph(
                    id='example-graph',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'project 1'},
                            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'project 2'},
                        ],
                        'layout': {
                            'title': 'Feature 01',
                            'xaxis' : dict(
                                title='x Axis',
                                titlefont=dict(
                                family='Courier New, monospace',
                                size=20,
                                color='#7f7f7f'
                            )),
                            'yaxis' : dict(
                                title='y Axis',
                                titlefont=dict(
                                family='Helvetica, monospace',
                                size=20,
                                color='#7f7f7f'
                            ))
                        }
                    }
                )

            ], className='six columns'
            ),
        

                html.Div([
                dcc.Graph(
                    id='example-graph-2',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'project 1'},
                            {'x': [1, 2, 3], 'y': [2, 9, 8], 'type': 'line', 'name': 'project 2'},
                        ],
                        'layout': {
                            'title': 'Feature 02'
                        }
                    }
                )
                ],  className='six columns'
                )
        ], className="row"
        ),


        html.Div([           
            
            html.Div([
                dcc.Graph(
                    id='example-graph3',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [7, 1, 6], 'type': 'line', 'name': 'project 1'},
                            {'x': [1, 2, 3], 'y': [2, 3, 8], 'type': 'line', 'name': 'project 2'},
                        ],
                        'layout': {
                            'title': 'Feature 03',
                            'xaxis' : dict(
                                title='x Axis',
                                titlefont=dict(
                                family='Courier New, monospace',
                                size=20,
                                color='#7f7f7f'
                            )),
                            'yaxis' : dict(
                                title='y Axis',
                                titlefont=dict(
                                family='Helvetica, monospace',
                                size=20,
                                color='#7f7f7f'
                            ))
                        }
                    }
                )
            ], className= 'six columns'
            ),    
                    

                html.Div([
                dcc.Graph(
                    id='example-graph 3',
                    figure={
                        'data': [
                            {'x': [1, 2, 3], 'y': [5, 1, 2], 'type': 'bar', 'name': 'project 1'},
                            {'x': [1, 2, 3], 'y': [1, 2, 5], 'type': 'bar', 'name': 'project 2'},
                        ],
                        'layout': {
                            'title': 'Feature 04',
                            'xaxis' : dict(
                                title='x Axis',
                                titlefont=dict(
                                family='Courier New, monospace',
                                size=20,
                                color='#7f7f7f'
                            )),
                            'yaxis' : dict(
                                title='y Axis',
                                titlefont=dict(
                                family='Helvetica, monospace',
                                size=20,
                                color='#7f7f7f'
                            ))
                        }
                    }
                )
                ], className= 'six columns'
                )


        ], className="row"
        )
]    
)
)
if __name__ == '__main__':
    app.run_server(debug=True)
