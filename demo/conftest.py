#!/usr/bin/env python
# encoding: utf-8 
# Created by zza on 2021/1/19 12:04
# Copyright 2021 LinkSense Technology CO,. Ltd
import numpy
import pytest


@pytest.fixture(autouse=True)
def add_np(doctest_namespace):
    doctest_namespace["np"] = numpy
    doctest_namespace["ccc"] = "abc"
    doctest_namespace["c1"] = [1, 2]
    doctest_namespace["c2"] = print


@pytest.fixture(scope="function")
def set_up_module(request):
    a = ("set_up_module")
    b = (request.node.name)
