import dash
from Data import Choropleth as data
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()  # instate the dashboard
interactive_map = data.get_fig()  # From the data, pull a plotly object

# Layout
app.layout = html.Div(children=[
    html.H1(children='Interactive Dashboard',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('A Python Dashboard for COVID-19 Visualization using Plotly', style={'textAlign': 'center'}),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('This interactive map visualizes COVID-19 impact across the United States of America and Wyoming.',
            style={'color': '#df2e56'}),
    dcc.Graph(id='COVID-19 in the United States of America and Wyoming', figure=interactive_map)
])
app.run_server()
