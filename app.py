import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


app = dash.Dash(__name__, suppress_callback_exceptions=True)

#COMBINED DATA SECTION
###################################################
#add all data here and initilize with you initials
csv_file_K = 'data/LocalPayNYC.csv'
data_visualize_K = pd.read_csv(csv_file_K)

###################################################
#DATA SECTION ENDS

app.layout = html.Div([
    html.H1("Careers influenced by various factors over the years"),
    
    dcc.Tabs(id='tabs', value='geographic', children=[
        dcc.Tab(label='Geographic', value='geographic'),
        dcc.Tab(label='Psycographic', value='psycographic'),
        dcc.Tab(label='Demographic', value='demographic'),
    ]),
    
    html.Div(id='tab-content'),
])

@app.callback(
    Output('tab-content', 'children'),
    Input('tabs', 'value')
)
def render_content(tab):
#HENRY'S SECTION
###################################################################################################
    if tab == 'geographic':
        # Return the content for the "Geographic" tab
        return html.Div("Content for Geographic tab")

#BRENDAN'S SECTION
####################################################################################################
    elif tab == 'psycographic':
        # Return the content for the "Psycographic" tab
        return html.Div("Content for Psycographic tab")

#KASAF'S SECTION
#####################################################################################################
    elif tab == 'demographic':
        # Return the content for the "Demographic" tab
        
        return dbc.Container([
            dbc.Row([
                dbc.Col([
                    dcc.Dropdown(
                        id='comparison-factor',
                        options=[
                            {'label': 'Gender', 'value': 'gender'},
                            {'label': 'Ethnicity', 'value': 'ethnicity'},
                            {'label': 'Race', 'value': 'race'}
                        ],
                        value='gender',  # Default selection
                    ),
                ], width=3),
            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='comparison-chart-box'),
                ], width=6),
                dbc.Col([
                    dcc.Graph(id='comparison-chart-bar'),
                ], width=6),
            ]),
        ])

@app.callback(
    [Output('comparison-chart-box', 'figure'),
     Output('comparison-chart-bar', 'figure')],
    Input('comparison-factor', 'value')
)
def update_plots(selected_factor):
    fig_box = px.box(
        data_visualize_K,
        x=selected_factor,
        y="upper_pay_band_bound",
        title=f"Pay Distribution by {selected_factor}",
    )

    fig_bar = px.histogram(
        data_visualize_K,
        x=selected_factor,
        color="job_category",
        title=f"Distribution of Job Categories by {selected_factor}",
    )

    return fig_box, fig_bar


###########################################################################################
#Kasaf's section ends here


if __name__ == '__main__':
    app.run_server(debug=True)
