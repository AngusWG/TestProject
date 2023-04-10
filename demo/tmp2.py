#!/usr/bin/python3
# encoding: utf-8
# @Time    : 2021/9/15 10:54
# @author  : zza
# @Email   : 740713651@qq.com

import sys

# n = int(sys.stdin.readline().strip())
# nodelist = []
# for i in range(n):
#     # 读取每一行
#     node_str = sys.stdin.readline().strip()
#     # 把每一]行的数字分隔后转化成int列表
#     x, y = node_str.split(",")
#     node = int(x), int(y)
from pprint import pprint

nodelist = [(1, 4), (2, 5), (3, 6)]
nodelist = sorted(nodelist, key=lambda x: x[0])
n = len(nodelist)

stack = []
stack_x = 0
stack_y = 0
count = 0

while nodelist:
    node = nodelist.pop(0)
    if not stack:
        stack.append(node)
        stack_x = node[0]
        stack_y = node[1]
        count += 1
    else:
        if not (stack_x <= node[0] < stack_y):
            stack = [node]
            stack_x = node[0]
            stack_y = node[1]
            count += 1
        elif stack_x <= node[0] <= node[1] <= stack_y:
            continue
        elif node[1] > stack_y:
            while len(stack) > 1:
                stack_node = stack.pop()
                if not (stack[-1][0] <= node[0] <= stack[-1][1]):
                    stack.append(stack_node)
                    stack.append(node)
                    count += 1
                    break
                else:
                    count -= 1
            if stack[-1] != node:
                stack.append(node)
                count += 1
            stack_y = node[1]
print(count)
