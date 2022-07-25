import plotly.offline as pyo
import plotly.graph_objects as go
from plotly import subplots
import pandas as pd


df = pd.read_csv('/Users/eduardo/Desktop/Proyectos/Plotly-Dash/Datasets/3.12/Temperatura_horaria.csv',
                 delimiter=";", encoding='ISO-8859-1')

# print(df.head(5))

data = [go.Heatmap(x=df['Día'], y=df['Hora'],
        z=df['T_prom'].values.tolist(), colorscale='Jet')]

layout = go.Layout(title='HeadMap')

figura = go.Figure(data=data, layout=layout)

pyo.plot(figura, filename="HeatMap.html")
