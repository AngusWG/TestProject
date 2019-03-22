#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/2/19 10:54
# @Author  : zza
# @Email   : 740713651@qq.com
# from flask import Flask
from sqlalchemy import create_engine

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']=
# db = SQLAlchemy(app) # 通过类`SQLAlchemy`来连接数据库

DB_URI = 'sqlite:///test.sqlite'
engine = create_engine(DB_URI)
from sqlalchemy.orm import sessionmaker

# 创建Session对象来绑定上文建立的engine连接
Session = sessionmaker(bind=engine)

# 实例化Session
session = Session()

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from sqlalchemy import Column, Integer, String


class User(Base):
    # 定义表名
    __tablename__ = 'users'
    # 定义表内容
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    score = Column(Integer)


db.create_all()
