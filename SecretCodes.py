# secret codes
# chr() int -> str, ord() str --> int
import random
from time import sleep
from pyperclip import copy


def encode(encode_input):
    shift = random.randint(1000, 15000)
    encoded = chr(shift+1500)  # ord(encoded[0])-1500 == shift
    for i in encode_input:
        encoded += chr((ord(str(i))+shift))
    copy(encoded)
    return encoded


def decode(decode_input):
    try:
        shift = ord(decode_input[0])-1500
        decoded = ""
        bug = 0
        for i in decode_input:
            bug += 1  # because of a glitch where first letter is bugged
            if bug > 1:  # and too lazy for string slicing (it's too complicated tbh)
                try:
                    decoded += chr((ord(str(i)) - shift))
                except:
                   print(f"We're pretty sure something went wrong, especially with letter", i)
        return decoded
    except IndexError:
        return "Something went wrong :("


def valid_input(validate_input):
    if len(str(validate_input).strip()) > 2:
        return True
    else:
        return False


print("Welcome to the Hackers Encrpyt Secret Messages machine, or HESM for short.")
sleep(.7)
print("Simply type \"Quit\" to stop.")
sleep(.7)
print("Good luck on your hacking adventures!")
sleep(.7)
while True:
    choice = input("Would you like to decode or encode a message?\n").lower()
    if len(choice) < 1:
        print("The heck are you doing?")
    elif choice[0] == "e":
        print(encode(input("What would you like to encode?\n")))
        print()
    elif choice[0] == "d":
        print(decode(input("What would you like to decode?\n")))
        print()
    elif choice == "quit":
        break
    else:
        print("..... what?")
        sleep(1)
