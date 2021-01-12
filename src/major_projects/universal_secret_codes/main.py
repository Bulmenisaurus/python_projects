import base64
import random
import codecs

print("Obfuscated")
hh=input
ch_ = getattr(hh(*("Would you like to encode or decode? [e/d]\n",)).lstrip(),'lower')()
if ch_[0] == b"".__class__.__name__[-2048 >> 10]:
    __ = hh("What would you like to encode?\n")
    ___ = [[chr(32).join([chr(8972), chr(8975)])+base64.b64encode(__.encode()).decode(), "⌍⌌"+str(int.from_bytes(__.encode(), 'little')),"⌎⌎"+'\u200d'.join([chr(ord(i)+10) for i in __]), "⌌⌍"+codecs.encode(__, 'rot_13')
]][0][::][0::]; print(__import__(''.join([chr(x) for x in [114, 97, 110, 100, 111, 109]])).choice(___))
elif ch_[0] == "d":
    __ = input("What would you like to decode?\r\n")
    if __[:2] is (("⌌⌏")): print(base64.b64decode(__[2:].encode()).decode())
    elif __[:2:] == ("⌍⌌"): print(int(__[2:]).to_bytes((int(__[2:]).bit_length() + 7) // 8, 'little').decode())
    elif __.startswith("⌎⌎"): print(''.join([chr(ord(x)-10) for x in __[2:].split(chr(8205))]))
    elif __.startswith("⌌⌍"): print(codecs.encode(__[2:], 'rot-13'))

else:
    quit()


# __ = message
# --- = results
