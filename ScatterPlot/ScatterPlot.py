# IMPORTANDO LIBRERIAS

from fileinput import filename
import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

df_iris = pd.read_csv('/Users/eduardo/Desktop/Proyectos/Plotly-Dash/Datasets/3.2/iris_dataset.csv',
                      encoding='iso-8859-1', delimiter=',')

print(df_iris.head())

data = [go.Scatter(x=df_iris['longitud_sépalo'],
                   y=df_iris['anchura_sépalo'],
                   mode="markers")]


layout = go.Layout(title="Grafico de Scatter Plot",
                   xaxis=dict(title="Longitud Sépalo"),
                   yaxis=dict(title="Anchura Sepalo")
                   )

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='Plot_iris.html')
