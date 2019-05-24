#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/5/24 9:36
# @Author  : zza
# @Email   : 740713651@qq.com
"""https://github.com/dzlzh/shiyanlou-courses/blob/a50f7177d392c71cfa702d23679295d541655374/courses/Python/Python%20%E5%9B%BE%E7%89%87%E8%BD%AC%E5%AD%97%E7%AC%A6%E7%94%BB/0.Python%20%E5%9B%BE%E7%89%87%E8%BD%AC%E5%AD%97%E7%AC%A6%E7%94%BB.md"""
import argparse

from PIL import Image

# 命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file')  # 输入文件
parser.add_argument('-o', '--output')  # 输出文件
parser.add_argument('--width', type=int, default=80)  # 输出字符画宽
parser.add_argument('--height', type=int, default=80)  # 输出字符画高

# 获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':
    """python a.py b.jpg"""
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print("txt")

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)
