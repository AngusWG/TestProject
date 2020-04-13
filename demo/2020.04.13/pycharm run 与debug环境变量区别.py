#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/12/3 13:59
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : pycharm run 与debug环境变量区别.py
import os

print(dict(os.environ))
run_environ = {'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\ZZA\\AppData\\Roaming',
               'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files',
               'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files',
               'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'ZZA',
               'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData',
               'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default',
               'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\ZZA', 'IPYTHONENABLE': 'True', 'LC_ALL': 'fr_BE.UTF-8',
               'LOCALAPPDATA': 'C:\\Users\\ZZA\\AppData\\Local', 'LOGONSERVER': '\\\\ZZA', 'NUMBER_OF_PROCESSORS': '16',
               'ONEDRIVE': 'C:\\Users\\ZZA\\OneDrive', 'OS': 'Windows_NT',
               'PATH': 'D:\\Program Files\\JetBrains\\PyCharm 2019.2\\jbr\\\\bin;D:\\Program Files\\JetBrains\\PyCharm 2019.2\\jbr\\\\bin\\server;D:\\Programs\\Python\\Python36\\Scripts\\;D:\\Programs\\Python\\Python36\\;D:\\Programs\\Python\\Python37\\Scripts\\;D:\\Programs\\Python\\Python37\\;D:\\Programs\\Python\\Python37-32\\Scripts\\;D:\\Programs\\Python\\Python37-32\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;D:\\Program Files\\Git\\cmd;C:\\Program Files\\Pandoc\\;C:\\Users\\ZZA\\AppData\\Local\\Microsoft\\WindowsApps;D:\\Program Files\\protoc\\bin;C:\\Users\\ZZA\\AppData\\Local\\BypassRuntm;D:\\Program Files (x86)\\Microsoft VS Code\\bin;D:\\Programs\\Python\\Python37\\lib\\site-packages\\pywin32_system32;D:\\Programs\\Python\\Python37\\lib\\site-packages\\numpy\\.libs',
               'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW',
               'PROCESSOR_ARCHITECTURE': 'AMD64',
               'PROCESSOR_IDENTIFIER': 'AMD64 Family 23 Model 8 Stepping 2, AuthenticAMD', 'PROCESSOR_LEVEL': '23',
               'PROCESSOR_REVISION': '0802', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files',
               'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files',
               'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules',
               'PUBLIC': 'C:\\Users\\Public', 'PYCHARM_DISPLAY_PORT': '63342', 'PYCHARM_HOSTED': '1',
               'PYCHARM_MATPLOTLIB_INDEX': '0', 'PYCHARM_MATPLOTLIB_INTERACTIVE': 'true',
               'PYDEVD_LOAD_VALUES_ASYNC': 'True', 'PYTHONIOENCODING': 'UTF-8',
               'PYTHONPATH': 'D:\\PycharmProjects\\TestProject;D:\\PycharmProjects\\rqalpha;D:\\PycharmProjects\\rqalpha-internal;D:\\PycharmProjects\\rqalpha-internal-mods;D:\\PycharmProjects\\rqalpha-mod-ricequant-data;D:\\Program Files\\JetBrains\\PyCharm 2019.2\\helpers\\pycharm_matplotlib_backend;D:\\Program Files\\JetBrains\\PyCharm 2019.2\\helpers\\pycharm_display;D:\\Program Files\\JetBrains\\PyCharm 2019.2\\helpers\\third_party\\thriftpy;D:\\Program Files\\JetBrains\\PyCharm 2019.2\\helpers\\pydev',
               'PYTHONUNBUFFERED': '1',
               'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows',
               'TEMP': 'C:\\Users\\ZZA\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\ZZA\\AppData\\Local\\Temp',
               'USERDOMAIN': 'ZZA', 'USERDOMAIN_ROAMINGPROFILE': 'ZZA', 'USERNAME': 'ZZA',
               'USERPROFILE': 'C:\\Users\\ZZA', 'WINDIR': 'C:\\Windows'}

