import pyautogui
import time

pyautogui.PAUSE = 0.001

while True:
    input('Press ENTER to start ')
    time.sleep(2)
    timeStart = time.time()
    while True:
        pyautogui.click()

        if (time.time() - timeStart) > 15:
            break
