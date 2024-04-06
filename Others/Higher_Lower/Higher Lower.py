from random import choice
from higher_lower_art import logo, vs
from higher_lower_game_data import data


def user_answer(celebrity_a, celebrity_b):
    """Prints the celebrity data in printable format and returns the user choice"""
    print(f"\nCompare A: {celebrity_a['name']}, a {celebrity_a['description']}, from {celebrity_a['country']}.")
    print(vs)
    print(f"\nAgainst B: {celebrity_b['name']}, a {celebrity_b['description']}, from {celebrity_b['country']}.")

    return input("Who has more followers? Type 'A' or 'B': ").lower()


def check(user_option, celebrity_a, celebrity_b):
    """check whether the user is correct"""
    other_option = celebrity_a
    if user_option == 'a':
        other_option = celebrity_b

    user_option = eval(f'celebrity_{user_option}')  # eval and f-strings to save useless lines of if statements

    if user_option['follower_count'] > other_option['follower_count']:  # checking the follower counts
        return user_option

    else:
        return 'wrong'


def game_play():
    """Controls the game flow"""
    print(logo)
    score = 0

    celebrity_A = choice(data)  # give it some random celebrity data

    while True:  # just needed some container to keep this part looping
        celebrity_B = choice(data)
        while celebrity_B == celebrity_A:
            celebrity_B = choice(data)

        user_input = user_answer(celebrity_A, celebrity_B)

        feedback = check(user_input, celebrity_A, celebrity_B)

        if feedback == 'wrong':
            return score

        else:
            score += 1
            print(f"\nYou're right! Current Score: {score}")
            celebrity_A = feedback


print(f"\nYou dey claim scrunchy 😂🤣🤣. Final Score: {game_play()}")


# TODO 1 Get the ASCII arts for welcome and for operations
# TODO 2 Get the data of the celebrities
# TODO 3 Create 2 variables and assign a random celebrity for each
# TODO 4 Create a list where every used celebrity data is appended to to avoid repetition
#  No longer required
# TODO 5 Create a score variable to track the user score
# TODO 6 Take an answer from the user and check whether or not she is right (in terms of her option
#  being the celebrity with more followers
# TODO 7 If wrong; print score and end
# TODO 8 Else; Make the 'chosen' 'correct' option the A variable and get another data to be B
# TODO 9 Use a while loop to go on and on until the user finally fails.
