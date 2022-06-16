import pyautogui
import time

time.sleep(1)
pyautogui.press('winleft')
pyautogui.write('paint')
pyautogui.press('enter')

pyautogui.moveTo(400, 400)

pyautogui.click()
distance = 100

time.sleep(2)


while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)  # move right
    distance = distance - 10
    pyautogui.dragRel(0, distance, duration=0.2)  # move down

    pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
    distance = distance - 10

    pyautogui.dragRel(0, -distance, duration=0.2)  # move up