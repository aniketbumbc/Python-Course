from matplotlib.axes import Subplot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("weatherdata.csv")

# print(data.head())


# filter data


# print(data[(data["Sunshine"] > 5) & (data["MaxTemp"] > 35)])


# *********  create new columns **********

# print(pd.DatetimeIndex(data["Date"]).year)

data["Year"] = pd.DatetimeIndex(data["Date"]).year
data["Month"] = pd.DatetimeIndex(data["Date"]).month
data["Day"] = pd.DatetimeIndex(data["Date"]).day

data["MaxTemp_F"] = data["MaxTemp"] * 9/5 + 32


# ******** Lamda functions ***********


data["is_rain"] = data["Rainfall"].apply(
    lambda x: "Rainy" if x > 50 else "No Rain")
print(data.head())


print(data[data["is_rain"] == "Rainy"])
