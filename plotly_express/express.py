import plotly.express as px
import pandas as pd


df = pd.read_excel(
    '/Users/eduardo/Desktop/Proyectos/Plotly-Dash/Datasets/3.6/Info_pais.xlsx')


fig1 = px.bar(df[0:10], x='País', y='Esperanza de vida',
              color='Continente', title='Distribucion paises',
              text_auto='.2s')

fig2 = px.scatter(df, x="País", y="Poblacion", color="Continente")
fig1.show()
fig2.show()
