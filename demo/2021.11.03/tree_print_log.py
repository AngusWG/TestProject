#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2021/8/19 21:07
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : tree_print_log.py
"""
will print:

├── call func_c
│    ├── call func_b
│    │    ├── call func_a
│    │    ├── call func_a 2
│    │    └── call func_a 3
│    ├── call func_b 2
│    └── call func_b 3
├── call func_c 2
└── call func_c 3
"""
import inspect
import logging
import os


class TreePrintHandler(logging.Handler):
    def __init__(self, dir_name=os.path.basename(os.getcwd())):
        super().__init__()
        self.dir_name = dir_name
        self.last_deep = 0
        self.last_msg = None

    def emit(self, record: logging.LogRecord) -> None:
        # print(record)
        space = 0
        for i in inspect.stack():
            if self.dir_name in i.filename:
                space += 1
        deep = space - 3  # current Handler is in the stack
        if self.last_deep > deep:
            print("\r" + self.last_msg.replace("├", "└"), end="")
        self.last_msg = deep * "│    " + "├── " + record.msg
        print("\n" + self.last_msg, end="")
        self.last_deep = deep

    def __del__(self):
        print("\r" + self.last_msg.replace("├", "└"), end="")


logger = logging.getLogger("default")
logger.addHandler(TreePrintHandler(dir_name=os.path.basename(os.getcwd())))
logger.setLevel(logging.DEBUG)


def func_a():
    logger.info("call func_a")
    logger.info("call func_a 2")
    logger.info("call func_a 3")


def func_b():
    logger.info("call func_b")
    func_a()
    logger.info("call func_b 2")
    logger.info("call func_b 3")


def func_c():
    logger.info("call func_c")
    func_b()
    logger.info("call func_c 2")
    logger.info("call func_c 3")


if __name__ == '__main__':
    func_c()
