from random import choice

# variables to keep the score
wins = 0
losses = 0
draws = 0

print('Welcome to Rock Paper Scissors!\n')
print(f'{wins} wins, {losses} losses, and {draws} draws\n')

while True:
    user = input('Enter "r" for "Rock", "p" for "Paper" and "s" for "Scissors"\n')
    ai = choice(['r', 'p', 's'])

    rock = '''
        _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    '''

    paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    '''

    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    '''

    if user == 'r':
        print(rock)
    if user == 'p':
        print(paper)
    if user == 's':
        print(scissors)
    if ai == 'r':
        print(rock)
    if ai == 'p':
        print(paper)
    if ai == 's':
        print(scissors)

    if (user == 'r' and ai == 's') or (user == 'p' and ai == 'r') or (user == 's' and ai == 'p'):
        print('You Win')
        wins += 1
    elif (ai == 'r' and user == 's') or (ai == 'p' and user == 'r') or (ai == 's' and user == 'p'):
        print('You Loose! 😂😂')
        losses += 1
    else:
        print('Draw!')
        draws += 1

    print(f'{wins} wins, {losses} losses, and {draws} draws\n')
