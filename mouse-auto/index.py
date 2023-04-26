import pyautogui as pg
import random
import time
import keyboard

while keyboard.is_pressed("q") == False:
    x = random.randint(600, 700)
    y = random.randint(600, 700)
    pg.moveTo(x, y, duration=0.5)
    time.sleep(2)