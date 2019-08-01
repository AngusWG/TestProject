#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2019/7/31 19:12
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : 聊天机器人.py

from wxpy import *

# 实例化，并登录微信
bot = Bot(cache_path=False)
# 查找到要使用机器人来聊天的好友
# my_friend = ensure_one(bot.search(u'好友名字'))
# # 调用图灵机器人API
# tuling = Tuling(api_key='4a0488cdce684468b95591a641f0971d')
#

# 使用图灵机器人自动与指定好友聊天
# @bot.register(my_friend)
# def reply_my_friend(msg):
#     tuling.do_reply(msg)


embed()
