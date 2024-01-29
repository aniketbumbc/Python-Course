\
#    "`info.csv` has the data hour by hour data about the concentration of polutants in the air and the status of the intruments. \n",
# "`item_info` has the data for items and levels of concetration. \n",
# "`station_info` has the data for measuring stations.

import pandas as pd

info_data = pd.read_csv('info.csv')
item_data = pd.read_csv('item_info.csv')
station_data = pd.read_csv('station_info.csv')


# print(info_data.head())
# print(item_data.head())
# print(station_data.head())

# Question

# 1. Create a new Dataframe whcih has information about the item code and item name


subItem = item_data[['Item code', 'Item name']]  # subset data

# print(subItem.head())


# 2. Create a new Dataframe whcih has information about the station code and station name

subStationInfo = station_data[['Station code', 'Station name(district)']]

# print(subStationInfo.head())


# 3.  In the `data` DataFrame add in a column displaying the names of the items.

# extract column and then concat to main DF
extracted_col = item_data['Item name']

# print(extracted_col)

info_data_item_name = pd.concat(
    [info_data, extracted_col], axis=1)

# print(info_data_item_name.head())


# 4. In the info_data_item_name DataFrame add in a column displaying the names of the stations.
extracted_col_station_name = station_data['Station name(district)']

info_data_item_name_sname = pd.concat(
    [info_data_item_name, extracted_col_station_name], axis=1)


# print(info_data_item_name_sname.head())


# 5 . DataFrame drop the columns Station code and Item code

info_data_item_name_sname = info_data_item_name_sname.drop(
    ['Station code', 'Station name(district)'], axis=1)


# print(info_data_item_name_sname.head())


# create dictionary

dic_data = {'Instrument status': [0, 1, 2, 4, 8, 9],
            'Status': ['Normal',
                       'Need for calibration',
                       'Abnormal',
                       'Power cut off',
                       'Under repair',
                       'Abnormal data']
            }


new_data = pd.DataFrame(dic_data)

# print(new_data)

# info_data = info_data.drop(['Instrument status'], axis=1)


instrument_data = info_data.merge(new_data, on="Instrument status", how="left")


print(instrument_data.head())

# 6. Time series Year, day , month

instrument_data['Year'] = pd.DatetimeIndex(
    instrument_data["Measurement date"]).year
instrument_data['Month'] = instrument_data["Month"] = pd.DatetimeIndex(
    instrument_data["Measurement date"]).month
instrument_data['Date'] = instrument_data["Day"] = pd.DatetimeIndex(
    instrument_data["Measurement date"]).day
instrument_data['Hour'] = instrument_data["Measurement date"] = pd.DatetimeIndex(
    instrument_data["Date"]).hour

# print(instrument_data.head())
