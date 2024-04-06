from random import choice
from blackjack_art import logo


def deal_card():
    """Returns a random card from the 'cards' deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card


def calculate_score(cards):
    """Takes a list of cards and returns the core calculated from the cards."""

    if 11 in cards and sum(cards) > 21:
        index = cards.index(11)
        cards.remove(11)
        cards.insert(index, 1)

    return sum(cards)


def compare(p_score, p_cards, d_score, d_cards):
    if p_score == d_score:
        return 'Draw 🙃'
    elif d_score == 21 and len(d_cards) == 2:
        return 'Lose, opponent has a BLACKJACK! 😱'
    elif p_score == 21 and len(p_cards) == 2:
        return 'You win with a BLACKJACK! 😎'
    elif p_score > 21:
        return 'Bust. You lose 😭'
    elif d_score > 21:
        return 'Opponent went over. You win 😁'
    elif p_score > d_score:
        return 'You win 😃'
    else:
        return 'You lose 😤'


def play_game():
    print(logo)

    player_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]

    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    game_over = False

    while not game_over:
        print(f'    Your cards: {player_cards}, current score: {player_score}')
        print(f"    Dealer's first card: {dealer_cards[0]}")

        if player_score == 21 or dealer_score == 21 or player_score > 21 or dealer_score> 21:
            game_over = True
        else:
            feedback = input("\nType 'y' to draw another card or 'n' to pass: ").lower()
            if feedback == 'y':
                player_cards.append(deal_card())
                player_score = calculate_score(player_cards)
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17 and player_score <= 21:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f'\n    Your final hand: {player_cards}, final score: {player_score}')
    print(f"    Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(f'\n{compare(player_score, player_cards, dealer_score, dealer_cards)}\n\n')


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()
