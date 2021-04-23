#!/usr/bin/env python
# encoding: utf-8
# Created by zza on 2021/3/10 18:31
# Copyright 2021 LinkSense Technology CO,. Ltd
from tenacity import retry


@retry
def test_retry():
    print("等待重试，重试无间隔执行。。。")
    raise Exception


test_retry()
