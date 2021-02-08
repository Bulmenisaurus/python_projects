from pyautogui import write, press, FailSafeException
from time import time, sleep
from random import random, randint, choice


def submit(text: str):
    """
    Helper function to write some text

    :param text: The text to be written
    :return: Absolutely nothing
    """
    write(text, interval=.025)
    press("enter")


# images and currency
class BotCommands:
    """
    A class for all the different commands.
    It keeps track of how many commands have been sent.
    """
    def __init__(self):
        self.commands_sent = 0

    def beg(self):
        submit("pls beg")
        self.commands_sent += 1

    def pm(self):
        submit("pls pm")
        sleep(2)
        submit(choice("frick"))
        self.commands_sent += 1

    def hunt(self):
        submit("pls hunt")
        sleep(9)
        self.commands_sent += 1

    def fish(self):
        submit("pls fish")
        sleep(9)
        self.commands_sent += 1

    def highlow(self):
        submit("pls highlow")
        sleep(2)
        submit(choice(("high", "low")))
        self.commands_sent += 1

    def gamble(self):
        submit(f"pls gamble {randint(420, 690)}")
        self.commands_sent += 1

    def triv(self):
        submit("pls triv")
        sleep(2)
        submit(f"{choice(['A', 'B', 'C', 'D'])}")
        self.commands_sent += 1

    def inv(self):
        submit(f"pls inv {choice(['1', '2', '3', '4'])}")
        self.commands_sent += 1

    def pet_pat(self):
        submit("pls pet pat")
        self.commands_sent += 1

    def image(self):
        choices = ['animals', 'aww', 'ducc', 'redpanda', 'snek', 'hoppyboi', 'kitty', 'ferret', 'foxxy', 'otter']
        submit(f"pls {choice(choices)}")
        self.commands_sent += 1

    def profile(self):
        submit("pls profile")
        self.commands_sent += 1

    def shop(self):
        submit(f"pls shop {randint(2, 4) if randint(0, 1) else ''}")
        self.commands_sent += 1

    def fun(self):
        fun = ['simprate', 'uselessweb', 'waifu']
        submit(f'pls {choice(fun)}')
        self.commands_sent += 1

    def memey(self):
        category = ['4chan', 'antiantijoke', 'antijoke', 'facepalm', 'meme', 'pun', 'surreal', 'xkcd']
        submit(f"pls {choice(category)}")
        self.commands_sent += 1


p = BotCommands()
# This just initializes the different cool downs of different commands
delays = {p.beg: 45, p.pm: 60, p.hunt: 60, p.fish: 60, p.highlow: 20, p.gamble: 50, p.triv: 25, p.inv: 70,
          p.pet_pat: 100, p.image: 15, p.profile: 40, p.shop: 20, p.fun: 22, p.memey: 20}

commands = {}
for command in delays.keys():
    commands[command] = time()

sleep(3)
submit("pls bal")
start_time = time()
while True:
    sleep(.75)
    for command in commands.items():  # command = (function, time when unlocks)
        try:
            if command[1] < time():
                sleep(.5)
                command[0]()
                commands[command[0]] = time() + delays[command[0]]  # resets value
                break  # so not too many commands at once
        except FailSafeException:
            print(f"{p.commands_sent} command[s] have been sent in {time() - start_time} seconds.")
            raise
