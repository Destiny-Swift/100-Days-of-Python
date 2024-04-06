# Life in weeks
age = int(input('How old are you: '))
years_left = 90 - age

months = years_left * 12
weeks = years_left * 52
days = years_left * 365

print(f'Time left on Earth: {days} days {weeks} weeks, and {months} months')
