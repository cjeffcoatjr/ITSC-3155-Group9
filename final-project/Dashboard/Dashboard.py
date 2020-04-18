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
    dcc.Graph(id='COVID-19 in the United States of America and Wyoming', figure=interactive_map),
    html.Div("Data Options"),
    dcc.Dropdown(
        id='select-data',
        options=[
            {'label': 'Cases', 'value': 'cases'},
            {'label': 'Deaths', 'value': 'deaths'},
            {'label': 'Cases Today', 'value': 'todayCases'},
            {'label': 'Deaths Today', 'value': 'todayDeaths'},
            {'label': 'Active Cases', 'value': 'active'},
            {'label': 'Tests', 'value': 'tests'},
            {'label': 'Tests Per Million', 'value': 'testsPerOneMillion'}
        ],
        value='cases'
    )

])
app.run_server()
