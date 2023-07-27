#!/usr/bin/env python
# encoding: utf-8
# @Time   : 2022/10/25 16:41:40
# @author : zza
# @Email  : z740713651@outlook.com
# @File   : 行云智能-笔试题.py

# 题目 1：
import re
from typing import List
import sqlalchemy

db = sqlalchemy.create_engine()


class Node:
    def __init__(self, node_id, ParentId=None, Name=None):
        """
        :param node_id:该节点的 ID(自增主键)
        :param ParentId: 该节点的父节点 ID
        :param Name: 节点名称
        """
        self.Id = node_id
        self.ParentId = ParentId
        self.Name = Name

    def __repr__(self):
        return f"Node({self.Id},{self.ParentId})"


def delete(target_id: int, node_list: List[Node]):
    """实现从 NodeList 中删除 Id 为 TargetId 的节点及其所有子节点。

    :param target_id: 目标节点id
    :param node_list: 已加载到内存的 节点对象列表
    :return: 被删除的 id 集合

    >>> n_list = [Node(1,0),Node(2,1),Node(3,1),Node(4,3),Node(5,3),Node(6,2)]
    >>> delete(3,n_list)
    DELETE FROM tree_table where id in (3,4,5)
    [3, 4, 5]
    >>> n_list
    [Node(1,0), Node(2,1), Node(6,2)]
    >>> delete(3,[])

    """
    delete_ids = []
    tmp_node_list = sorted(node_list, key=lambda x: x.Id)
    # 使用备份列表，避免删除造成跳读
    for node in tmp_node_list:
        if node.ParentId in delete_ids:
            delete_ids.append(node.Id)
            node_list.remove(node)
        elif node.Id == target_id:
            delete_ids.append(node.Id)
            node_list.remove(node)
    if not delete_ids:
        return
    # 数据库删除
    sql = f"DELETE FROM tree_table where id in ({','.join(str(i) for i in delete_ids)})"
    print(sql)  # todo:should be logger.info
    # db.execute(sql)
    # 返回已经被删除的id
    return delete_ids


## 题目2


def get_k_min_nums(nums: List[int], k: int) -> List[int]:
    """找到最小的k个数

    Args:
        nums (List[int]): 输入数组
        k (int): k个数字

    Returns:
        List[int]: 数组nums中的最小的k个数字

    >>> get_k_min_nums([5,6,7,1,2,3,4,8],4)
    [4, 3, 2, 1]
    >>> get_k_min_nums([8,1,3,4,2,2,5],4)
    [3, 2, 2, 1]
    >>> get_k_min_nums([8,1,3,4,2],1)
    [1]
    >>> get_k_min_nums([],0)
    []
    """
    min_num_stack = []  # eg. [4, 3, 2, 1]

    def check_num(num: int):
        # 比最小值小
        if not min_num_stack:
            min_num_stack.append(num)
            return

        # 插入到合适位置
        for index, value in enumerate(min_num_stack):
            if num > value:
                min_num_stack.insert(index, num)
                break
        else:
            min_num_stack.append(num)
        if len(min_num_stack) > k:
            min_num_stack.pop(0)  # pop 最大的
        # print(min_num_stack)

    for i in nums[:]:
        check_num(i)
    return min_num_stack


## 题目3


def singleton(cls):
    instances = {}

    def get_instance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return get_instance


@singleton
class MyClass:
    ...


## 题目4


def check_is_cn_phone_number(number: str) -> bool:
    """是否为中国电话号码

    Args:
        number (str): 电话号码

    Returns:
        bool: True 为电话号码 False 表示不是中国的电话号码

    >>> check_is_cn_phone_number('13712345678')
    True
    >>> check_is_cn_phone_number('+8613812345678')
    True
    """
    if re.match(r"(\+86)?1\d{10}", number):
        return True
    return False


## 题目 5


def 题目5():
    db.execute(
        """
    Select
      SNO,
      SNAME,
      GRADE
    FROM
      S
      LEFT JOIN SC
    WHERE
      S.SNO = SC.SNO
    WHERE
      CNO = (
        SELECT
          CNO
        FROM
          C
        WHERE
          CNAME = 'MATH'
      )
    """
    )
    ## 2
    db.execute(
        """
    Select
      SNO,
      SNAME,
      GRADE
    FROM
      S
      LEFT JOIN SC
    WHERE
      S.SNO = SC.SNO
    WHERE
      GRADE = null
      AND CNO = (
        SELECT
          CNO
        FROM
          C
        WHERE
          CNAME = 'MATH'
      )
       
    """
    )
