import plotly.graph_objects as go
import pandas as pd
from Data import BaseData as data

df = pd.read_json(data.stateDict)

for col in df.columns:
    df[col] = df[col].astype(str)

df['text'] = 'Total Cases: ' + df['cases'] + ', New Cases Today: ' + df['todayCases'] + '<br>' + \
             'Total Deaths: ' + df['deaths'] + ', New Deaths Today: ' + df['todayDeaths'] + '<br>' + \
             'Active Cases: ' + df['active'] + '<br>' + \
             'Tests Performed: ' + df['tests'] + ', Tests Per 1 Million People: ' + df['testsPerOneMillion']

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
