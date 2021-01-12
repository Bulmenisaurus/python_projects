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
jokes = [('Leon', 'Leon me when you’re not strong!'), ('Annie', 'Annie thing you can do I can better!'), ('Lena', 'Lena a little closer, and I’ll tell you another joke!'), ('Quiche', 'Can I have a hug and a quiche?'), ('Wa', 'What are you so excited about?!'), ('Adore', 'Adore is between you and me so please open up!'), ('I am', 'Don’t you even know who you are?!'), ('A leaf.', ''), ('Hike', 'I didn’t know you liked Japanese poetry!'), ('A little old lady', 'Wow, I didn’t know you could yodel!'), ('Ice cream soda ', 'Ice scream soda people can hear me!'), ('Candice ', 'Candice joke get any worse?!'), ('Haven', 'Haven you heard enough of these knock-knock jokes?'), ('Double', 'W!'), ('Anita', 'Anita drink of water so please let me in!'), ('Banana', 'Orange you glad I didn’t say banana?'), ('Alex', 'Alex-plain when you open the door!'), ('Olive.', 'Olive next door. Hi neighbor!'), ('Keith', 'Keith me, my thweet prince!'), ('Europe', 'No, you’re a poo!'), ('Hawaii', 'I’m fine, Hawaii you?'), ('Nun', 'Nunya business!'), ('June', 'June know how long I’ve been knocking out here?'), ('Spell', 'W-H-O!'), ('Anita who?', 'Anita go to the bathroom!'), ('Dejav ', 'Knock, knock'), ('Owls say', 'Yes, they do.'), ('Cargo', 'Cargo beep, beep and vroom, vroom!'), ('To', 'No, it’s to whom!'), ('Cash', 'No thanks, but I’d love some peanuts.'), ('Mustache', 'Mustache you a question, but I’ll shave it for later!'), ('Dwayne', 'Dwayne the bathtub ⏤ I’m dwowning!'), ('Ya', 'No thanks, I use Bing or Google.'), ('Control Freak', 'Okay, now you say control freak who?'), ('Billy Bob Joe Penny', 'Really? How many Billy Bob Joe Pennies do you know?'), ('Theodore', 'Theodore wasn’t opened so I knocked.'), ('Alec', 'Alec it when you ask me questions. '), ('Cereal', 'Cereal pleasure to meet you!'), ('Cantaloupe', 'Cantaloupe to Vegas, you’re too young!'), ('Beats', 'Beats me. '), ('Kenya', 'Kenya feel the love tonight?'), ('Interrupting sloth', 'Sloooooooooth'), ('Ida', 'Surely, it’s pronounced Idaho.'), ('Art', 'R2-D2!'), ('Smellmop', 'Ew, no thanks!'), ('I need a puh', 'Then why don’t you find a toilet! '), ('Hatch', 'God bless you!'), ('Tank', 'You’re welcome.'), ('Voodoo', 'Voodoo you think you are asking me so many questions?'), ('Boo', 'Uh, why are you crying?'), ('Opportunity ', 'Opportunity doesn’t knock twice!'), ('Honeybee', 'Honeybee a dear and open up will you?'), ('Says', 'Says me, that’s who!'), ('Alice', 'Alice so quiet. Let’s make some noise!'), ('Iran', 'Iran all the way here!'), ('Doctor', 'No, no, just the doctor.'), ('Euripides ', 'Euripides jeans and you pay for them, okay?'), ('Amish', 'Really, you’re a shoe? Uh, okay. '), ('Figs', 'Figs the doorbell!'), ('Dishes', ''), ('Lettuce.', 'Lettuce in or we’ll break down the door!'), ('Razor', 'Razor hand and dance the boogie!'), ('I am', 'So you have identity problems, huh?'), ('Luke', 'Luke through the keyhole and see!'), ('Amos', 'A mosquito!'), ('Howard', 'Howard I know?'), ('Odysseus', 'Odysseus the last straw!'), ('A Mayan', 'A Mayan in the way?'), ('Abe', 'Abe-C-D-E!'), ('Icing', 'Icing so loudly so everyone can hear me!'), ('Tennis', 'Tennis five plus five!'), ('…', 'Snow use, I forgot my name again. '), ('Nicholas', 'A Nicholas is not much money these days.'), (' Candice', ' Candice door open or am I stuck out here?'), ('Cow', 'No cow says mooooooo!'), ('Robin', 'Robin you! Now hand over the cash'), ('Annie', 'Annie way you can let me in?'), ('Canoe', 'Canoe come and play? I’m bored!'), ('Gorilla', 'Gorilla me a hamburger!'), ('Snow', 'Snow who?'), ('Kanga', 'Actually it’s Kangaroo'), ('A broken pencil', 'Never mind it’s pointless'), ('Cabbage', 'You expect a cabbage to have a last name?'), ('You didn’t remember me!', 'You didn’t remember me!'), ('Sweden', 'Sweden sour chicken!'), ('Alpaca', 'Alpaca the trunk, you pack the suitcase.'), ('Pecan', 'Pecan someone your own size.')]

def knock_encode(knock_joke):
    return "knock-knock{" + \
           ','.join(["\'" + base64.b64encode(x.encode()).decode()+"\'" for x in knock_joke])\
           + "}"


def knock_decode(b64_knock_joke: str):
    if b64_knock_joke.startswith('knock-knock{'):
        b64_knock_joke = b64_knock_joke[11:] \
            .replace('{', '(')\
            .replace('}', ')')

        return [base64.b64decode(x).decode() for x in list(eval(b64_knock_joke))]
    else:
        return False


def format_knock(knock_joke):
    print("Knock Knock!")
    input()
    print(knock_joke[0].strip())
    input()
    print(knock_joke[1].strip())


while True:
    print("""Would you like to:
    1) Listen to a random joke
    2) Listen to a joke someone else created
    3) Create a joke""")
    choice = input()

    print()
    if choice == '1':
        format_knock(random.choice(jokes))
    elif choice == '2':
        joke = input("Enter your joke here: \n")
        joke_loaded = knock_decode(joke.strip())
        if joke_loaded:
            print("Joke loading succesful. \n\n")
            format_knock(joke_loaded)
        else:
            print("Something went wrong. Make sure your joke looks similar to:\nknock-knock{UXVhY2s=,"
                  "UXVhY2sgUXVhY2s=}")
    elif choice == '3':
        joke = ['', '']
        print("you: Knock knock\nuser: Who's there?")
        joke[0] = input("you: ")
        print("user: " + joke[0] + " who?")
        joke[1] = input("you: ")

        generated_joke = knock_encode(joke)
        print("Here is your generated joke:\n ", generated_joke)

    print()

