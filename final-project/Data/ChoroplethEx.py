import plotly.graph_objects as go
import requests
import pandas as pd # Load data frame and tidy it.

response = requests.get("https://corona.lmao.ninja/v2/states")
if response.status_code == 200:
    stateDict = response.json()
else:
    print("error, server responded with status code of" + str(response.status_code))
    exit(-1)

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')
df = pd.read_json(stateDict)
fig = go.Figure(data=go.Choropleth(
    locations=df['code'], # Spatial coordinates
    z = df['total exports'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "Infected",
))

fig.update_layout(
    title_text = 'Covid-19 In the United States and Wyoming',
    geo_scope='usa', # limite map scope to USA
)

fig.show()