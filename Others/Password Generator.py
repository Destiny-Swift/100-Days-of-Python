from random import choice, shuffle
print('Welcome to PyPassword Generator')

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = list('''!#$%&()*+''')


length_letters = int(input('How many letters would you like in your password?\n'))
length_symbols = int(input('How many symbols would you like in your password?\n'))
length_numbers = int(input('How many numbers would you like in your password?\n'))

password = []

for i in range(length_letters):
    password.append(choice(letters))

for i in range(length_numbers):
    password.append(choice(numbers))

for i in range(length_symbols):
    password.append(choice(symbols))

shuffle(password)


print(f'Here is your password: {"".join(password)}')
