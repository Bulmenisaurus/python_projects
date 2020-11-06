import string
from random import choice

def multiline_input(__prompt):
    print(__prompt)
    input_lines = ['\x00']
    while (line := input()) != '' and input_lines[-1] != '':
        input_lines.append(line)
    return '\n'.join(input_lines)[1:]


sentences = multiline_input("Enter your sentences to funnify!")

vowels = "eyuioa"
consonants = "qwrtpsdfghklzxcvbnm"
funny_ending = input("What is the funny ending? [dont write anything for random]\n") or \
               (choice(consonants) + choice(vowels))

new_sentences = [x+funny_ending if x[-1].isalpha() else x for x in sentences.split()]
print(new_sentences)



