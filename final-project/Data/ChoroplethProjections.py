import plotly.graph_objects as go
import requests
import pandas as pd  # Load data frame and tidy it.
from Data import ProjectionsCalcRework as projections

weekly_df = pd.read_json(projections.weekly)
monthly_df = pd.read_json(projections.monthly)

for col in weekly_df.columns:
    weekly_df[col] = weekly_df[col].astype(str)

for col in monthly_df.columns:
    monthly_df[col] = monthly_df[col].astype(str)

weekly_df['text'] = 'Total Projected Cases Tomorrow: ' + weekly_df['cases'] + '<br>' + \
             'Total Deaths: ' + weekly_df['deaths']

fig = go.Figure(data=go.Choropleth(
    locations=df['state'],
    z=df['cases'].astype(int),
    locationmode='USA-states',
    colorscale='Reds',
    autocolorscale=False,
    text=df['text'],  # hover text
    marker_line_color='white',  # line markers between states
    colorbar_title="Cases"
))

fig.update_layout(
    geo=dict(
        scope='usa',
        projection=go.layout.geo.Projection(type='albers usa'),
        showlakes=False),
)


def get_fig():
    return fig
