from dash import html, dcc
from dash.dependencies import Input, Output
import dash
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import dash_bootstrap_components as dbc  # Import dash-bootstrap-components
from app import app

# Load your data
csv_file = 'data/LocalPayNYC.csv'
data = pd.read_csv(csv_file)

# Dash app layout
layout = dbc.Container([  # Use dbc.Container for responsive design
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

# Callback to update the box plot and bar plot
@app.callback(
    [Output('comparison-chart-box', 'figure'),
     Output('comparison-chart-bar', 'figure')],
    Input('comparison-factor', 'value')
)
def update_plots(selected_factor):
    # Create box plots for pay by ethnicity, race, and gender
    fig_box = plt.figure(figsize=(10, 6))
    sns.boxplot(x=selected_factor, y='upper_pay_band_bound', data=data)
    plt.title(f'Pay Distribution by {selected_factor}')
    plt.xticks(rotation=45)

    # Create bar plots for job categories by ethnicity, race, and gender
    fig_bar = plt.figure(figsize=(10, 6))
    sns.countplot(x=selected_factor, hue='job_category', data=data)
    plt.title(f'Distribution of Job Categories by {selected_factor}')
    plt.xticks(rotation=45)

    return fig_box, fig_bar

if __name__ == '__main__':
    app.run_server(debug=True)