debug_environ = {'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\ZZA\\AppData\\Roaming',
                 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files',
                 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files',
                 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'ZZA',
                 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe',
                 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData',
                 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default',
                 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\ZZA',
                 'IDE_PROJECT_ROOTS': 'D:/PycharmProjects/TestProject;D:/PycharmProjects/rqalpha;D:/PycharmProjects/rqalpha-internal;D:/PycharmProjects/rqalpha-internal-mods;D:/PycharmProjects/rqalpha-mod-ricequant-data',
                 'IPYTHONENABLE': 'True', 'LC_ALL': 'fr_BE.UTF-8',
                 'LIBRARY_ROOTS': 'D:/Programs/Python/Python37/DLLs;D:/Programs/Python/Python37/Lib;D:/Programs/Python/Python37;C:/Users/ZZA/AppData/Roaming/Python/Python37/site-packages;D:/Programs/Python/Python37/Lib/site-packages;D:/PycharmProjects/rqutils;D:/PycharmProjects/rqalpha-internal-mods/rqalpha-mod-control;D:/PycharmProjects/rqalpha-internal-mods/rqalpha-mod-indicator;D:/PycharmProjects/rqalpha-internal-mods/rqalpha-mod-auth;D:/PycharmProjects/rqalpha-internal-mods/rqalpha-mod-feeder;D:/PycharmProjects/rqpms;D:/PycharmProjects/rqopen-client;D:/PycharmProjects/rqalpha-internal-mods/rqalpha-mod-optimizer;D:/PycharmProjects/portfolio-calc;D:/PycharmProjects/rqams-utils;D:/PycharmProjects/rqportal-internal;D:/PycharmProjects/ricequant-protobuf/python;D:/PycharmProjects/contest-api-server;D:/PycharmProjects/rqlicense/rqlicense-server;D:/Programs/Python/Python37/Lib/site-packages/win32;D:/Programs/Python/Python37/Lib/site-packages/win32/lib;D:/Programs/Python/Python37/Lib/site-packages/pythonwin;C:/Users/ZZA/.PyCharm2019.2/system/python_stubs/201831395;D:/Program Files/JetBrains/PyCharm 2019.2/helpers/python-skeletons;D:/Program Files/JetBrains/PyCharm 2019.2/helpers/typeshed/stdlib/3;D:/Program Files/JetBrains/PyCharm 2019.2/helpers/typeshed/stdlib/2and3;D:/Program Files/JetBrains/PyCharm 2019.2/helpers/typeshed/third_party/3;D:/Program Files/JetBrains/PyCharm 2019.2/helpers/typeshed/third_party/2and3',
                 'LOCALAPPDATA': 'C:\\Users\\ZZA\\AppData\\Local', 'LOGONSERVER': '\\\\ZZA',
                 'NUMBER_OF_PROCESSORS': '16', 'ONEDRIVE': 'C:\\Users\\ZZA\\OneDrive', 'OS': 'Windows_NT',
                 'PATH': 'D:\\Program Files\\JetBrains\\PyCharm 2019.2\\jbr\\\\bin;D:\\Program Files\\JetBrains\\PyCharm 2019.2\\jbr\\\\bin\\server;D:\\Programs\\Python\\Python36\\Scripts\\;D:\\Programs\\Python\\Python36\\;D:\\Programs\\Python\\Python37\\Scripts\\;D:\\Programs\\Python\\Python37\\;D:\\Programs\\Python\\Python37-32\\Scripts\\;D:\\Programs\\Python\\Python37-32\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;D:\\Program Files\\Git\\cmd;C:\\Program Files\\Pandoc\\;C:\\Users\\ZZA\\AppData\\Local\\Microsoft\\WindowsApps;D:\\Program Files\\protoc\\bin;C:\\Users\\ZZA\\AppData\\Local\\BypassRuntm;D:\\Program Files (x86)\\Microsoft VS Code\\bin;D:\\Programs\\Python\\Python37\\lib\\site-packages\\pywin32_system32;D:\\Programs\\Python\\Python37\\lib\\site-packages\\numpy\\.libs',
                 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW',
                 'PROCESSOR_ARCHITECTURE': 'AMD64',
                 'PROCESSOR_IDENTIFIER': 'AMD64 Family 23 Model 8 Stepping 2, AuthenticAMD', 'PROCESSOR_LEVEL': '23',
                 'PROCESSOR_REVISION': '0802', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files',
                 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files',
                 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules',
                 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM_DISPLAY_PORT': '63342', 'PYCHARM_HOSTED': '1',
                 'PYDEVD_LOAD_VALUES_ASYNC': 'True', 'PYTHONDONTWRITEBYTECODE': '1', 'PYTHONIOENCODING': 'UTF-8',
                 'PYTHONPATH': 'D:\\PycharmProjects\\TestProject;D:\\PycharmProjects\\rqalpha;D:\\PycharmProjects\\rqalpha-internal;D:\\PycharmProjects\\rqalpha-internal-mods;D:\\PycharmProjects\\rqalpha-mod-ricequant-data;D:\\Program Files\\JetBrains\\PyCharm 2019.2\\helpers\\pycharm_matplotlib_backend;D:\\Program Files\\JetBrains\\PyCharm 2019.2\\helpers\\pycharm_display;D:\\Program Files\\JetBrains\\PyCharm 2019.2\\helpers\\third_party\\thriftpy;D:\\Program Files\\JetBrains\\PyCharm 2019.2\\helpers\\pydev;C:\\Users\\ZZA\\.PyCharm2019.2\\system\\cythonExtensions;D:/PycharmProjects/TestProject/demo',
                 'PYTHONUNBUFFERED': '1',
                 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows',
                 'TEMP': 'C:\\Users\\ZZA\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\ZZA\\AppData\\Local\\Temp',
                 'USERDOMAIN': 'ZZA', 'USERDOMAIN_ROAMINGPROFILE': 'ZZA', 'USERNAME': 'ZZA',
                 'USERPROFILE': 'C:\\Users\\ZZA', 'WINDIR': 'C:\\Windows'}

