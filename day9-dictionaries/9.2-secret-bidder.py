from replit import clear
from art import logo
# HINT: You can call clear() to clear the output in the console.


def start_auction():
    print(logo)
    auction_on = True
    players = {}
    while auction_on:
        name = input('What is your name? ')
        bid = int(input('How much do you want to bid? '))
        players[name] = bid
        continue_bid = input('Are their any other players? Yes or no ').lower()
        if (continue_bid == 'no'):
            auction_on = False
        elif continue_bid == 'yes':
            clear()

    highest_bidder = {
        'name': 'unknown',
        'bid': 0
    }
    for player in players:
        if players[player] > highest_bidder['bid']:
            highest_bidder['name'] = player
            highest_bidder['bid'] = players[player]

    print(
        f"The winner is {highest_bidder['name']} with a bid of {highest_bidder['bid']}")


start_auction()
