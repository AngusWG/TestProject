#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/1/22 10:25
# @Author  : zza
# @Email   : 740713651@qq.com
import time
from importlib import import_module
from rqalpha.utils.config import get_mod_conf
import six


def get_info(v):
    title = "\n| name | opts | key | info | \n| :------ | ----- | ----- | ----- | \n"
    res = ""
    later_table = {}
    line = "| {} | {} | {} | {} |\n"
    for i in v:
        if "help" not in dir(i):
            i.help = ""
        key = i.name.rsplit("__", 1)[-1] if "__" in i.name else i.name

        if "__" in i.name:
            mod, name = i.name.rsplit("__", 1)
            i.name = "[{}] {}".format(mod.replace("__", "_"), name)
            if later_table.get(mod) is None:
                later_table[mod] = "* {} \n".format(mod) + title
            later_table[mod] += line.format(i.name, " , ".join(i.opts), key, i.help)
            continue
        res += line.format(i.name, " , ".join(i.opts), key, i.help)
    for k, v in later_table.items():
        res += v
    return title + res + "\n"


def save_to_file(res, file_name, add_time=True):
    if add_time is True:
        file_name += "_" + time.strftime("%Y%m%d", time.localtime())
    with open(file_name + ".md", "w", encoding="utf8") as f:
        f.write(res)
    return True


def server():
    modules = None
    mod_config = get_mod_conf()
    res = "# rqalpha param list \n"
    for mod_name, mod in six.iteritems(mod_config['mod']):
        if not mod_name.startswith("sys_"):
            modules = import_module("rqalpha_mod_" + mod_name)
    if modules is not None:
        for k, v in modules.cli.commands.items():
            info = get_info(v.params)
            if len(info) > 0:
                help_str = v.help.replace("\n\n", "\n").replace("\n", "\n> ")
                res += "### {}\n> {}\n{}---\n\n".format(v.name, help_str, info)
    print(res)
    return save_to_file(res, "rqalpha_param_list", add_time=True)


if __name__ == '__main__':
    server()
