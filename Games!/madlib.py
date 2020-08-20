import random

madlib_num = random.randint(0, 0)


def inp(input_text):
    x = input(str(input_text)+"\n")
    return x


def madlib(num):
    ln = chr(10)  # cant put \ in f strings, have to improvise
    if num == 0:
        madlib_text = f"""It was a {inp("Input an adjective.")}, cold November day. 
I woke up to the {inp("Another adjective!")} smell of {inp("Some food now!")} cooking down in the kitchen. 
I {inp("Past tense verb now!")} down the stairs to see if I could help cook the {inp("Adjective?")} dinner. 
My mom said, \"See if {inp("A name now!")} needs a fresh {inp("Noun time!")}.\" So I carried a tray of 
glasses full of {inp("Your favorite food?")} into the {inp("Verb ending with -ing")} room. When I got there, I 
couldn't believe my {inp("Plural body part?")}! There were {inp("Plural noun, please!")} 
{inp("Verb ending with -ing")} on a {inp("Noun, now!")}!"""
    print(madlib_text)


madlib(0)

