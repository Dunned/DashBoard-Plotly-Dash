from fileinput import filename
import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv('/Users/eduardo/Desktop/Proyectos/Plotly-Dash/Datasets/3.4/Ventas.csv',
                 encoding='iso-8859-1', delimiter=';')


data1 = go.Scatter(x=df['Fecha'], y=df['Total Venta Classic Cars'],
                   mode='lines', name='Ventas Carros')

data2 = go.Scatter(x=df['Fecha'], y=df['Total Venta Motorcycles'],
                   mode='lines', name='Ventas Trucks')

datos = [data1, data2]


layout = go.Layout(title='Ventas Comprativo',
                   xaxis=dict(title='Ventas'),
                   yaxis=dict(title='Fecha')
                   )

fig = go.Figure(data=datos, layout=layout)

pyo.plot(fig, filename='Ejercicio.html')
