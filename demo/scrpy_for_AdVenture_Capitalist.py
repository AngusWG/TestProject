import time
import sys
import pyautogui
from pynput.keyboard import Listener


pos_list = [
    (1032 ,490),
    (1025 ,619),
    (1032 ,753),
    (1044 ,879),
    (1059 ,1001),
    (1459 ,494),
    (1474 ,625),
    (1479 ,746),
    (1479 ,870),
    (1478 ,998),
]


def press(key):
    key = str(key)
    print(type(key),key)
    x, y = pyautogui.position()
    print((x, y))
    if key == "Key.esc":
        sys.exit()
    elif key == "a":
        pos_list.append((x, y))
        print(len(pos_list))
    elif key == "s":
        while True:
            click_game()
            time.sleep(1)




def click_game():
    for x, v in pos_list:
        pyautogui.moveTo(x, v)  # 移动鼠标到指定位置
        pyautogui.click()  # 单击


def service():
    while True:
        with Listener(on_press=press) as listener:
            listener.join()



if __name__ == "__main__":
    service()
    # get_position()
    # click_game()
