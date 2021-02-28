import string
from random import randint

# checks english dictionary for % of words. Feel free to replace this with your own file or request.
with open("../python_data/Dictionary.txt", "r") as check_eng:  # checks english dictionary
    dictionary_ = check_eng.read()


def check_wrd(wrd):
    if wrd in dictionary_:
        return True
    else:
        return False


alph = string.ascii_letters[0:26]
if (choice := input("Would you like to encode, decode, or hack a ceaser shift?\n")).lower() == 'encode':
    to_encode = input("What would you like to encode?\n")
    key = randint(1, 25)
    print("Done!")
    print("Key:", key)
    print(''.join([alph[(alph.index(x.lower()) + key) % 26] if x.lower() in alph else x for x in to_encode]))
elif choice == 'decode':
    to_decode = input("What message would you like to decode?\n")
    key = 26 - int(input("What is the key?\n"))
    print(''.join([alph[(alph.index(x.lower()) + key) % 26] if x.lower() in alph else x for x in to_decode]))
elif choice == 'hack':
    input("Password: ")
    print("Oops, that input isn't connected to anything. Oh well! ¯\\_(ツ)_/¯")

    secret_code = input("What message would you like to intercept & hack?\n")

    decodings, validating = [], []

    for shift in range(26):
        decoded = [alph[(alph.index(x.lower()) + shift) % 26] if x.lower() in alph else x for x in secret_code]
        decodings.append(''.join(decoded))

    for count, sentence in enumerate(decodings):
        validate_words, fract = (0, len(sentence.split(' ')))
        for word in sentence.split(' '):
            if check_wrd(word):
                validate_words += 1
        validating.append(
            validate_words / fract)  # number from 0-1 that shows how many % words are in the engl dictionary

    print("Hacking complete:\n\n")
    print(decodings[validating.index(max(validating))])
    print(f"Key: {validating.index(max(validating))}")
