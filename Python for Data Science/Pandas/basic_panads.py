import pandas as pd
import numpy as np
cars_per_cap = [809, 731, 588, 18, 200, 70, 45]
country = ['United States', 'Australia', 'Japan',
           'India', 'Russia', 'Morocco', 'Egypt']
drives_right = [True, False, False, False, True, True, True]


data = {"cars_per_cap": cars_per_cap,
        "country": country, "drives_right": drives_right}


cars = pd.DataFrame(data)
# print(cars)


# newCars = pd.DataFrame([cars_per_cap, country, columns=['CAR', 'COUNTRY'])
# print(newCars)

# car_df = pd.read_csv('cars.csv')
car_df_no_header = pd.read_csv('cars.csv', header=None, index_col=0)
# print(car_df)
car_df_no_header.index.name = None
# print(car_df_no_header)

# assign header

# car_df_no_header.columns = ["region",
#                             "country_name", "cap", "drive_right"]


# print(car_df_no_header.index)

new_car = pd.read_csv('cars.csv', header=None)

new_car.columns = ["country_code", "region",
                   "country_name", "cap", "drive_right"]

new_car.set_index(["region", "country_code"], inplace=True)

print(new_car)


# back Dataframe to csv
new_car.to_csv('new_cars.csv')