console_environ = {'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\ZZA\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'ZZA', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\ZZA', 'IPYTHONENABLE': 'True', 'LC_ALL': 'fr_BE.UTF-8', 'LOCALAPPDATA': 'C:\\Users\\ZZA\\AppData\\Local', 'LOGONSERVER': '\\\\ZZA', 'NUMBER_OF_PROCESSORS': '16', 'ONEDRIVE': 'C:\\Users\\ZZA\\OneDrive', 'OS': 'Windows_NT', 'PATH': 'D:\\Program Files\\JetBrains\\PyCharm 2019.2\\jbr\\\\bin;D:\\Program Files\\JetBrains\\PyCharm 2019.2\\jbr\\\\bin\\server;D:\\Programs\\Python\\Python36\\Scripts\\;D:\\Programs\\Python\\Python36\\;D:\\Programs\\Python\\Python37\\Scripts\\;D:\\Programs\\Python\\Python37\\;D:\\Programs\\Python\\Python37-32\\Scripts\\;D:\\Programs\\Python\\Python37-32\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;D:\\Program Files\\Git\\cmd;C:\\Program Files\\Pandoc\\;C:\\Users\\ZZA\\AppData\\Local\\Microsoft\\WindowsApps;D:\\Program Files\\protoc\\bin;C:\\Users\\ZZA\\AppData\\Local\\BypassRuntm;D:\\Program Files (x86)\\Microsoft VS Code\\bin;D:\\Programs\\Python\\Python37\\lib\\site-packages\\pywin32_system32;D:\\Programs\\Python\\Python37\\lib\\site-packages\\numpy\\.libs', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'AMD64 Family 23 Model 8 Stepping 2, AuthenticAMD', 'PROCESSOR_LEVEL': '23', 'PROCESSOR_REVISION': '0802', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM_DISPLAY_PORT': '63342', 'PYCHARM_HOSTED': '1', 'PYCHARM_MATPLOTLIB_INDEX': '0', 'PYCHARM_MATPLOTLIB_INTERACTIVE': 'true', 'PYDEVD_LOAD_VALUES_ASYNC': 'True', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'D:\\Program Files\\JetBrains\\PyCharm 2019.2\\helpers\\pycharm_matplotlib_backend;D:\\Program Files\\JetBrains\\PyCharm 2019.2\\helpers\\pycharm_display;D:\\Program Files\\JetBrains\\PyCharm 2019.2\\helpers\\third_party\\thriftpy;D:\\Program Files\\JetBrains\\PyCharm 2019.2\\helpers\\pydev', 'PYTHONUNBUFFERED': '1', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\ZZA\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\ZZA\\AppData\\Local\\Temp', 'USERDOMAIN': 'ZZA', 'USERDOMAIN_ROAMINGPROFILE': 'ZZA', 'USERNAME': 'ZZA', 'USERPROFILE': 'C:\\Users\\ZZA', 'WINDIR': 'C:\\Windows'}


run_environ_set = set(run_environ.keys())
debug_environ_set = set(debug_environ.keys())
console_environ_set = set(console_environ.keys())
def_key = debug_environ_set.difference(run_environ_set)
for key in def_key:
    print("key: ", key)
    print(run_environ.get(key))
    print(debug_environ[key])

print("def_key", list(def_key))
