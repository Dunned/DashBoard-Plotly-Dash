import plotly.offline as pyo
import plotly.graph_objects as go
from plotly import subplots
import pandas as pd


df = pd.read_csv('/Users/eduardo/Desktop/Proyectos/Plotly-Dash/Datasets/3.12/Temperatura_horaria.csv',
                 delimiter=";", encoding='ISO-8859-1')
df_iris = pd.read_csv('/Users/eduardo/Desktop/Proyectos/Plotly-Dash/Datasets/3.2/iris_dataset.csv',
                      encoding='iso-8859-1', delimiter=',')

trace1 = go.Heatmap(x=df['Día'], y=df['Hora'], z=df['T_prom'].values.tolist())
trace2 = go.Scatter(x=df_iris['longitud_sépalo'],
                    y=df_iris['anchura_sépalo'],
                    mode="markers")

fig = subplots.make_subplots(rows=1, cols=2, subplot_titles=['HeatMap', 'Scatterplot'],
                             shared_xaxes=False)

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)

pyo.plot(fig, filename="Subplots")
