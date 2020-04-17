import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/Olympic2016Rio.csv')
df2 = pd.read_csv('../Datasets/Weather2014-15.csv')

app = dash.Dash()

# Bar chart data
barchart_df1 = df1
barchart_df1 = barchart_df1.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
barchart_df1 = barchart_df1.groupby(['NOC'])['Total'].sum().reset_index()
barchart_df1 = barchart_df1.sort_values(by=['Total'], ascending=[False]).head(20)
data_barchart = [go.Bar(x=barchart_df1['NOC'], y=barchart_df1['Total'])]

# Line Chart
line_df2 = df2
line_df2['date'] = pd.to_datetime(line_df2['date'])
data_linechart = [go.Scatter(x=line_df2['date'], y=line_df2['actual_mean_temp'], mode='lines', name='mean Temps')]

# Multi Line Chart
multiline_df2 = df2
multiline_df2['date'] = pd.to_datetime(multiline_df2['date'])
trace1_multiline = go.Scatter(x=multiline_df2['date'], y=multiline_df2['actual_min_temp'], mode='lines', name='min')
trace2_multiline = go.Scatter(x=multiline_df2['date'], y=multiline_df2['actual_max_temp'], mode='lines', name='max')
trace3_multiline = go.Scatter(x=multiline_df2['date'], y=multiline_df2['actual_mean_temp'], mode='lines',
                              name='mean')
data_multiline = [trace1_multiline, trace2_multiline, trace3_multiline]

# Bubble chart
# bubble_df2 = df2
# bubble_df2 = bubble_df2.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
# bubble_df2['Unrecovered'] = bubble_df2['Confirmed'] - bubble_df2['Deaths'] - bubble_df2['Recovered']
# data_bubblechart = [
#      go.Scatter(x=bubble_df2['date'],
#                 y=bubble_df2['average_Precipitation'],
#                 text=bubble_df2['day'],
#                 mode='markers',
#                 marker=dict(size=bubble_df2['average_Precipitation'] / 200, color=bubble_df2['average_Precipitation'] / 200, showscale=True))
#  ]

# Heatmap
data_heatmap = [go.Heatmap(x=df2['day'],
                           y=df2['month'],
                           z=df2['actual_mean_temp'].values.tolist(),
                           colorscale='Jet')]

# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Div('Aggregated data from the Rio 2016 Olympics and Weather Data from 2014 and 2015.', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bar Chart', style={'color': '#df2e56'}),
    html.Div('This bar chart represents the number of total olympic medals earned by the top 20 countries.'),
    dcc.Graph(id='graph1',
              figure={
                  'data': data_barchart,
                  'layout': go.Layout(title='Top 20 countries, sorted by total medal count. ',
                                      xaxis={'title': 'Countries'}, yaxis={'title': 'Number of total medals'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df2e56'}),
    html.Div('This line chart represent the mean temperature in the given period.'),
    dcc.Graph(id='graph4',
           figure={
               'data': data_linechart,
               'layout': go.Layout(title='Mean temperatures over time',
                                       xaxis={'title': 'Date'}, yaxis={'title': 'Temperature'})
               }
               ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Multi Line chart', style={'color': '#df2e56'}),
    html.Div(
        'This line chart represents temperature highs and lows in the given period.'),
    dcc.Graph(id='graph5',
              figure={
                  'data': data_multiline,
                  'layout': go.Layout(
                      title='Temperature averages',
                      xaxis={'title': 'Date'}, yaxis={'title': 'Temperature'})
              }
              ),
    # html.Hr(style={'color': '#7FDBFF'}),
    # html.H3('Bubble chart', style={'color': '#df2e56'}),
    # html.Div(
    #     'This bubble chart represent the Corona Virus recovered and under treatment of all reported countries except China.'),
    # dcc.Graph(id='graph6',
    #           figure={
    #               'data': data_bubblechart,
    #               'layout': go.Layout(title='Corona Virus Confirmed Cases',
    #                                   xaxis={'title': 'Recovered Cases'}, yaxis={'title': 'under Treatment Cases'},
    #                                   hovermode='closest')
    #           }
    #           ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Heat map', style={'color': '#df2e56'}),
    html.Div(
        'This heat map represent the mean temperature per day of week and month.'),
    dcc.Graph(id='graph7',
              figure={
                  'data': data_heatmap,
                  'layout': go.Layout(title='Temperature over the year',
                                      xaxis={'title': 'Day of Week'}, yaxis={'title': 'Month'})
              }
              )
])

# @app.callback(Output('graph1', 'figure'),
#               [Input('select-continent', 'value')])
# def update_figure(selected_continent):
#     filtered_df2 = df2[df2['Continent'] == selected_continent]
#
#     filtered_df2 = filtered_df2.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
#     new_df2 = filtered_df2.groupby(['Country'])['Confirmed'].sum().reset_index()
#     new_df2 = new_df2.sort_values(by=['Confirmed'], ascending=[False]).head(20)
#     data_interactive_barchart = [go.Bar(x=new_df2['Country'], y=new_df2['Confirmed'])]
#     return {'data': data_interactive_barchart,
#             'layout': go.Layout(title='Corona Virus Confirmed Cases in ' + selected_continent,
#                                 xaxis={'title': 'Country'},
#                                 yaxis={'title': 'Number of confirmed cases'})}

if __name__ == '__main__':
    app.run_server()