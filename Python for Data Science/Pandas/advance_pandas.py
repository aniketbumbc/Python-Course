from matplotlib.axes import Subplot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


sales = pd.read_excel('sales.xlsx', index_col=[0, 1])

print(sales.head(3))  # first three rows
print(sales)  # last five rows


# print(sales.info()) # info about column and data types


print(sales.describe())  # min, max,mean,std

# print(sales["Profit"])

# sales[['Sales', 'Profit']].plot(kind='box', subplots=True)
# plt.show()
