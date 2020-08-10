import random

madlib_num = random.randint(0, 0)


def madlib(num):
    ln = chr(10)  # cant put \ in f strings, have to improvise
    if num == 0:
        madlib_text = f"""It was a {input("Input an adjective."+ln)}, cold November day. 
I woke up to the {input("Another adjective!"+ln)} smell of {input("Some food now!"+ln)} roasting in the kitchen downstairs. 
I {input("Past tense verb now!"+ln)} down the stairs to see if I could help cook the {input("Adjective?"+ln)} dinner. 
My mom said, \"See if {input("A name, now!"+ln)} needs a fresh {input("Noun time!"+ln)}.\" So I carried a tray of 
glasses full of {input("Your fav food?"+ln)} into the {input("Verb ending with -ing!"+ln)} room. When I got there, I 
couldn't believe my {input("Plural body part."+ln)}! There were {input("Pluran noun!!"+ln)} 
{input('Verb that ends with -ing!'+ln)} on a {input("Noun!"+ln)}!"""
    print(madlib_text)


madlib(0)

