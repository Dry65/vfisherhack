import pyautogui
from time import sleep

prefix = input("Input your prefix: ")
time = float(input("Input your time: "))
repeat = int(input("0 = infinity or a number to time repeat: "))
if repeat < 0:
    repeat = 0

print(f"Prefix:{prefix} -- Time:{time} -- Repeat: {repeat}")
print("Just put mouse in Discord icon on taskbar (in correct channel to start fish) and see the magic")

sleep(2)
pyautogui.click()

if repeat > 0:
    for x in repeat:
        repeat -=1
        pyautogui.write(f"{prefix}fish")
        pyautogui.press("enter")
        sleep(time)
else:
    while True:
        pyautogui.write(f"{prefix}fish")
        pyautogui.press("enter")
        sleep(time)