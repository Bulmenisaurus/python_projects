import base64
import random
import codecs


choice = input("Would you like to encode or decode? [e/d]\n")
if choice[0] == "e":
    message = input("What would you like to encode?\n")
    results = [
        "⌌⌏"+base64.b64encode(message.encode()).decode(),
        "⌍⌌"+str(int.from_bytes(message.encode(), 'little')),
        "⌎⌎"+'\u200d'.join([chr(ord(i)+10) for i in message]),
        "⌌⌍"+codecs.encode(message, 'rot_13')
    ]
    print(random.choice(results))
elif choice[0] == "d":
    message = input("What would you like to decode?\r\n")
    if message.startswith("⌌⌏"):
        print(base64.b64decode(message[2:].encode()).decode())
    elif message.startswith("⌍⌌"):
        print(int(message[2:]).to_bytes((int(message[2:]).bit_length() + 7) // 8, 'little').decode())
    elif message.startswith("⌎⌎"):
        print(''.join([chr(ord(x)-10) for x in message[2:].split(chr(8205))]))
    elif message.startswith("⌌⌍"):
        print(codecs.encode(message[2:], 'rot-13'))

else:
    quit()


