import os

import sys


def get_local_file():
    res_list = []
    for i in os.listdir():
        if os.path.isfile(i):
            if "." not in i:
                res_list.append(i)
    return res_list


def change_name(add_name, file__list):
    for i in file__list:
        os.rename(i, i + add_name)
    return True


def main():
    file_List = get_local_file()
    if not file_List:
        return False
    res = change_name(".mp4", file_List)
    if res:
        print("succes")
    else:
        print("false")
    return True


if __name__ == '__main__':

    input()
    print(main())
    input()
