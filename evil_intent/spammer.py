import pyautogui
import pyperclip
import random
import string
import time


pyautogui.FAILSAFE = True


def gen_spam(len_):
    return "".join([chr(random.randint(1000, 10000)) for _ in range(len_)])




time.sleep(5)
for _ in range(20):
    pyperclip.copy(gen_spam(100))
    pyautogui.hotkey('command', 'v', 'enter')
    time.sleep(.5)