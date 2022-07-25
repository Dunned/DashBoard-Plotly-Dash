from turtle import title
import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd
import numpy as np


datos = np.random.randint(5, 15, 20)

print(datos)

data = [go.Box(y=datos)]

layout = go.Layout(title="Box Plot")

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename="BoxPlot.html")
