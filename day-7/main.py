# Step 1
import random
from hangman_art import logo, stages
import hangman_words

lives = 7

chosen_word = random.choice(hangman_words.word_list)
letter_by_user = []
for char in chosen_word:
    letter_by_user.append("_")

print(logo)

while '_' in letter_by_user and lives > 0:
    guess = input('Guess a letter ').lower()
    if (guess in chosen_word):
        for idx in range(0, len(chosen_word)):
            if (chosen_word[idx] == guess):
                letter_by_user[idx] = chosen_word[idx]
        print(letter_by_user)
    else:
        print("You lost a life")
        lives -= 1
        print(stages[lives])
if (lives > 0):
    print("You win!")
else:
    print(f"You Lose! The word was {chosen_word}")
