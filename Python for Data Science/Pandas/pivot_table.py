import pandas as pd

data = pd.read_csv("weatherdata.csv")

data["Year"] = pd.DatetimeIndex(data["Date"]).year
data["Month"] = pd.DatetimeIndex(data["Date"]).month
data["DayOfMonth"] = pd.DatetimeIndex(data["Date"]).day


# print(data.head())

data_2016 = data[data["Year"] == 2016]
print(data_2016.head())

pv_table_avg_rainfall = data_2016.pivot_table(
    index="Location", columns="Month", values="Rainfall", aggfunc="mean")

print(pv_table_avg_rainfall.head())

# df.pivot(columns='grouping_variable_col', values='value_to_aggregate', index='grouping_variable_row')

# Group the data 'df' by 'month' and 'day' and find the mean value for column 'rain' and 'wind' using the pivot table command.

# df_1 = df.pivot_table(index = ["month","day"],columns="month",values=["rain","wind"],aggfunc=["rain":np.mean, "wind":np.mean])
