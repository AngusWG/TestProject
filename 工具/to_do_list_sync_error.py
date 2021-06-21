#!/usr/bin/python3
# encoding: utf-8
# @Time   : 2021-06-20 11:44:27
# @author : zza
# @Email  : z740713651@outlook.com
# @File   : to_do_list_sync_error.py
import os
import winreg

from typing import Optional


def get_todos_key() -> Optional[str]:
    reg_path = r"Software\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Mappings"
    access_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path)
    try:
        n = 0
        while True:
            sub_key_name = winreg.EnumKey(access_key, n)
            sub_key = winreg.OpenKey(access_key, sub_key_name)
            display_name = winreg.QueryValueEx(sub_key, "DisplayName")[0]
            # print(display_name)
            n += 1
            if "Todos" in display_name:
                print(display_name)
                print(sub_key_name)
                return sub_key_name
    except WindowsError:
        return None


def service() -> None:
    key = get_todos_key()
    if key is None:
        raise KeyError("Can't find Microsoft.Todos key in registry")
    command = f"CheckNetIsolation.exe loopbackexempt -a -p={key}"
    os.popen(command).read()
    result = os.popen("CheckNetIsolation.exe LoopbackExempt -s").read()
    assert key in result, "设置失败"
    print("设置成功")


if __name__ == "__main__":
    service()
