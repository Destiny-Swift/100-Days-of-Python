import os
from blind_auction_art import logo
print(logo)

print('Welcome to the secret auction program')
bids = {}

finished_bidding = False

while not finished_bidding:
    name = input('What is your name?: ')
    bid = int(input('What\'s your bid?: $'))

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
    if other_bidders == 'no':
        finished_bidding = True

    bids[name] = bid

    # os.system("clear")  # my unsuccessful attempt to replicate the replit clear() function

# find highest bid and bidder 😎
highest_bid = max(list(bids.values()))
highest_bidder = ''

for bidder in bids:
    if bids[bidder] == highest_bid:
        highest_bidder = bidder

print(f'The winner is {highest_bidder} with a bid of ${highest_bid}')
