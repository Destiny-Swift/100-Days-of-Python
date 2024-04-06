from random import randint, seed

# names = ['Swift', 'Prosper', 'Daluchi', 'Nnanna', 'Chidinma', 'Chidi', 'Paula']

while True:
    seed(input('Enter seed: '))
    names = input('Enter the names of everyone\n').split(', ')
    random_choice = randint(0, len(names) - 1)
    person_who_will_pay = names[random_choice]
    print(f'{person_who_will_pay} is going to buy the meal today!')
