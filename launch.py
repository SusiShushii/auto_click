import cv2
import pyautogui
import pydirectinput
import numpy as np
from time import time,sleep
from windowcapture import WindowCapture
import os
import compareimage

os.chdir(os.path.dirname(os.path.abspath(__file__)))
wincap = WindowCapture('FC ONLINE')
template = cv2.imread("p1.png")
template_gray = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
template_w, template_h = template_gray.shape[::-1]
threshold =0.96
loop_time = time()

while(True):

    screenshot = wincap.get_screenshot()
    

    cv2.imshow('Computer Vision',screenshot)
    compareimage.getResult(screenshot,"p1.png",0.90)
    sleep(1)
    


    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break
print('Done.')
