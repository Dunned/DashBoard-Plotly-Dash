from tracemalloc import start
import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd


df = pd.read_excel('/Users/eduardo/Desktop/Proyectos/Plotly-Dash/Datasets/3.9/Temperaturas.xlsx',
                   )


data = [
    go.Histogram(x=df['T_Promedio'], xbins=dict(
        start=0, end=40, size=5), histnorm="probability",
        cumulative_enabled=True)  # acumular anteriores
]

layout = go.Layout(title="Histograma")

figura = go.Figure(data=data, layout=layout)

pyo.plot(figura, filename="Histograma.html")
