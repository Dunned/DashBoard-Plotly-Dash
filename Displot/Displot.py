from tokenize import group
import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np


array1 = np.random.randn(500)
array2 = np.random.randn(500)+2

hist_data = [array1, array2]

group_labels = ["Arreglo 1", "Arreglo2"]

fig = ff.create_distplot(hist_data, group_labels, bin_size=[2, 2])

pyo.plot(fig, filename="Displot.py")
