import plotly.graph_objects as go
import requests
import pandas as pd  # Load data frame and tidy it.
from Data import States as states

response = requests.get("https://corona.lmao.ninja/v2/states")
if response.status_code == 200:
    stateDict = response.text
    statesList = states.stateList
    states = states.states
  #  statesList = states.statesList
    i = 0
    for el in statesList:
        itm = states[el]
        print(i)
        i = i + 1
        stateDict = stateDict.replace(el, itm)



else:
    print("error, server responded with status code of" + str(response.status_code))
    exit(-1)
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')
df = pd.read_json(stateDict)

# states = states.states
# i = 0
# for el in df:
#     if el in states.keys():
#         print(i)
#         i = i + 1
#         el = states.get(el)
# for col in df.columns:
#     df[col] = df[col].astype(str)

# df['text'] = df['state'] + '<br>' + \
#     'Beef ' + df['beef'] + ' Dairy ' + df['dairy'] + '<br>' + \
#     'Fruits ' + df['total fruits'] + ' Veggies ' + df['total veggies'] + '<br>' + \
#     'Wheat ' + df['wheat'] + ' Corn ' + df['corn']

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
    # title_text='Covid-19 In the United States and Wyoming',
    geo=dict(
        scope='usa',
        projection=go.layout.geo.Projection(type='albers usa'),
        showlakes=False,  # lakes
        lakecolor='rgb(0, 0, 255)'),
)


def get_fig():
    return fig


fig.show()
