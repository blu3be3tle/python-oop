import pyautogui
import time

n = int(input("Enter number of lines: "))
time.sleep(3)

for i in range(1, n + 1):
    pyautogui.typewrite('#' * i)
    pyautogui.press('enter')
