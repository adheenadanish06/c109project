import pandas as pd 
import plotly.figure_factory as ff
import csv

df = pd.read_csv("project.csv")

# fig = px.bar(x = dice_result , y = count)
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"],show_hist = False)
fig.show()