from art import logo
import random
# Todo1- Create Logo
# Todo2- Create starter function
# todo3- choose level and give the correct lives amount accordingly
# Todo4- Create logic that subtracts lives left each time user choses a wrong number
# todo5- create logic for when the user chooses the right number. Let him know that he won!


def begin_game():
    print(logo)
    level_chosen = input(
        "Choose a level. Type E for easy and H for hard ").lower()
    rand_number = random.randint(0, 100)
    lives = None
    if level_chosen == 'e':
        lives = 10
    else:
        lives = 5
    guess = None
    while guess != rand_number and lives > 0:
        guess = int(input('Guess a number '))
        if guess == rand_number:
            print('You win')
            return
        else:
            lives -= 1
            if guess > rand_number:
                print('Too high')
            elif guess < rand_number:
                print('To low')
            print(f'Lives left {lives}')

    print(f'You lose the number was {rand_number}')


begin_game()
