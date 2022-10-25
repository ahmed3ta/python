# import csv
import pandas
#
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     print(data)
# #     for row in data:
# #         if row[1] != "temp":
# #             # print(row)
# #             temperatures.append(int(row[1]))
# #
# #     print(temperatures)
#
#
# data = pandas.read_csv("weather_data.csv")
# # data_dict = data.to_dict()
# # # print(data_dict)
# # temp_list = data["temp"].to_list()
# # print(data["temp"].max())
# monday = data[data.day == "Monday"]
# print(int(monday.temp)*1.8 + 32)

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(squirrel_data["Primary Fur Color"])
gray_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]["Primary Fur Color"])
black_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]["Primary Fur Color"])
cinnamon_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"])

squirrel_color = {
    "Color": ["gray", "black", "cinnamon"],
    "Count": [gray_count, black_count, cinnamon_count]
}
print(squirrel_color)
squirrel_color_df = pandas.DataFrame(squirrel_color)
print(squirrel_color_df)
squirrel_color_df.to_csv("squirrel-colors.csv")




# data_dict = {
#     "Students": ["Amy", "Ahmed", "Eman", "Aya"],
#     "Grades": [56, 80, 99, 79]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("grades.csv")