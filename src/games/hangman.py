from time import sleep
import requests
from random import choice


class Colors:
    PURPL = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[32m'
    YELLO = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


response = requests.get("http://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
data = response.json()

name = input("What is your name, good sir?\n")
print(f"{Colors.PURPL}Welcome to Hangman, {name}! Your game will begin shortly, so do not fret!{Colors.ENDC}")
sleep(1)
counter = 0
while True:
    word = choice(data)
    guesses = []
    turns = round(len(set(word)) * 1.5) + 3
    guessed = ""
    guessed_true = False
    if counter > 0:
        playAgain = input(f"{Colors.BLUE}{name}, would you like to play again?\n{Colors.ENDC}")
        if playAgain.lower() in ["no", "nah", "nope", "never"]:
            break
    while turns > 0:
        guessed = ""
        for x in word:
            if x in guesses:
                guessed += x
            else:
                guessed += "_"
        if guessed == word:
            print(f"{Colors.GREEN}Nice! You successfully finished!{Colors.ENDC}")
            guessed_true = True
            break
        print(f"You have {Colors.BLUE}{Colors.BOLD}{turns}{Colors.ENDC} turns left!\n")
        print(guessed)
        guess = input("What is your guess?\n").lower()
        if guess in word and len(guess) == 1:  # if the guess is in the word
            if guess in guesses:  # if the person guessed that already
                print(f"{Colors.RED}You already guessed that, dummy!{Colors.ENDC}")
                turns -= 1
            else:
                print(f"{Colors.GREEN}Congrats! That was a letter!{Colors.ENDC}")
        else:
            print(f"{Colors.RED}Wrong!{Colors.ENDC}")
            turns -= 1
        guesses.append(guess)
    if not guessed_true:
        print(f"The word was {word}!")
    counter += 1
