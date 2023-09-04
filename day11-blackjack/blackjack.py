############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
from art import logo
import random
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
##################### Hints #####################

counter = {
    '1': 4,
    '2': 4,
    '3': 4,
    '4': 4,
    '5': 4,
    '6': 4,
    '7': 4,
    '8': 4,
    '9': 4,
    '10': 16
}


def add(prev_num, new_num):
    return prev_num+new_num


set_user_drawing = True


def draw_card(computer_total=None):
    new_card = str(random.choice(cards))
    print(new_card)
    if (counter[new_card] > 0):
        counter[new_card] -= 1
        if (new_card == '1'):
            print('inside')
            user_des = None
            if set_user_drawing:
                while user_des != '1' and user_des != '2':
                    user_des = input(
                        'What do you want your ace to be equal to? Enter 1 for 1, enter 2 for 11 ')
                    if (user_des == '1'):
                        return 1
                    elif user_des == '2':
                        return 11
                    else:
                        print('Please choose a valid answer')
            else:
                if computer_total < 10:
                    return 11
                elif computer_total == 10:
                    return random.choice([1, 11])
                else:
                    return 1
        return int(new_card)
    else:
        draw_card()


def play():
    print(logo)
    your_cards = []
    computer_cards = []
    user_total = 0
    computer_total = 0
    user_is_drawing = True
    for idx in range(0, 2):
        your_cards.append(draw_card())
        computer_cards.append(draw_card())

    print('your_cards', your_cards)
    print('computer_cards', computer_cards[0])
    while user_is_drawing:
        user_choice = None
        user_choice = input('Do you want another card? Y or N ').lower()
        if (user_choice == 'y'):
            your_cards.append(draw_card())
            user_total = sum(your_cards)
            print(your_cards)
            if user_total > 21:
                print(f'Your score is {user_total}. Game Over!')
                return
            else:
                print(f'Your score is {user_total}')
        elif user_choice == 'n':
            user_total = sum(your_cards)
            print('Time for dealer to draw cards')
            set_user_drawing = False
            user_is_drawing = False
        else:
            print('Please choose a valid option Y or N ')

    computer_total = sum(computer_cards)
    while computer_total >= 0 and computer_total <= 17:
        computer_cards.append(draw_card())
        computer_total = sum(computer_cards)
    if (computer_total > 21):
        print(f'You win! Dealer has {computer_total}')
    else:
        if computer_total > user_total:
            print(f'Dealer wins!, with {computer_total} vs {user_total}')
        elif computer_total < user_total:
            print(f'You win!, with {user_total} vs {computer_total}')
        elif computer_total == user_total:
            print(f'Its a draw! Both of you have got {user_total}')


def start_game():
    want_to_play = None
    while want_to_play != 'y' and want_to_play != 'n':
        want_to_play = input(
            "Do you want to play a game of BlackJack? Enter Y or N ").lower()
        if want_to_play == 'y':
            play()
        elif want_to_play == 'n':
            print('Ok thank you')
        else:
            print('Please choose a valid option Y or N ')


start_game()
