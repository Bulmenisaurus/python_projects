import base64
import random

"""
c is computer, u is user

c: Knock Knock
u: Who's there?
c: lena
u: leon who?
c: Lena a little closer, and I'll tell you another joke!
"""

# jokes automatically web-scraped from https://www.fatherly.com/play/funniest-knock-knock-jokes-kids/
def knock_encode(knock_joke):
    return "knock-knock{" + \
           ','.join([base64.b64encode(x.encode()).decode() for x in knock_joke])\
           + "}"


def knock_decode(b64_knock_joke: str):
    if b64_knock_joke.startswith('knock-knock{'):
        b64_knock_joke = b64_knock_joke[11:] \
            .replace('{', '(')\
            .replace('}', ')')

        return list(eval(b64_knock_joke))
    else:
        pass  # not a valid joke :(


def format_knock(knock_joke):
    print("Knock Knock!")
    input()
    print(knock_joke[0])
    input()
    print(knock_joke[1])


while True:
    print("""Would you like to:
    1) Listen to a random joke
    2) Listen to a joke someone else created
    3) Create a joke""")
    choice = input()

    if choice == '1':
        format_knock(random.choice(jokes))
    print()

