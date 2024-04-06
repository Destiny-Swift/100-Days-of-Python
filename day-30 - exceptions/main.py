# Error Handling

# FileNotFoundError
# with open('a_file.txt') as file:
#     print(file.read())

# KeyError
# a_dictionary = {'key': 'value'}
# print(a_dictionary['non_existent_key'])

# IndexError
# fruit_list = ['Apple', 'Banana', 'Pear']
# fruit = fruit_list[3]

# TypeError
# text = 'abc'
# print(text + 5)


# string error exception (entering a string when numbers are needed)

user_input = input('Enter some input 🙄')

try:
    print(int(user_input))
except ValueError as error_message:
    print(f'Your input {user_input} is a string, an unacceptable Data Type 🙂')
else:
    print('Worked')
finally:
    # raising errors cause it's fun and I feel like 🙂
    print(f'Hidi Guy Hidi There')
    raise TypeError('Necessary Village People Induced Error 🙂')
