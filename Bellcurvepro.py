import pandas as pd,plotly.figure_factory as pff

data = pd.read_csv("Bellcurvepro.csv")
fig = pff.create_distplot([data["Avg Rating"].tolist()],["Rating"])
fig.show()