#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2020/11/29 1:30
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : peepee_db_orm_demo.py
from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db