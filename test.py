import os
import time

from cv2 import cv2

import action

imgs = action.load_imgs(0.7)

a = "adb shell screencap -p sdcard/screen.jpg"
b = "adb pull sdcard/screen.jpg"
for row in [a, b]:
    time.sleep(0.5)
    os.system(row)
screen = cv2.imread('screen.jpg')

pts = action.locate(screen, imgs['jinbi2'], 1)
print(pts)

