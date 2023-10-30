import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from tabs import demographic
import dash_bootstrap_components as dbc
from tabs import demographic, geographic, psycographic

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Careers influenced by various factors over the years"),
    
    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='Geographic', value='tab-1'),
        dcc.Tab(label='Psycographic', value='tab-2'),
        dcc.Tab(label='Demographic', value='tab-3'),
    ]),
    
    html.Div(id='tab-content'),
])

@app.callback(
    Output('tab-content', 'children'),
    Input('tabs', 'value'),
)
def render_content(tab):
    if tab == 'tab-1':
        
        return geographic.layout
    elif tab == 'tab-2':
       
        return psycographic.layout
    elif tab == 'tab-3':
       
        return demographic.layout

if __name__ == '__main__':
    app.run_server(debug=True)
