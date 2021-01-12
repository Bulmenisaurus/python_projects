import pyautogui
import time
from random import randint

s = time.time()
while True:
    time.sleep(15)
    pyautogui.moveTo(randint(100, 150), randint(100, 150))
    if (time.time() - s) > 1800:
        quit()