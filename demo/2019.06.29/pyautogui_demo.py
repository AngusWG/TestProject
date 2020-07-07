#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/5/9 13:47
# @Author  : zza
# @Email   : 740713651@qq.com
import time

import pyautogui

# http://hugit.app/posts/doc-pyautogui.html

print('Press Ctrl-C to quit')
try:
    a = 0
    while True:
        x, y = pyautogui.position()
        x, y = [str(x).rjust(4) for x in [x, y]]
        positionStr = '{} X: {} Y: {}'.format(a, x, y)
        time.sleep(1)
        a += 1
        print(positionStr)
        # print('\b' * len(positionStr), end='', flush=True)

except KeyboardInterrupt:
    print('\n')
# : 2749 Y:  890X
# pyautogui.moveTo(1240, 757)
# for i in range(100):
#     pyautogui.doubleClick()
