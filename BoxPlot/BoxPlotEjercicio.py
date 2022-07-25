import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd


df = pd.read_excel('/Users/eduardo/Desktop/Proyectos/Plotly-Dash/Datasets/3.8/Temperaturas.xlsx',
                   sheet_name='Sheet1')

# print(df.head(5))


recurso1 = go.Box(x=df["Ciudad"], y=df['T_Promedio'])

data = [recurso1]

layout = go.Layout(title='BloxBplot')

figura = go.Figure(data=data, layout=layout)

pyo.plot(figura, filename="EjercicioBox.html")
