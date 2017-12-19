''' 微信接收消息时把消息发给小冰, 并回复小冰的回复 '''
import os
import itchat
from itchat.content import *
last_msgId = False

def get_userName():
    ''' 获得小冰和自己的username '''
    try:
        return itchat.search_mps(name='小冰')[0]['UserName'], itchat.get_friends()[0]['UserName']
    except IndexError as err:
        print('获取userName出错啦', err)   #需要置顶公众号
        print(itchat.get_mps())
        print('请把公众号置顶!!!')

def get_nick(userName):
    ''' 通过userName获取nickName '''
    try:
        user = itchat.search_friends(userName=userName)
        if not user:
            user = itchat.search_chatrooms(userName=userName)
            if not user:
                user = itchat.search_mps(userName=userName)
        return user.get('NickName')
    except AttributeError as err:
        print('获取nickName出错啦', err)
        print(user)
        return None


@itchat.msg_register([TEXT, RECORDING, PICTURE, VIDEO, ATTACHMENT], isFriendChat=True, isGroupChat=True)
def reply(msg):
    ''' 接受到别人发送给我的消息,转发给小冰 '''
    try:
        if msg['FromUserName'] not in (ice_name, my_name):
            if msg['Type'] == "Text":
                itchat.send(msg['Text'], ice_name)
                print('转发', get_nick(msg['FromUserName']), "的文本消息给小冰", msg['Text'])
            else:
                msg['Text'](msg['FileName'])
                itchat.send('@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName']), ice_name)
                print(msg['Type'], msg['FileName'], {'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'))
                os.remove(msg['FileName'])
                print('转发', get_nick(msg['FromUserName']), "的消息给小冰成功")


        if msg['FromUserName'] != my_name:
            @itchat.msg_register([TEXT, RECORDING, PICTURE, VIDEO, ATTACHMENT], isMpChat=True)
            def re_from_ice(message):
                ''' 将小冰发回的消息转发给别人 '''
                global last_msgId
                if message['FromUserName'] == ice_name and msg.get('MsgId') != last_msgId:
                    if message['Type'] == "Text":
                        itchat.send(message['Text'], msg['FromUserName'])
                        print("小冰已回复消息", message['Text'])
                    else:
                        message['Text'](message['FileName'])
                        itchat.send(
                            '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(message['Type'], 'fil'), message['FileName']), msg['FromUserName'])
                        os.remove(message['FileName'])
                        print("小冰回复消息:%s=>%s" % (message['Type'], message['Text']))

                    last_msgId = msg.get('MsgId')
    except AttributeError as err:
        print(err)
    except Exception as err:
        print(err)

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    ice_name, my_name = get_userName()
    itchat.run()
    itchat.dump_login_status()