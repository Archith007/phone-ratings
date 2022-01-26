import csv
import pandas as pd
import plotly.figure_factory as ff


df = pd.read_csv("phone.csv")
phone_list = df["Avg Rating"].tolist()

fig = ff.create_distplot([phone_list],["ratings"])
fig.show()
