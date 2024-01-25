from math import sqrt
from matplotlib.axes import Subplot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("weatherdata.csv")

# print(data.head())


# filter data


# print(data[(data["Sunshine"] > 5) & (data["MaxTemp"] > 35)])


# *********  create new columns **********

print(pd.DatetimeIndex(data["Date"]).year)

data["Year"] = pd.DatetimeIndex(data["Date"]).year
data["Month"] = pd.DatetimeIndex(data["Date"]).month
data["Day"] = pd.DatetimeIndex(data["Date"]).day

# data["MaxTemp_F"] = data["MaxTemp"] * 9/5 + 32


# ******** Lamda functions ***********


# data["is_rain"] = data["Rainfall"].apply(
#     lambda x: "Rainy" if x > 50 else "No Rain")
# print(data.head())


# print(data[data["is_rain"] == "Rainy"])


# find location where most amount of rainfall


# print(data.tail())

data_location = data.groupby(by=["Location"]).mean(numeric_only=True)

# print(data_location.sort_values("Rainfall").tail())

data_month = data.groupby(by=["Month"]).mean(numeric_only=True)

# print(data_month.sort_values("MinTemp").head())


# x one row of data frame


def wci(x):
    velocity = x["WindGustSpeed"]
    minTemp = x["MinTemp"]
    return (10*sqrt(velocity)-velocity + 10.5)*(33 - minTemp)


data["WCI"] = data.apply(wci, axis=1)
data_grp_month = data.groupby(by=["Month", "Year"]).mean(numeric_only=True)

print(data_grp_month.sort_values(['WCI', 'MaxTemp'], ascending=False).head())
