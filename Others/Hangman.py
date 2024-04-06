from random import choice

# import the other necessary modules
from hangman_art import logo, stages
from hangman_words import word_list

# the list of words to be chosen from
word_list = word_list

# the chosen word from the list
chosen_word = choice(word_list)

# numer of lives the user has, corresponding to the number of hangman styles.
lives = 6

# fill in the required number of blanks based on the word chosen
word_display = ['_' for i in range(len(chosen_word))]

# the different hangman stages
stages = stages

# print the welcome hangman logo ascii art
print(logo)

# the main operation which takes the user input and modifies the display with every correct guess.
# only runs when lives != 0 and '_' is not in the display word. It stops running once one of these is false.
# that is when lives is 0 or all blanks have been replaced with the correct letters.
# still working on making my quintessential logic understandable to the mere man...😁😎
while lives != 0 and '_' in word_display:
    guess = input('Guess a letter:\n').lower()

    # check if the guess matches any letter in the chosen word, if yes replace the _ in the word display position
    # with the corresponding letter position

    # Being kind to let the user know that their guess has already been made, and also kind to not take a life.
    if guess in word_display or guess == '':
        print(f'You gave no guess or you\'ve entered the letter "{guess}" already 😐😐😐')

    # Take a life since the guess is not in the chosen word and print the new hangman stage
    elif guess not in chosen_word:
        print(f'Your guessed the letter {guess}, that\'s not in the word. You loose a life 😐😐')
        lives -= 1
        print(stages[lives])

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            word_display[position] = letter

    print(' '.join(word_display))

# check for a win
if '_' not in word_display:
    print('\nYou Win! (in a sarcastic manner 😐😐)')

else:
    print('\nYou Loose 😂😂😂😂😂 \nSee as you just kill that guy! 😐😐😐')
