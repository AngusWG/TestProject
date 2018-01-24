#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/1/8 0008 14:23
# @author  : zza
# @Email   : 740713651@qq.com


class AAA(object):
    def __init__(self, num1):
        self.num1 = num1

    def test(self):
        """
        sadasdsadfsaf
        :return:
        """
        raise NotImplementedError("54156456")


class BBB(AAA):

    def lst(self):
        print(self.num1)


if __name__ == '__main__':
    BBB(666).lst()
