import numpy as np
import pandas as pd


sales = pd.read_csv('junesales.csv', header=0)

data = pd.read_csv("weatherdata.csv")
data["Year"] = pd.DatetimeIndex(data["Date"]).year
data["Month"] = pd.DatetimeIndex(data["Date"]).month
data["DayOfMonth"] = pd.DatetimeIndex(data["Date"]).day


sales["DayOfMonth"] = pd.DatetimeIndex(sales['Date']).day
print(sales.head())


New_Castle = data[(data["Location"] == "Newcastle") & (
    data["Year"] == 2011) & (data["Month"] == 6)]
print(New_Castle.head())

merge_data = New_Castle.merge(sales, on="DayOfMonth")

print(merge_data.head())
