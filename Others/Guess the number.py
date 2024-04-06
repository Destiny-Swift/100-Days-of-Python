from guess_the_number_art import logo
from random import randint

print(logo)
print('Welcome to the Number Guessing Game')
print("I'm thinking of a number between 1 and 100")

random_number = randint(1, 100)

attempts = 0

difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ")

if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5


def feedback(guess):
    difference = guess - random_number

    if difference > 30 or difference < -30:
        message = 'Way too high'.split(' ')
    elif difference > 20 or difference < -20:
        message = 'Too high'.split(' ')
    elif difference > 5 or difference < -5:
        message = 'Moderately high'.split(' ')
    else:
        message = 'Very close but still high'.split(' ')

    if '-' in str(difference) and len(message) != 0:
        message.remove('high')
        message.append('low'.capitalize())

    return ' '.join(message)


user_guess = 0

while attempts != 0 and user_guess != random_number:
    user_guess = int(input(f"You have {attempts} attempts to guess the number \nMake a guess: "))
    if user_guess != random_number:  # for a special case when I guess correctly on the last trial
        print(f'\n{feedback(user_guess)}\n')
        attempts -= 1

if attempts != 0:
    print(f'\nYou win 😎 \nThe number I\'m thinking about is {random_number}')
else:
    print(f'You loose 😂😂😂 \nThe number I\'m thinking about is {random_number}')
