import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__, suppress_callback_exceptions=True)

# COMBINED DATA SECTION
###################################################
# add all data here and initialize with your initials
data_visualize_K = pd.read_csv('data/LocalPayNYC.csv')
data_visualize_B = pd.read_csv('data/emotionalEmployment.csv')

###################################################
# DATA SECTION ENDS

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
    # HENRY'S SECTION
    ###################################################################################################
    if tab == 'geographic':
        # Return the content for the "Geographic" tab
        return html.Div("Content for Geographic tab")

    # BRENDAN'S SECTION
    ####################################################################################################
    elif tab == 'psycographic':
        # Return the content for the "Psycographic" tab
        return dbc.Container([
            dbc.Row([
                dbc.Col([
                    dcc.Dropdown(
                        id='psych-factor',
                        options=[
                            {'label': 'Agreeableness', 'value': '_agreeableness'},
                            {'label': 'Conscientiousness', 'value': '_conscientiousness'},
                            {'label': 'Emotional Stability', 'value': '_emotional_stability'},
                            {'label': 'Extroversion', 'value': '_extroversion'},
                            {'label': 'Openness', 'value': '_openness'}
                        ],
                        value='_agreeableness',  # Default selection
                    ),
                ], width=3),
            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='psych-chart-box1'),
                    # dcc.Graph(id='psych-chart-box2'),
                    # dcc.Graph(id='psych-chart-box3'),
                    # dcc.Graph(id='psych-chart-box4'),
                    # dcc.Graph(id='psych-chart-box5')
                ], width=6),
                dbc.Col([
                    dcc.Graph(id='psych-chart-bar'),
                ], width=6),
            ]),
        ])

# KASAF'S SECTION
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
#############Kasaf section end 


##Brendan functions
##Brendan we all need to put all our callbacks and functions right in the end here. 
@app.callback(
    # Output('psych-chart-box1', 'figure'),
#      Output('psych-chart-box2', 'figure'),
#      Output('psych-chart-box3', 'figure'),
#      Output('psych-chart-box4', 'figure'),
#      Output('psych-chart-box5', 'figure'),
     Output('psych-chart-bar', 'figure'),
    Input('psych-factor', 'value')
)
def update_plots(selected_factor):
    # fig_box1 = px.box(
    #     data_visualize_B,
    #     x=selected_factor, ## you spelled 'agreableness' which wasn't correct
    #     y='100-150k',
    #     title=f"{selected_factor} $50-100k",
    # ) ### there's something wrong with this one . i changed your y value btw. y need to be a column name in the dataset 
    fig_bar = px.histogram(
        data_visualize_B,
        x=selected_factor,
        color="_employment",
        title=f"Employment by {selected_factor}",
    )

    return fig_bar

 

if __name__ == '__main__':
    app.run_server(debug=True)




# @app.callback(
#     [Output('psych-chart-box1', 'figure'),
# #      Output('psych-chart-box2', 'figure'),
# #      Output('psych-chart-box3', 'figure'),
# #      Output('psych-chart-box4', 'figure'),
# #      Output('psych-chart-box5', 'figure'),
#      Output('psych-chart-bar', 'figure')],
#     [Input('psych-factor', 'value')]
# )
# def update_plots2(selected_factor):
#     fig_box1 = px.box(
#         data_visualize_B,
#         x=selected_factor,
#         y='_50-100k',
#         title=f"{selected_factor} $50-100k",
#     )

#     fig_box2 = px.box(
#         data_visualize_B,
#         x=selected_factor,
#         y='_100-150k',
#         title=f"{selected_factor} $100-150k",
#     )

    # fig_box3 = px.box(
    #     data_visualize_B,
    #     x=selected_factor,
    #     y='_150-200k',
    #     title=f"{selected_factor} $150-200k",
    # )

    # fig_box4 = px.box(
    #     data_visualize_B,
    #     x=selected_factor,
    #     y='_200-500k',
    #     title=f"{selected_factor} $200-500k",
    # )

    # fig_box5 = px.box(
    #     data_visualize_B,
    #     x=selected_factor,
    #     y='_+500k',
    #     title=f"{selected_factor} $500k+",
    # )

    # fig_bar = px.histogram(
    #     data_visualize_B,
    #     x=selected_factor,
    #     color="_employment",
    #     title=f"Employment by {selected_factor}",
    # )

    # return figbox1, fig_bar

    # return [fig_box1, fig_box2, fig_box3, fig_box4, fig_box5, fig_bar]