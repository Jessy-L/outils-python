#This script saves the image of the region 660,350,600,400 as savedimage.png in the path "C:\Users\Antec\Desktop\Tutorial\savedimage.png"

import pyautogui

im1 = pyautogui.screenshot(region=(660,380,600,420))
im1.save(r"./joi.jpg")
