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

fig = go.Figure(data=go.Choropleth(
    locations=df['state'],
    z=df['cases'].astype(int),
    locationmode='USA-states',
    colorscale='Reds',
    autocolorscale=False,
    text=df['deaths'],  # hover text
    marker_line_color='white',  # line markers between states
    colorbar_title="Infected"
))

fig.update_layout(
    geo=dict(
        scope='usa',
        projection=go.layout.geo.Projection(type='albers usa'),
        showlakes=False,  # lakes
        lakecolor='rgb(0, 0, 255)'),
)


def get_fig():
    return fig


fig.show()
