#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/2/19 18:26
# @Author  : zza
# @Email   : 740713651@qq.com
from ruamel import yaml

config_yaml_path = r"C:\Users\admin\Desktop\fsdownload\config.yaml"
new_yaml_path = r"C:\Users\admin\Desktop\fsdownload\new_config.yaml"
py_config_path = r"C:\Users\admin\Desktop\fsdownload\config.py"

file_dict = yaml.load(open(config_yaml_path, "r", encoding="utf8").read())
py_file = open(py_config_path, 'r', encoding="utf-8").read()

# 检查py代码
compile(py_file, "config,py", "exec")
file_dict["data"]["config.py"] = py_file
with open(new_yaml_path, "w", encoding="utf-8") as f:
    yaml.dump(file_dict, f,Dumper=yaml.RoundTripDumper)

print("finish")
