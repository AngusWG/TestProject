#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/2/2 0002 15:30
# @author  : zza
# @Email   : 740713651@qq.com

import re


def coverage_detection(text):
    a = re.findall("root:Contract[^%]*%", text)
    res = ""
    all_num = 0
    for i in a:
        contract_name = re.findall("sol:(.*):", i)[0]
        contract_num = re.findall(" (\d\d\d.\d|\d\d.\d)*%", i)[0]
        all_num += float(contract_num)
        res += contract_name + " " + contract_num + "\n"
    res += str(all_num / len(a))
    return res


def main():
    text = """WARNING:root:You are using an untested version of z3. 4.5.0 is the officially tested version
WARNING:root:You are using evm version 1.7.3. The supported version is 1.6.6
WARNING:root:You are using solc version 0.4.19, The latest supported version is 0.4.17
INFO:root:Contract BCV.sol:BCV:
INFO:oyente.symExec:Running, please wait...
INFO:oyente.symExec:	============ Results ===========
INFO:oyente.symExec:	  EVM code coverage: 	 99.9%
INFO:oyente.symExec:	  Callstack bug: 	 False
INFO:oyente.symExec:	  Money concurrency bug: False
INFO:oyente.symExec:	  Time dependency bug: 	 False
INFO:oyente.symExec:	  Reentrancy bug: 	 False
INFO:oyente.symExec:	====== Analysis Completed ======
bnet@ubuntu:~/solidity$ 
        """
    print(coverage_detection(text))


if __name__ == '__main__':
    main()
