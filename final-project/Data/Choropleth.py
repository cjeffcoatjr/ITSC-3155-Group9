import plotly.graph_objects as go
import requests
import pandas as pd  # Load data frame and tidy it.
from Data import States as states

response = requests.get("https://corona.lmao.ninja/v2/states")
if response.status_code == 200:
    stateDict = response.text
    statesList = states.stateList
    states = states.states
    i = 0
    for el in statesList:
        itm = states[el]
        stateDict = stateDict.replace(el, itm)
    stateDict = stateDict.replace("West VA", "WV")  # Fix some funsies


else:
    print("error, server responded with status code of" + str(response.status_code))
    exit(-1)
df = pd.read_json(stateDict)

df['text'] = df['state'] + '<br>' + \
    'Total Cases: ' + str(df['cases']) + ', New Cases Today: ' + str(df['todayCases']) + '<br>' + \
    'Total Deaths: ' + str(df['deaths']) + ', New Deaths Today: ' + str(df['todayDeaths']) + '<br>' + \
    'Active Cases: ' + str(df['active']) + '<br>' + \
    'Tests Performed: ' + str(df['tests']) + ', Tests Per 1 Million People: ' + str(df['testsPerOneMillion'])

fig = go.Figure(data=go.Choropleth(
    locations=df['state'],
    z=df['cases'].astype(int),
    locationmode='USA-states',
    colorscale='Reds',
    autocolorscale=False,
    text=df['text'],  # hover text
    marker_line_color='white',  # line markers between states
    colorbar_title="Infected"
))

fig.update_layout(
    geo=dict(
        scope='usa',
        projection=go.layout.geo.Projection(type='albers usa'),
        showlakes=False),
)


def get_fig():
    return fig


fig.show()
