# IMPORT LIBRERIAS
import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

df = pd.read_excel('/Users/eduardo/Desktop/Proyectos/Plotly-Dash/Datasets/3.5/Medallas_olímpicas.xlsx',
                   sheet_name="Sheet2")

# print(df.head(5))

df = df.sort_values(by='Total', ascending=False)


#data = [go.Bar(x=df['País'], y=df['Total'])]

trace0 = go.Bar(x=df['País'], y=df['Oro'], marker={
                "color": "#FFD700"}, name="Oro")

trace1 = go.Bar(x=df['País'], y=df['Plata'], marker={
                "color": "#C0C0C0"}, name="Plata")

trace2 = go.Bar(x=df['País'], y=df['Bronce'], marker={
                "color": "#CD7F32"}, name="Bronce")

data = [trace0, trace1, trace2]

layout = go.Layout(
    title="Evolutivo Medallas",
    xaxis=dict(title="Medallas de Oro"),
    yaxis=dict(title="Paises"),
    barmode="stack"
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="Barplot.html")
