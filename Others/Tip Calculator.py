# Tip Calculator
print('Welcome to the Tip Calculator!')

bill = float(input('What was the total bill? $'))

tip = int(input('What percentage tip would you like to give? 10, 12 or 15? '))

num_people = int(input('How many people to split the bill? '))

bill_per_person = (bill *((tip/100) + 1)) / num_people

print(f'Each person should pay ${round(bill_per_person, 2)}')
