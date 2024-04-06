# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#
#     temperatures = []
#
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# So much fuss just to get a column of a data set 🙄


import pandas as pd  # Pandas...now we're talking baby. 😎


# data = pd.read_csv('weather_data.csv')
# print(type(data))
#
# print(type(data['temp']))
#
# data_dict = data.to_dict()
# print(data_dict)


# Get data in column

# temp_list = data['temp'].to_list()

# average_temp = round(sum(temp_list)/len(temp_list), 2)
# print(average_temp)
# 👆🏻👆🏻👆🏻👆🏻 Too much stress and that's why we have pandas 😏


# print(round(data['temp'].mean(), 2))  # Now we're talking

# print(data['temp'].max())  # getting the max value vs python's humongous process

# print(data['condition'])

# print(data.condition)

# Get data in Row
# print(data[data.day == 'Monday'])

# print(data[data.temp == data.temp.max()])  # row(s) with max temperature

# monday = data[data.day == 'Monday']
# print(monday.condition)

# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)


# Create DataFrame from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'score': [75, 56, 65]
# }
# data = pd.DataFrame(data_dict)
# print(data)
# data.to_csv('new_data.csv', index=False)


data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

# print(len(data))
# print(len(data['Primary Fur Color'][data['Age'] == 'Adult']))

gray_squirrels_count = len(data['Primary Fur Color'][data['Primary Fur Color'] == 'Gray'])  # faster than value_counts()
red_squirrels_count = len(data['Primary Fur Color'][data['Primary Fur Color'] == 'Cinnamon'])  # & returns int not a
black_squirrels_count = len(data['Primary Fur Color'][data['Primary Fur Color'] == 'Black'])  # DataFrame 😕


print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dictionary = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrels_count, red_squirrels_count, black_squirrels_count],
}

df = pd.DataFrame(data_dictionary)

df.to_csv('squirrel_count.csv', index=False)
