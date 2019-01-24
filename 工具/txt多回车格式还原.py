#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/1/24 13:32
# @Author  : zza
# @Email   : 740713651@qq.com


def server(_path):
    with open(_path, "r", encoding="utf8") as f:
        txt = f.readlines()
    res = ""
    for line in txt:
        _line = line.replace("\n", "")
        if _line[-1] in ['。']:
            res += _line + "\n"
        elif len(_line) is 0:
            res += _line + "\n"
        else:
            res += _line
    print(res)
    with open(_path.replace(".", "_bak."), "w", encoding="utf8") as f:
        f.write(res)
    print(_path.replace(".", "_bak."))


if __name__ == '__main__':
    server(r"C:\Users\admin\Desktop\卢瑟经济学.txt")
