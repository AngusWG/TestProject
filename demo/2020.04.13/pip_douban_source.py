#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2020/4/13 14:12
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : pip_douban_source.py
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c13/p10_read_configuration_files.html
# https://www.jianshu.com/p/0cdd647bcc3e
"""
python -c "import requests;res = requests.get('http://cdn.ricequant.com/rqpro/pip_douban_source_v2.py');exec(res.text)"
"""

import os
import sys

from configparser import ConfigParser

conf_dir = os.path.join(os.path.expanduser("~"), ".pip")
os.makedirs(conf_dir, exist_ok=True)
WINDOWS = (sys.platform.startswith("win") or (sys.platform == 'cli' and os.name == 'nt'))
CONFIG_BASENAME = 'pip.ini' if WINDOWS else 'pip.conf'
conf_path = os.path.join(conf_dir, CONFIG_BASENAME)

cfg = ConfigParser()
cfg.read(conf_path, encoding="utf8")

if not cfg.has_section('global'):
    cfg.add_section('global')

cfg.set('global', 'index-url', 'http://pypi.douban.com/simple')
cfg.set('global', 'trusted-host', 'pypi.douban.com')
cfg.set('global', 'timeout', "60")

if not WINDOWS:
    if not cfg.has_section('install'):
        cfg.add_section('install')
    cfg.set("install", "use-mirrors", "true")
    cfg.set("install", "mirrors", "https://pypi.douban.com/simple/")
    cfg.set("install", "trusted-host", "pypi.douban.com")

with open(conf_path, "w", encoding="utf8:") as f:
    cfg.write(f)

print("save to {}".format(conf_path))
