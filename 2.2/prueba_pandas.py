import pandas as pd

df = pd.read_csv("Info_pais.csv", encoding='ISO-8859-1', delimiter=';')

print(df.head(10))

df2 = df[df['Poblacion'] > 150000]
df2 = df[["País", "Poblacion"]]

print(df2.head().sort_values(by='Poblacion', ascending=False))
