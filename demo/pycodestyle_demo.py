# encoding: utf-8
# @Time   : 2021/7/5 9:19
# @author : zza
# @Email  : 740713651@qq.com
# @File   : pycodestyle_demo.py

"""
# https://zhuanlan.zhihu.com/p/386617187

# Install pycodestyle
pip install pycodestyle numpy pandas

pycodestyle --statistics -qq pycodestyle_demo.py
"""

# pycodestyle_sample_script.py
# Import libraries
import numpy as np, pandas as pd

# Take the users input
words = input("Enter some text to translate to pig latin: " )
# Break apart the words into a list
words_list = words.split(' ' )
for word in words_list:
    if len(word) >= 3 : # For this pig latin translation, we only want to translate words greater than 3 characters
        pig_latin = word + "%say" % (word[0])
        pig_latin = pig_latin[ 1: ]
        print(pig_latin )
    else:
        pass