#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/1/30 0030 15:29
# @author  : zza
# @Email   : 740713651@qq.com
import difflib

diff = difflib.HtmlDiff()
a = open("E:\pythonCode\smart_contract_test\solidity\HydroToken\HydroToken.sol", 'U', encoding="utf-8").readlines()
b = open("E:\pythonCode\smart_contract_test\solidity\HyperCreditToken\HyperCreditToken.sol", 'U', encoding="utf-8").readlines()
result = diff.make_file(a, b, context=True)
# print(new_path + "/" + item)
if "No Differences Found" in result:
    pass
output = open("./result.html", "w+",encoding="utf8")
output.write(result)