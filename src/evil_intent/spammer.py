import pyautogui
import pyperclip
import random
import time


"""
Spammer to-dos:

1. Generate 100 random unicode characters
2. Copy the characters to clipboard
3. Paste the `spam`
4. Repeat 1 - 3 20 more times
"""


def gen_spam(len_):
    return "".join([chr(random.randint(1000, 10000)) for _ in range(len_)])


time.sleep(5)
for _ in range(20):
    pyperclip.copy(gen_spam(100))
    pyautogui.hotkey('command', 'v', 'enter')
    time.sleep(.5)
