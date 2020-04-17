import dash
from Data import ChoroplethEx as data
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()  # instate the dashboard

# From the data, pull a plotly object
interactive_map = data.init

