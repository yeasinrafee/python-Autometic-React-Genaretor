import pyautogui
import time

pyautogui.FAILSAFE = False
for i in range(0, 10):
    time.sleep(3)
    pyautogui.press('j')
    time.sleep(2)
    pyautogui.press('l')
    time.sleep(2)
    pyautogui.press('right')
    time.sleep(2)
    pyautogui.press('enter')