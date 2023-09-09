from art import logo, vs
from game_data import data
import random
print(logo)


# Todo1 - create all variables that define the game such as- score, is_playing

score = 0
is_playing = True

random.shuffle(data)
curr_page = data.pop()
curr_compare = data.pop()
did_win = False
# Todo2- Define what is the condition for game to keep going
while is_playing:
    print(f'Your score is {score}')
    print('Who has more followers? ')
    print(f'{curr_page["name"]}, {curr_page["description"]} from {curr_page["country"]}. This profile has {curr_page["follower_count"]}')
    print(vs)
    print(
        f'{curr_compare["name"]}, {curr_compare["description"]} from {curr_compare["country"]}')
    answer = input("Who have more followers? A or B? ").lower()
    winner = None
    print(f'{curr_page["name"]} has {curr_page["follower_count"]} followers vs {curr_compare["name"]} has {curr_compare["follower_count"]} followers')
    if answer == 'a' or answer == 'b':
        if curr_page["follower_count"] > curr_compare["follower_count"]:
            if answer == 'a':
                if len(data) > 0:
                    score += 1
                    curr_compare = data.pop()
                else:
                    is_playing = False
                    did_win = True

            elif answer == 'b':
                is_playing = False
        elif curr_page["follower_count"] < curr_compare["follower_count"]:
            if answer == 'a':
                is_playing = False
            elif answer == 'b':
                if len(data) > 0:
                    score += 1
                    temp_page = curr_compare
                    curr_page = temp_page
                    curr_compare = data.pop()
                else:
                    is_playing = False
                    did_win = True
        else:
            if answer == 'a':
                curr_compare = data.pop()
            elif answer == 'b':
                temp_page = curr_compare
                curr_page = temp_page
                curr_compare = data.pop()
    else:
        print('Please pick a valid option ')

if not is_playing and did_win:
    print('You won!')
else:
    print('You lose!')
