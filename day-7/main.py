# Step 1
import random
from hangman_art import logo, stages
import hangman_words

lives = 7

chosen_word = random.choice(hangman_words.word_list)
word = []
letters_used = []
for char in chosen_word:
    word.append("_")

print(logo)

while '_' in word and lives > 0:
    guess = input('Guess a letter ').lower()
    if guess not in letters_used:
        letters_used += guess
        if (guess in chosen_word):
            for idx in range(0, len(chosen_word)):
                if (chosen_word[idx] == guess):
                    word[idx] = chosen_word[idx]
            print(f"Your word {word}")
        else:
            print("You lost a life")
            lives -= 1
            print(f"Lives left {stages[lives]}")
    else:
        print("already used this letter")
    print(f"Letters used {','.join(letters_used)}")
if (lives > 0):
    print("You win!")
else:
    print(f"You Lose! The word was {chosen_word}")
