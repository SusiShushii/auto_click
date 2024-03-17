import cv2
import numpy as np
import pyautogui
import os
def getResult(screen_img,template,threshold):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    second_tem = cv2.imread(template)
    template_gray = cv2.cvtColor(second_tem,cv2.COLOR_RGB2GRAY)
    template_w,template_h = template_gray.shape[::-1]
    
    screen_gray = cv2.cvtColor(screen_img, cv2.COLOR_RGB2GRAY)
    result = cv2.matchTemplate(screen_gray,template_gray,cv2.TM_CCOEFF_NORMED)
    locations = np.where(result>= threshold)
    locations = list(zip(*locations[::-1]))

    for pt in locations:
        print(locations)
        cv2.rectangle(screen_img, pt, (pt[0] + template_w, pt[1] + template_h), (0,255,0), thickness=2,lineType=cv2.LINE_4)
        cv2.imwrite("result.jpg",screen_img)
        pyautogui.click(x=pt[0]+template_w,y=pt[1]+template_h)
    