import time
import requests
from random import choice

response = requests.get("http://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
data = response.json()

name = input("What is your name, good sir?\n")
print(f"Welcome to Hangman, {name}! Your game well begin shortly, so do not fret!")
time.sleep(1)
counter = 0
while True:
    word = choice(data)
    guesses = []
    turns = round(len(set(word)) * 1.5) + 5
    guessed = ""
    guessed_true = False
    if counter > 0:
        playAgain = input(f"{name}, would you like to play again?\n")
        if playAgain.lower() == "no":
            break
    while turns > 0:
        guessed = ""
        for x in word:
            if x in guesses:
                guessed += x
            else:
                guessed += "_"
        if guessed == word:
            print(f"Nice! You successfully finished!")
            guessed_true = True
            break
        print(f"You have {turns} turns left!\n")
        print(guessed)
        guess = input("What is your guess?\n").lower()
        if guess in word and len(guess) == 1:  # if the guess is in the word
            if guess in guesses:  # if the person guessed that already
                print("You already guessed that, dummy!")
                turns -= 1
            else:
                print("Congrats! That was a letter!")
        else:
            print("Wrong!")
            turns -= 1
        guesses.append(guess)
    if not guessed_true:
        print(f"The word was {word}!")
    counter += 1
