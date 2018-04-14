#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/3/7 0007 17:30
# @author  : zza
# @Email   : 740713651@qq.com
# 资料来源  https://blog.csdn.net/mycafe_/article/details/79146764#基本使用方法如下
# 可以使用上面提到的各种推荐系统算法
from __future__ import (absolute_import, division, print_function,unicode_literals)

from surprise import SVD
from surprise import Dataset
from surprise import evaluate, print_perf

# # 默认载入movielens数据集
# data = Dataset.load_builtin('ml-100k')
# # k折交叉验证(k=3)
# data.split(n_folds=3)
# # 试一把SVD矩阵分解
# algo = SVD()
# # 在数据集上测试一下效果
# perf = evaluate(algo, data, measures=['RMSE', 'MAE'])
# #输出结果
# print_perf(perf)

"""
以下的程序段告诉大家如何在协同过滤算法建模以后，根据一个item取回相似度最高的item，主要是用到algo.get_neighbors()这个函数
"""

import os
import io

from surprise import KNNBaseline
from surprise import Dataset


def read_item_names():
    """
    获取电影名到电影id 和 电影id到电影名的映射
    """

    file_name = (os.path.expanduser('~') +
                 '/.surprise_data/ml-100k/ml-100k/u.item')
    rid_to_name = {}
    name_to_rid = {}
    with io.open(file_name, 'r', encoding='ISO-8859-1') as f:
        for line in f:
            line = line.split('|')
            rid_to_name[line[0]] = line[1]
            name_to_rid[line[1]] = line[0]

    return rid_to_name, name_to_rid


# 首先，用算法计算相互间的相似度
data = Dataset.load_builtin('ml-100k')
trainset = data.build_full_trainset()
sim_options = {'name': 'pearson_baseline', 'user_based': False}
algo = KNNBaseline(sim_options=sim_options)
algo.train(trainset)

# 获取电影名到电影id 和 电影id到电影名的映射
rid_to_name, name_to_rid = read_item_names()

# Retieve inner id of the movie Toy Story
toy_story_raw_id = name_to_rid['Toy Story (1995)']
toy_story_inner_id = algo.trainset.to_inner_iid(toy_story_raw_id)

# Retrieve inner ids of the nearest neighbors of Toy Story.
toy_story_neighbors = algo.get_neighbors(toy_story_inner_id, k=10)

# Convert inner ids of the neighbors into names.
toy_story_neighbors = (algo.trainset.to_raw_iid(inner_id)
                       for inner_id in toy_story_neighbors)
toy_story_neighbors = (rid_to_name[rid]
                       for rid in toy_story_neighbors)

print()
print('The 10 nearest neighbors of Toy Story are:')
for movie in toy_story_neighbors:
    print(movie)