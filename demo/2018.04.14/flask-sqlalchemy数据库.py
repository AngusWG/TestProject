#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2018/7/16 0016 15:54
# @author  : zza
# @Email   : 740713651@qq.com
import os
import sqlalchemy as sa

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 用Sqlite做例子,别的数据库连接字符串不同
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@192.168.14.147:3306/zza_text'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_POOL_SIZE'] = 128  # 线程池大小
# app.config['SQLALCHEMY_POOL_TIMEOUT'] = 45  # 超时时间
# app.config['SQLALCHEMY_POOL_RECYCLE'] = 3  # 空闲连接自动回收时间
# app.config['SQLALCHEMY_MAX_OVERFLOW'] = 128  # 控制在连接池达到最大值后可以创建的连接数。
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


# metadata = sa.MetaData()
class TokenInfo(db.Model):
    """token信息表, 需要用户上传(我们爬取etherscan.io)"""

    __tablename__ = 'token_info'
    contract_address = db.Column(db.Integer, autoincrement=True, primary_key=True, comment='主键, 合约地址')
    overview = db.Column(db.String(1024), comment='代币简介')
    ico_information = db.Column(db.Text, comment='ico信息的json对象')


db.drop_all()
db.create_all()
# 假定这是你的数据结构,在一个list中每个元组是一条记录
values = [
    (None, "Test", "Test"),
    (None, "Test", "Test"),
]
# 主要是参考这部分如何批量插入
with db.session.connection() as connection:
    # with connection.begin() as transaction:
    try:
        markers = ','.join(['%s'] * len(values[0]))
        # markers = ','.join(['?'] * len(values[0]))
        # 按段数拼成makers = '(?,?,?,?)'
        ins = 'INSERT INTO {tablename} VALUES ({markers})'
        ins = ins.format(tablename=TokenInfo.__tablename__, markers=markers)
        # 如果你的表已经存在了,widgets_table.name改成表名就行了.
        connection.execute(ins, values)
        db.session.commit()
    except Exception as err:
        # db.session.rollback()
        print("*" * 50)
        print(err)
        raise err
    # print("/" * 50)
    # print("*" * 50)
    # transaction.commit()
