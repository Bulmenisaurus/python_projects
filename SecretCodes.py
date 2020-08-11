# secret codes
# chr() int -> str, ord() str --> int
import random


def encode(encode_input):
    shift = random.randint(0, 15000)
    encoded = chr(shift+1500)  # ord(encoded[0])-1500 == shift
    for i in encode_input:
        encoded += chr((ord(str(i))+shift))
    return encoded


def decode(decode_input):
    shift = ord(decode_input[0])-1500
    decoded = ""
    bug = 0
    for i in decode_input:
        bug += 1  # because of a glitch where first letter is bugged
        if bug > 1:  # and too lazy for string slicing (it's too complicated tbh)
            decoded += chr((ord(str(i))-shift))
    return decoded


print("Simply type \"Quit\" to stop.")
while True:
    choice = input("Would you like to decode or encode a message?\n").lower()
    if choice[0] == "e":
        print(encode(input("What would you like to encode?\n")), "\n")
    elif choice[0] == "d":
        print(decode(input("What would you like to decode?\n")), "\n")
    elif choice == "quit":
        break
    else:
        print("..... what?")
