import string

original = string.ascii_lowercase
new = input('What is the new alphabet?\n').lower()


def substitute_letter(letter: str, unmapped: str, mapped: str):
    return mapped[unmapped.index(letter)]


def de_substitute_letter(letter: str, unmapped: str, mapped: str):
    return unmapped[mapped.index(letter)]


def substitute_encode(words: str, unmapped: str, mapped: str):
    new = ""
    for letter in words:
        if letter.lower() in string.ascii_lowercase:
            new += substitute_letter(letter.lower(), unmapped, mapped)
        else:
            new += letter

    return new


def substitute_decode(words: str, unmapped: str, mapped: str):
    new = ""
    for letter in words:
        if letter.lower() in string.ascii_lowercase:
            new += de_substitute_letter(letter.lower(), unmapped, mapped)
        else:
            new += letter

    return new


choice = input("Would you like to [e]ncode/[d]ecode?\n")[0]

if choice == 'e':
    text = input('What would you like to encode?\n')
    substituded = substitute_encode(text, original, new)
    print(f"Here is you result: {substituded}")
else:
    text = input('What would you like to decode?\n')
    substituded = substitute_decode(text, original, new)
    print(f"Here is you result: {substituded}")
