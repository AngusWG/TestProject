#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/4/23 10:33
# @Author  : zza
# @Email   : 740713651@qq.com
"""
python simple_cli.py -v -I foo/bar -Ispam/eggs x.cpp y.cpp z.cpp
python plumbum_cli.py x.cpp y.cpp z.cpp -v -I foo/bar -Ispam/eggs
"""
import logging

from plumbum import cli


class MyCompiler(cli.Application):
    verbose = cli.Flag(["-v", "--verbose"], help="Enable verbose mode")
    include_dirs = cli.SwitchAttr("-I", list=True, help="Specify include directories")

    @cli.switch("--loglevel", int)
    def set_log_level(self, level):
        """Sets the log-level of the logger"""
        logging.root.setLevel(level)

    def main(self, *srcfiles):
        print("Verbose:", self.verbose)
        print("Include dirs:", self.include_dirs)
        print("Compiling:", srcfiles)


if __name__ == "__main__":
    MyCompiler.run()
