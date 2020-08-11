# secret codes
# chr() int -> str, ord() str --> int
import random
from time import sleep


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
            try:
                decoded += chr((ord(str(i))-shift))
            except:
                print(f"{i} is bugged. :(")
    return decoded


print("Welcome to the Hackers Encrpyt Secret Messages machine, or HESM for short.")
sleep(.5)
print("Simply type \"Quit\" to stop.")
sleep(.5)
print("Good luck on your hacking adventures!")
sleep(.5)
while True:
    choice = input("Would you like to decode or encode a message?\n").lower()
    if choice[0] == "e":
        print(encode(input("What would you like to encode?\n")), "\n")
    elif choice[0] == "d":
        print(decode(input("What would you like to decode?\n")), "\n")
    elif choice == "quit":
        break
    else:
        sleep(1)
        print("..... what?")
