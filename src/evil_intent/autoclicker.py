import pyautogui
import time

# sets click speed to be really, really fast
pyautogui.PAUSE = 0.001

while True:
    # So it can be re-used instead of running the project 1,000,000 times.
    input('Press ENTER to start ')
    time.sleep(2)
    timeStart = time.time()
    while True:
        pyautogui.click()

        if (time.time() - timeStart) > 15:
            break
