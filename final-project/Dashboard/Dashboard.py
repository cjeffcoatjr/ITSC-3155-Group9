import dash
import plotly.graph_objects as go
from Data import Choropleth as data
from Data import ChoroplethProjections as projections
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()  # instate the dashboard

interactive_map = data.get_fig()  # From the data, pull a plotly object
weekly_interactive_projections = projections.get_weekly_fig()  # And again
monthly_interactive_projections = projections.get_monthly_fig()  # And one more time

df = data.get_df()  # From the data, pull the df
weekly_df = projections.get_weekly_df()  # And again
monthly_df = projections.get_monthly_df()  # And one more time

# Layout
app.layout = html.Div(children=[
    html.H1(children='Interactive Dashboard',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('A Python Dashboard for COVID-19 Visualization using Plotly',
             style={'textAlign': 'center', 'height': '80px'}, ),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('This interactive map visualizes COVID-19 impact across the United States of America and Wyoming.',
            style={'color': '#df2e56'}),
    dcc.Graph(id='map', figure=interactive_map, ),
    html.Br(),
    html.Div("Data Options", id="data-options"),
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
    ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('This interactive map visualizes possible future COVID-19 impact across the United States of America and '
            'Wyoming based on calculations made using the growth rate over the past week.',
            style={'color': '#df2e56'}),
    dcc.Graph(id='weekly-map', figure=weekly_interactive_projections, ),
    html.Br(),
    html.Div("Data Options", id="weekly-data-options"),
    dcc.Dropdown(
        id='select-weekly-data',
        options=[
            {'label': 'Cases Tomorrow', 'value': 'casesTomorrow'},
            {'label': 'Cases in 14 days', 'value': 'casesIn14'},
            {'label': 'Cases in 30 days', 'value': 'casesIn30'},
            {'label': 'Deaths Tomorrow', 'value': 'deathsTomorrow'},
            {'label': 'Deaths in 14 days', 'value': 'deathsIn14'},
            {'label': 'Deaths in 30 days', 'value': 'deathsIn30'}
        ],
        value='casesTomorrow'
    ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('This interactive map visualizes possible future COVID-19 impact across the United States of America and '
            'Wyoming based on calculations made using the growth rate over the past month.',
            style={'color': '#df2e56'}),
    dcc.Graph(id='monthly-map', figure=monthly_interactive_projections, ),
    html.Br(),
    html.Div("Data Options", id="monthly-data-options"),
    dcc.Dropdown(
        id='select-monthly-data',
        options=[
            {'label': 'Cases Tomorrow', 'value': 'casesTomorrow'},
            {'label': 'Cases in 14 days', 'value': 'casesIn14'},
            {'label': 'Cases in 30 days', 'value': 'casesIn30'},
            {'label': 'Deaths Tomorrow', 'value': 'deathsTomorrow'},
            {'label': 'Deaths in 14 days', 'value': 'deathsIn14'},
            {'label': 'Deaths in 30 days', 'value': 'deathsIn30'}
        ],
        value='casesTomorrow'
    )

])


@app.callback(
    dash.dependencies.Output('map', 'figure'),
    [dash.dependencies.Input('select-data', 'value')])
def update_output_a(value):
    fig = go.Figure(data=go.Choropleth(
        locations=df['state'],
        z=df[value].astype(int),
        locationmode='USA-states',
        colorscale='Reds',
        autocolorscale=False,
        text=df['text'],  # hover text
        marker_line_color='white',  # line markers between states
        colorbar_title=value

    ), )
    fig.update_layout(
        geo=dict(
            scope='usa',
            projection=go.layout.geo.Projection(type='albers usa'),
            showlakes=False),

    )

    return fig


@app.callback(
    dash.dependencies.Output('weekly-map', 'figure'),
    [dash.dependencies.Input('select-weekly-data', 'value')])
def update_output_b(value):
    fig = go.Figure(data=go.Choropleth(
        locations=weekly_df['state'],
        z=weekly_df[value].astype(int),
        locationmode='USA-states',
        colorscale='Reds',
        autocolorscale=False,
        text=weekly_df['text'],  # hover text
        marker_line_color='white',  # line markers between states
        colorbar_title=value

    ), )
    fig.update_layout(
        geo=dict(
            scope='usa',
            projection=go.layout.geo.Projection(type='albers usa'),
            showlakes=False),

    )

    return fig


@app.callback(
    dash.dependencies.Output('monthly-map', 'figure'),
    [dash.dependencies.Input('select-monthly-data', 'value')])
def update_output_b(value):
    fig = go.Figure(data=go.Choropleth(
        locations=monthly_df['state'],
        z=monthly_df[value].astype(int),
        locationmode='USA-states',
        colorscale='Reds',
        autocolorscale=False,
        text=monthly_df['text'],  # hover text
        marker_line_color='white',  # line markers between states
        colorbar_title=value

    ), )
    fig.update_layout(
        geo=dict(
            scope='usa',
            projection=go.layout.geo.Projection(type='albers usa'),
            showlakes=False),

    )

    return fig


app.run_server()
