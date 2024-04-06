
sentence = 'What is the Airspeed velocity of an Unladen Swallow?'
# Don't change the code above 👆

# Write your code below:

results = {word: len(word) for word in sentence.split(' ')}

print(results)


# converting temperatures
weather_c = {
    'Monday': 12,
    'Tuesday': 14,
    'Wednesday': 15,
    'Thursday': 14,
    'Friday': 21,
    'Saturday': 22,
    'Sunday': 24,
}

# Don't change the code above 👆

# Write your code below:
weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}


print(weather_f)
