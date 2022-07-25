import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv(
    '/Users/eduardo/Desktop/Proyectos/Plotly-Dash/Datasets/3.11/PEATONES_2020_mod.csv',
    encoding='ISO-8859-1', delimiter=';')

argenza = df[df['DISTRITO'] == 'Arganzuela']['PEATONES']
centro = df[df['DISTRITO'] == 'Centro']['PEATONES']


hist_data = [argenza, centro]
labels = ['Peatones Promedio Argenza', 'Peatones Promedio Centro']

fig = ff.create_distplot(hist_data=hist_data, group_labels=labels,
                         bin_size=20)

pyo.plot(fig, filename="ResultadoEjercico1.html")
