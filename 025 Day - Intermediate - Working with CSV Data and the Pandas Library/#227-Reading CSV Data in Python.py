# with open("weather_data.csv", "r") as weather_data:
#     data = weather_data.readlines()

# import csv
#
# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     tempretures = []
#     for row in data:
#         if row[1] != "temp":
#             tempretures.append(int(row[1]))
#     print(tempretures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
