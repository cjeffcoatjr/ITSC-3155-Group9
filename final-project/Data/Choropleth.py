import plotly.graph_objects as go
import requests
import pandas as pd  # Load data frame and tidy it.
from Data import States as states

response = requests.get("https://corona.lmao.ninja/v2/states")
if response.status_code == 200:
    stateDict = response.text
    for state in states.stateList:
        abbrev = states.states[state]
        stateDict = stateDict.replace(state, abbrev)
    stateDict = stateDict.replace("West VA", "WV")  # Fix some funsies
else:
    print("Error, server responded with status code of " + str(response.status_code))
    exit(-1)
df = pd.read_json(stateDict)
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


def get_fig():
    return fig
