#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/2/28 0028 11:52
# @author  : zza
# @Email   : 740713651@qq.com
import re


def punctuationToCN(var_str):
    var_str = re.subn(" +", " ", var_str)[0]
    var_str = var_str.replace(",", "，").replace(".", "。").replace("(", "（").replace(")", "）").replace(" ", "，").split("\n")
    res = ""
    for i in var_str:
        if i == "":
            res += "\n"
            continue
        if not i.endswith("。"):
            res += i + "。\n"
        else:
            res += i +"\n"
    return res


def main():
    a = """WARNING:root:You are using an untested version of z3. 4.5.0 is the officially tested version
WARNING:root:You are using evm version 1.7.3. The supported version is 1.6.6
WARNING:root:You are using solc version 0.4.19, The latest supported version is 0.4.17
INFO:root:Contract hc.sol:BasicToken:
INFO:oyente.symExec:Running, please wait...
INFO:oyente.symExec:	============ Results ===========
INFO:oyente.symExec:	  EVM code coverage: 	 86.4%
INFO:oyente.symExec:	  Callstack bug: 	 False
INFO:oyente.symExec:	  Money concurrency bug: False
INFO:oyente.symExec:	  Time dependency bug: 	 False
INFO:oyente.symExec:	  Reentrancy bug: 	 False
INFO:root:Contract hc.sol:CappedToken:
INFO:oyente.symExec:Running, please wait...
INFO:oyente.symExec:	============ Results ===========
INFO:oyente.symExec:	  EVM code coverage: 	 95.4%
INFO:oyente.symExec:	  Callstack bug: 	 False
INFO:oyente.symExec:	  Money concurrency bug: False
INFO:oyente.symExec:	  Time dependency bug: 	 False
INFO:oyente.symExec:	  Reentrancy bug: 	 False
INFO:root:Contract hc.sol:HyperCreditToken:
INFO:oyente.symExec:Running, please wait...
INFO:oyente.symExec:	============ Results ===========
INFO:oyente.symExec:	  EVM code coverage: 	 89.2%
INFO:oyente.symExec:	  Callstack bug: 	 False
INFO:oyente.symExec:	  Money concurrency bug: False
INFO:oyente.symExec:	  Time dependency bug: 	 False
INFO:oyente.symExec:	  Reentrancy bug: 	 False
INFO:root:Contract hc.sol:MintableToken:
INFO:oyente.symExec:Running, please wait...
INFO:oyente.symExec:	============ Results ===========
INFO:oyente.symExec:	  EVM code coverage: 	 95.4%
INFO:oyente.symExec:	  Callstack bug: 	 False
INFO:oyente.symExec:	  Money concurrency bug: False
INFO:oyente.symExec:	  Time dependency bug: 	 False
INFO:oyente.symExec:	  Reentrancy bug: 	 False
INFO:root:Contract hc.sol:Ownable:
INFO:oyente.symExec:Running, please wait...
INFO:oyente.symExec:	============ Results ===========
INFO:oyente.symExec:	  EVM code coverage: 	 99.5%
INFO:oyente.symExec:	  Callstack bug: 	 False
INFO:oyente.symExec:	  Money concurrency bug: False
INFO:oyente.symExec:	  Time dependency bug: 	 False
INFO:oyente.symExec:	  Reentrancy bug: 	 False
INFO:root:Contract hc.sol:ParameterizedToken:
INFO:oyente.symExec:Running, please wait...
INFO:oyente.symExec:	============ Results ===========
INFO:oyente.symExec:	  EVM code coverage: 	 89.2%
INFO:oyente.symExec:	  Callstack bug: 	 False
INFO:oyente.symExec:	  Money concurrency bug: False
INFO:oyente.symExec:	  Time dependency bug: 	 False
INFO:oyente.symExec:	  Reentrancy bug: 	 False
INFO:root:Contract hc.sol:SafeMath:
INFO:oyente.symExec:Running, please wait...
INFO:oyente.symExec:	============ Results ===========
INFO:oyente.symExec:	  EVM code coverage: 	 100.0%
INFO:oyente.symExec:	  Callstack bug: 	 False
INFO:oyente.symExec:	  Money concurrency bug: False
INFO:oyente.symExec:	  Time dependency bug: 	 False
INFO:oyente.symExec:	  Reentrancy bug: 	 False
INFO:root:Contract hc.sol:StandardToken:
INFO:oyente.symExec:Running, please wait...
INFO:oyente.symExec:	============ Results ===========
INFO:oyente.symExec:	  EVM code coverage: 	 93.8%
INFO:oyente.symExec:	  Callstack bug: 	 False
INFO:oyente.symExec:	  Money concurrency bug: False
INFO:oyente.symExec:	  Time dependency bug: 	 False
INFO:oyente.symExec:	  Reentrancy bug: 	 False
INFO:oyente.symExec:	====== Analysis Completed ======
INFO:oyente.symExec:	====== Analysis Completed ======
INFO:oyente.symExec:	====== Analysis Completed ======
INFO:oyente.symExec:	====== Analysis Completed ======
INFO:oyente.symExec:	====== Analysis Completed ======
INFO:oyente.symExec:	====== Analysis Completed ======
INFO:oyente.symExec:	====== Analysis Completed ======
INFO:oyente.symExec:	====== Analysis Completed ======

"""
    # a = punctuationToCN(a)
    print(a)


if __name__ == '__main__':
    main()
