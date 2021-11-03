#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2021/8/25 9:46
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : pywinauto_demo.py


def pyautogui_demo():
    import time
    import pyautogui as pag

    # Below code will open the calculator.
    pag.press("winleft", _pause=True)  # will trigger left window key to open the start menu
    time.sleep(0.5)
    pag.typewrite("calculator", interval=0.2)  # it will type calculator in the search.
    time.sleep(0.5)
    pag.press("enter")  # it will trigger the enter key to open the calculator.
    time.sleep(0.5)
    # Below code will perform add operation on the calculator.
    pag.press("2")
    time.sleep(0.5)
    pag.press("+")
    time.sleep(0.5)
    pag.press("5")
    time.sleep(0.5)
    pag.press("+")
    time.sleep(0.5)
    pag.press("9")
    time.sleep(0.5)
    pag.press("enter")
    time.sleep(0.5)
    pag.press("esc")
    # Below code will perform subtraction operation on the calculator.


def pywinauto_demo():
    from pywinauto import Application, Desktop

    # 获取应用对象
    # 三种方式任选一种
    # 方式一：应用进程pid（连接）
    # pid= 12492
    # app = Application(backend='uia').connect(process=pid)
    # # 方式二：应用完整路径（连接）
    # app = Application(backend='uia').connect(path="D:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
    # # 方式三：打开应用（打开）
    # app = Application(backend='uia').start('D:\Program Files (x86)\Tencent\WeChat\WeChat.exe')

    app = Application(backend="uia").start('calc.exe')

    dlg = Desktop(backend="uia").计算器  # window specification
    dlg.type_keys('2*3=')
    dlg.print_control_identifiers()  # this is also window spec method

    dlg.minimize()
    # minimized window needs some tricks to find it and restore
    Desktop(backend="uia").window(title='计算器', visible_only=False).restore()


if __name__ == '__main__':
    pyautogui_demo()
    pywinauto_demo()
