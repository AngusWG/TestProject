#!/usr/bin/env python
# encoding: utf-8
# @Time   : 2022/04/25 20:14:58
# @author : zza
# @Email  : z740713651@outlook.com
# @File   : demo_pyinstrument.py
""" pip install pyinstrument"""
import asyncio
from pyinstrument import Profiler


async def main():
    p = Profiler(async_mode="disabled")

    with p:
        print("Hello ...")
        await asyncio.sleep(1)
        print("... World!")

    p.print()


asyncio.run(main())
