# secret codes
# chr() int -> str, ord() str --> int
import random


def encode(encode_input):
    shift = random.randint(0, 15000)
    encoded = chr(shift+1500)  # to make it seem more random
    print(shift)
    for i in encode_input:
        encoded += chr((ord(str(i))+shift))
    return encoded


while True:
    print(encode(input()))