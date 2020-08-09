import random

madlib_num = random.randint(0, 0)


def madlib(num):
    ln = chr(10)  # cant put \ in f strings, have to improvise
    if num == 0:
        madlib = f"""It was a {input('Enter an adjective!' + ln)}, cold November day. 
I woke up to the {input("Anotha adjective!"+ ln)}"""
    print(madlib)


madlib(0)

