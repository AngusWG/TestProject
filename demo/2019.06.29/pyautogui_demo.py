#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/5/9 13:47
# @Author  : zza
# @Email   : 740713651@qq.com
import pyautogui

# http://hugit.app/posts/doc-pyautogui.html
print('Press Ctrl-C to quit')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: {} Y: {}'.format(*[str(x).rjust(4) for x in [x, y]])
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
