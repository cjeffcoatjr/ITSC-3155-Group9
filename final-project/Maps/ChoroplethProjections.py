import plotly.graph_objects as go
import pandas as pd
from Data import ProjectionsCalc as projections
import json

# use the json to build the dataframe
weekly_df = pd.read_json(json.dumps(projections.weekly))
monthly_df = pd.read_json(json.dumps(projections.monthly))

# format the labelling for the map
for col in weekly_df.columns:
    weekly_df[col] = weekly_df[col].astype(str)
for col in monthly_df.columns:
    monthly_df[col] = monthly_df[col].astype(str)
weekly_df['text'] = 'Total Projected Cases Tomorrow: ' + weekly_df['casesTomorrow'] + '<br>' + \
                    'Total Projected Cases in 14 days: ' + weekly_df['casesIn14'] + '<br>' + \
                    'Total Projected Cases in 30 days: ' + weekly_df['casesIn30'] + '<br>' + \
                    'Total Projected Deaths Tomorrow: ' + weekly_df['deathsTomorrow'] + '<br>' + \
                    'Total Projected Deaths in 14 days: ' + weekly_df['deathsIn14'] + '<br>' + \
                    'Total Projected Deaths in 30 days: ' + weekly_df['deathsIn30']
monthly_df['text'] = 'Total Projected Cases Tomorrow: ' + monthly_df['casesTomorrow'] + '<br>' + \
                     'Total Projected Cases in 14 days: ' + monthly_df['casesIn14'] + '<br>' + \
                     'Total Projected Cases in 30 days: ' + monthly_df['casesIn30'] + '<br>' + \
                     'Total Projected Deaths Tomorrow: ' + monthly_df['deathsTomorrow'] + '<br>' + \
                     'Total Projected Deaths in 14 days: ' + monthly_df['deathsIn14'] + '<br>' + \
                     'Total Projected Deaths in 30 days: ' + monthly_df['deathsIn30']

# draw the map
weekly_fig = go.Figure(data=go.Choropleth(
    locations=weekly_df['state'],
    z=weekly_df['casesTomorrow'].astype(int),
    locationmode='USA-states',
    colorscale='Reds',
    autocolorscale=False,
    text=weekly_df['text'],  # hover text
    marker_line_color='white',  # line markers between states
    colorbar_title="Cases Tomorrow"
))
weekly_fig.update_layout(
    geo=dict(
        scope='usa',
        projection=go.layout.geo.Projection(type='albers usa'),
        showlakes=False),
)
monthly_fig = go.Figure(data=go.Choropleth(
    locations=monthly_df['state'],
    z=monthly_df['casesTomorrow'].astype(int),
    locationmode='USA-states',
    colorscale='Reds',
    autocolorscale=False,
    text=monthly_df['text'],  # hover text
    marker_line_color='white',  # line markers between states
    colorbar_title="Cases Tomorrow"
))
monthly_fig.update_layout(
    geo=dict(
        scope='usa',
        projection=go.layout.geo.Projection(type='albers usa'),
        showlakes=False),
)
