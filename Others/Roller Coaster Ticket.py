# Roller Coaster Ticket Sales
if int(input('Enter your height in cm: ')) > 120:
    print('You can ride the roller coaster')
    age = int(input('How old are you? '))
    ticket = 0
    if age < 12:
        ticket = 5

    elif age < 18:
        ticket = 7

    elif 45 <= age <= 55:
        print("Everything is going to be okay. Have a free ride on us.")
    else:
        ticket = 12
    photos = input('Would you like a ticket with photos for an extra $3? (Y/N): ')
    if photos == 'Y':
        ticket += 3

    print(f'You have to pay ${ticket}.')

else:
    print('You can not ride the roller coaster!')


print('Welcome to Python Pizza Delivery')
bill = 0
size = input('What size of pizza would you like (s/m/l)? ')
pepperoni = input('Would you like pepperoni on your pizza (y/n)? ')
extra_cheese = input('Would you like extra cheese on your pizza (y/n)? ')

if size == 's':
    bill += 15
elif size == 'm':
    bill += 20
else:
    bill += 25

if pepperoni == 'y':
    if size == 's':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'y':
    bill += 1

print(f'Your total bill is ${bill}.')
