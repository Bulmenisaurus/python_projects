import sys
import time
import pyautogui

"""
can be run with:
> python3 autoclicker_cli.py 5

to left click for 5 secs
"""

duration = sys.argv[1]
mouse_button = sys.argv[2] if len(sys.argv) >= 3 else 'left'

pyautogui.PAUSE = 0.001

print(f"Clicking for {duration} seconds with the {mouse_button} click button")
time.sleep(2)

start_time = time.time()
clicks = 0
while True:
    clicks += 10
    pyautogui.click(button=mouse_button, _pause=False, clicks=10)

    if (time.time() - start_time) > int(duration):
        break

print(f"Clicked {clicks} times with the {mouse_button} click button")
