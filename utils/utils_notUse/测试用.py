#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/2/2 0002 13:45
# @author  : zza
# @Email   : 740713651@qq.com
import os

from bean.solidity_file import SolidityFile


def getfilelist(param):
    # 列出目录下的所有文件和目录
    result = os.listdir(param)
    # add_list = list()
    for item in result[::-1]:
        file = (param + "/" + item)
        if os.path.isdir(file):
            lower_item = getfilelist(file)
            result.remove(item)
            if lower_item is not None:
                add_item = {item: lower_item}
                result.append(add_item)
    if len(result) == 0:
        return None
    return result


def count_file_lines(file):
    try:
        count = len(open(file, 'r', encoding="utf8").readlines())
        if count > 1000:
            print(count, file)
        return count
    except:
        return 0


def get_all_file(dirs, path):
    res = []
    for item in dirs:
        if isinstance(item, dict):
            item_path = list(item.keys())[0]
            item_dirs = list(item.values())[0]
            res+=get_all_file(item_dirs, path + "/" + item_path)
        if isinstance(item, str):
            res.append(SolidityFile(path + "/" + item))
    return res


def do_one():
    # 合约文件地址
    file_address = "E:\pythonCode\smart_contract_test\solidity\已过\HyperCreditToken\s222.sol"
    # 获得整个文件
    file = SolidityFile(file_address)
    print(file.g_describe())
    pass


def batch_operation():
    path = "../solidity/contracts"
    # 获得文件目录树
    dirs = getfilelist(path)
    # 获得每个文件的行数
    files = get_all_file(dirs, path)
    for i in files:
        print(i.file_name)
        print(i.g_describe())


if __name__ == '__main__':
    batch_operation()
    # do_one()
