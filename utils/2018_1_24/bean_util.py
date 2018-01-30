#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2017/12/25 0025 19:47
# @author  : zza
# @Email   : 740713651@qq.com
import re


def clear_str(pro):
    pro = pro.replace("'", '')
    pro = pro.replace('"', '')
    pro = pro.replace(' ', '')
    pro = pro.split(',')
    res = list()
    for i in pro:
        res.append(i.split('=')[0])
    return res


def bean_util1(pro: str = ""):
    pro = clear_str(pro)
    result = ''''''
    for i in pro:
        result += 'self._' + i + ' = ' + i + '\n'

    return result


def bean_util2(pro: str = ""):
    pro = clear_str(pro)
    ret = ''''''

    for i in pro:
        result = '''
@property
def bid(self):
    return self._bid

@bid.setter
def bid(self, new_bid):
    self._bid = new_bid
    
'''
        ret += result.replace('bid', i)
        # ret += result
    return ret


def str_util(str1):
    str1 = clear_str(str1)
    res_list = list()
    for i in str1:
        res_list.append("_" + i)
    return res_list


if __name__ == '__main__':
    str1 = "'bid', 'ask', 'high', 'low', 'popen', 'pclose', 'last', 'volume', 'timestamp'"
    print(str_util(str1))
    # print(bean_util1(str1))
    # print(bean_util2(str1))
