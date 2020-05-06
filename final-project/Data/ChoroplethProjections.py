import plotly.graph_objects as go
import pandas as pd  # Load data frame and tidy it.
from Data import ProjectionsCalcRework as projections

weekly_df = pd.read_json(projections.weekly)
monthly_df = pd.read_json(projections.monthly)

for col in weekly_df.columns:
    weekly_df[col] = weekly_df[col].astype(str)

for col in monthly_df.columns:
    monthly_df[col] = monthly_df[col].astype(str)

weekly_df['text'] = 'Total Projected Cases Tomorrow: ' + weekly_df['cases'][0] + '<br>' + \
                    'Total Projected Cases in 14 days: ' + weekly_df['cases'][1] + '<br>' + \
                    'Total Projected Cases in 30 days: ' + weekly_df['cases'][2] + '<br>' + \
                    'Total Projected Deaths Tomorrow: ' + weekly_df['deaths'][0] + '<br>' + \
                    'Total Projected Deaths in 14 days: ' + weekly_df['deaths'][0] + '<br>' + \
                    'Total Projected Deaths in 30 days: ' + weekly_df['deaths'][0]

monthly_df['text'] = 'Total Projected Cases Tomorrow: ' + monthly_df['cases'][0] + '<br>' + \
                     'Total Projected Cases in 14 days: ' + monthly_df['cases'][1] + '<br>' + \
                     'Total Projected Cases in 30 days: ' + monthly_df['cases'][2] + '<br>' + \
                     'Total Projected Deaths Tomorrow: ' + monthly_df['deaths'][0] + '<br>' + \
                     'Total Projected Deaths in 14 days: ' + monthly_df['deaths'][0] + '<br>' + \
                     'Total Projected Deaths in 30 days: ' + monthly_df['deaths'][0]

weekly_fig = go.Figure(data=go.Choropleth(
    locations=weekly_df['state'],
    z=weekly_df['cases'][0].astype(int),
    locationmode='USA-states',
    colorscale='Reds',
    autocolorscale=False,
    text=weekly_df['text'],  # hover text
    marker_line_color='white',  # line markers between states
    colorbar_title="Cases"
))

weekly_df.update_layout(
    geo=dict(
        scope='usa',
        projection=go.layout.geo.Projection(type='albers usa'),
        showlakes=False),
)

monthly_fig = go.Figure(data=go.Choropleth(
    locations=monthly_df['state'],
    z=monthly_df['cases'][0].astype(int),
    locationmode='USA-states',
    colorscale='Reds',
    autocolorscale=False,
    text=monthly_df['text'],  # hover text
    marker_line_color='white',  # line markers between states
    colorbar_title="Cases"
))

monthly_df.update_layout(
    geo=dict(
        scope='usa',
        projection=go.layout.geo.Projection(type='albers usa'),
        showlakes=False),
)


def get_weekly_fig():
    return weekly_fig


def get_monthly_fig():
    return monthly_fig
