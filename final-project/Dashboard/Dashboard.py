import dash
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from Data import Choropleth as data
import dash_core_components as dcc
import dash_html_components as html
from Data import Choropleth as chloropleth

app = dash.Dash()  # instate the dashboard
interactive_map = data.get_fig()  # From the data, pull a plotly object
df = chloropleth.df

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
    dcc.Graph(id='map', figure=interactive_map),
    html.Br(),
    html.Div("Data Options", id="dd-output-container"),
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


@app.callback(
    dash.dependencies.Output('map', 'figure'),
    [dash.dependencies.Input('select-data', 'value')])
def update_output(value):
    fig = go.Figure(data=go.Choropleth(
        locations=df['state'],
        z=df[value].astype(int),
        locationmode='USA-states',
        colorscale='Reds',
        autocolorscale=False,
        text=df['text'],  # hover text
        marker_line_color='white',  # line markers between states
        colorbar_title=value
        ))
    fig.update_layout(
        geo=dict(
            scope='usa',
            projection=go.layout.geo.Projection(type='albers usa'),
            showlakes=False),
        LAYOUT={'height': 150,
                'width': 800}
    )

    return fig


app.run_server()

