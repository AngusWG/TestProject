#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/1/24 0024 16:31
# @author  : zza
# @Email   : 740713651@qq.com

def fun1(pa):
    return str(pa) + "* 4"

class AAA:
    def fun1(s, pa):
        return str(pa) + "* 4"

    def testdemo(s, param=fun1(2)):
        print(param)




def main():
    AAA().testdemo(666)


if __name__ == '__main__':
    main()
