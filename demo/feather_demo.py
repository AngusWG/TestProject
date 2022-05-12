#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2021/9/12 11:08
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : feather_demo.py

import feather
import numpy as np
import pandas as pd

np.random.seed = 42
df_size = 10000000

df = pd.DataFrame({
    'a': np.random.rand(df_size),
    'b': np.random.rand(df_size),
    'c': np.random.rand(df_size),
    'd': np.random.rand(df_size),
    'e': np.random.rand(df_size)
})
df.head()

feather.write_dataframe(df, '1M.feather')
df = feather.read_dataframe('1M.feather')

print(df)
