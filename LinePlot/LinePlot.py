from fileinput import filename
import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('/Users/eduardo/Desktop/Proyectos/Plotly-Dash/Datasets/3.3/SP500_data_.csv',
                 encoding='iso-8859-1', delimiter=',')

# print(df.head())

data = go.Scatter(x=df['Date'], y=df['Open'],
                  mode='lines+markers', name='Apertura')
data1 = go.Scatter(x=df['Date'], y=df['Close'],
                   mode='lines+markers', name='Cierre')

datas = [data, data1]

layout = go.Layout(title="Grafico LinePlot",
                   xaxis=dict(title="Fecha"),
                   yaxis=dict(title="SP500 VALOR")
                   )

fig = go.Figure(data=datas, layout=layout)

pyo.plot(fig, filename="Line_plot.html")
