import pyautogui
with open(__file__, "r") as f:
    pyautogui.typewrite(f.read(), 0)
    pyautogui.hotkey('command', 'c', 'left')
