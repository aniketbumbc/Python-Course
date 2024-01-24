from matplotlib.axes import Subplot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# sales = pd.read_excel('sales.xlsx', index_col=[0, 1])

# print(sales.head(3))  # first three rows
# print(sales)  # last five rows


# print(sales.info()) # info about column and data types


# print(sales.describe())  # min, max,mean,std

# print(sales["Profit"])

# sales[['Sales', 'Profit']].plot(kind='box', subplots=True)
# plt.show()

sales = pd.read_excel('sales.xlsx', index_col=[1])
print(sales)

# to access specific coloumn  ie coloumn indexing

# print(sales[['Profit', 'Sales']]) # multiple columns

# print(sales.No_of_Orders)

# Data type in pandas <class 'pandas.core.series.Series'>'
# print(type(sales["Profit"]))


# *** row and column specific index single output ***
# print(sales.loc["Western US"])  # row and colmns

# print(sales.loc["Western US", "Profit"])  # profit and

# # *** iloc with number ***
# print(sales.iloc[6])
# print(sales.iloc[18, 2])


# *** slicling ie indexing in chunks and columns range of data ***

# print(sales.loc[:, ["Market", "Profit"]].head())
# print(sales.iloc[:, [0, 3, 2]].head())


# ** slicling ie indexing in chunks and rows range of data ****

# print(sales.loc[["Western Africa", "Southern Africa", "North Africa"], :])
# print(sales.iloc[0:3, :])


# slicling both rows and columns

# print(sales.iloc[0:3, 2:4])


# ******* Filter Data *******


print(sales[(sales["Profit"] > 80000) & (sales["No_of_Orders"] > 500)])

# print(sales[(sales["Market"].isin(["LATAM", "Europe"]))
#       & (sales["Sales"] > 250000)])
