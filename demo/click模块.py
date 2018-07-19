#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/7/17 0017 14:35
# @author  : zza
# @Email   : 740713651@qq.com

# click模块 python cli 模块
import click


# 作者：进击的STE
# 链接：https://www.jianshu.com/p/488750ca69f0
# 來源：简书
# 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。

@click.command()
@click.option('--count',default = 5, type=click.IntRange(0, 20, clamp=True))
@click.option('--digit',default = 5, type=click.IntRange(0, 10))
def repeat(count, digit):
    click.echo(str(digit) * count)


if __name__ == '__main__':
    repeat()
