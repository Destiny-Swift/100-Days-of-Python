# Love Calculator
print('Welcome to the Love Calculator!')
name1 = input('What is your name? \n').lower()
name2 = input('What is their name? \n').lower()

result = name1 + name2

true = result.count('t') + result.count('r') + result.count('u') + result.count('e')
love = result.count('l') + result.count('o') + result.count('v') + result.count('e')

love_score = int(str(true) + str(love))

message = ''

if (love_score < 10) or (love_score > 90):
    message = 'You go together like Coke and Mentos'
elif 40 <= love_score <= 50:
    message = "You're alright together"

print(f'Your score is is {love_score}%')
print(message)