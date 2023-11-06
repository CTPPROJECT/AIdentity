import dash
import dash_core_components as dcc
import pandas as pd
import plotly.express as px

from dash import html
from dash.dependencies import Input, Output


csv_file = "data/LocalPayNYC.csv"
data = pd.read_csv(csv_file)

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Dropdown(
            id="comparison-factor",
            options=[
                {"label": "Gender", "value": "gender"},
                {"label": "Ethnicity", "value": "ethnicity"},
                {"label": "Race", "value": "race"},
            ],
            value="gender",
        ),
        dcc.Graph(id="comparison-chart-box"),
        dcc.Graph(id="comparison-chart-bar"),
    ]
)


@app.callback(
    [
        Output("comparison-chart-box", "figure"),
        Output("comparison-chart-bar", "figure"),
    ],
    [Input("comparison-factor", "value")],
)
def update_plots(selected_factor):
    fig_box = px.box(
        data,
        x=selected_factor,
        y="upper_pay_band_bound",
        title=f"Pay Distribution by {selected_factor}",
    )

    fig_bar = px.histogram(
        data,
        x=selected_factor,
        color="job_category",
        title=f"Distribution of Job Categories by {selected_factor}",
    )

    return fig_box, fig_bar


if __name__ == "__main__":
    app.run_server(debug=True)