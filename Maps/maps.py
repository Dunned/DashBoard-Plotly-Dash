
import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

df = pd.read_excel(r'/Users/eduardo/Desktop/Proyectos/Plotly-Dash/Datasets/3.13/Peatones_prom_coord.xlsx',
                   )

token_map = 'pk.eyJ1IjoiZWR1YXJkbzV0IiwiYSI6ImNrcGthZDRhMDExdmkydnJyM2pyajhxN2oifQ.PcUawWc5D7QMsADngKwKHw'

fig = go.Figure(
    go.Scattermapbox(
        lon=df['LONGITUD'],
        lat=df['LATITUD'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=df['Peatones_prom']/10,
            color=df['Peatones_prom']
        )
    )
)

fig.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=token_map,
        center=dict(
            lat=40.41,
            lon=-3.7
        ),
        zoom=12
    ),
)

pyo.plot(fig, filename='mapa.html')
