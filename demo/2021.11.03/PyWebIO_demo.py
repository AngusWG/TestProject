#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2021/4/14 22:42
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : PyWebIO_demo.py
from pywebio import start_server
from pywebio.input import input, FLOAT
from pywebio.output import put_text

from pywebio.input import input, FLOAT
from pywebio.output import put_text


def bmi():
    height = input("请输入你的身高(cm)：", type=FLOAT)
    weight = input("请输入你的体重(kg)：", type=FLOAT)

    BMI = weight / (height / 100) ** 2

    top_status = [(14.9, '极瘦'), (18.4, '偏瘦'),
                  (22.9, '正常'), (27.5, '过重'),
                  (40.0, '肥胖'), (float('inf'), '非常肥胖')]

    for top, status in top_status:
        if BMI <= top:
            put_text('你的 BMI 值: %.1f，身体状态：%s' % (BMI, status))
            break


if __name__ == '__main__':
    start_server(bmi, port=80, host='127.0.0.1')
