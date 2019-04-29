import itchat
from itchat.content import *
import requests, json
from BaiDuVoice import distingHandle
from time import sleep
from voiceSpeech import voiceSpeech
import os

#即使程序关闭，一定时间内重新开启也可以不用重新扫码(hotReload=True为True时)
itchat.auto_login(True)

#图灵机器人
def rbot(msgs):
    api_url = 'http://openapi.tuling123.com/openapi/api/v2'
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": "%s" % msgs
            }
        },
        "userInfo": {
            "apiKey": "8b0ff33b79324e3381aca79fb13c4515",
            "userId": "oldKingFT"
        }
    }
    data = json.dumps(data)
    r = requests.post(api_url, data=data).json()
    text = r['results'][0]['values']['text']
    if text:
        return text
    else:
        return '呵呵~'

#当接收到好友的语音消息时回复
@itchat.msg_register(RECORDING, isFriendChat=True)
def text_reply(msg):
    fileName = msg.fileName
    msg.download(fileName)

    dist = distingHandle(fileName)
    print(dist)
    if dist == 'ERROR':
        msg.user.send('听不懂你在说什么,重发一个吧!')
    else:
        #msg.user.send(rbot(dist))#回复文字消息
        speech = voiceSpeech(rbot(dist))#回复语音消息
        msg.user.send_file(speech)
        os.remove(speech)


#当接收到好友的文本消息时回复
@itchat.msg_register(TEXT, isFriendChat=True)
def text_reply(msg):
    msg.user.send(rbot(msg.text))

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.send('你好呀,我是陪聊高手,快来探索我的新功能吧,你可以对我说:脑筋急转弯~')



#运行itchat
itchat.run(True)