#!/usr/bin/env python
# encoding: utf-8
# Created by zza on 2021/6/21 9:45
# Copyright 2021 LinkSense Technology CO,. Ltd
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


if __name__ == "__main__":
    service()
