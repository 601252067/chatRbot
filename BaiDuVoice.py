#此文件负责语音识别

from aip import AipSpeech #引入百度语音识别SDK
from tranceFile import tranceMp3ToWav#将MP3格式文件转换为wav格式文件
import os
APP_ID = '16119934'
API_KEY = '9jx6ujnZEbYoqXsg6j517kjq'
SECRET_KEY = 'ICGqlErts4SsSjuyAqmnuPuUK5PeTG1i'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)#实例化语音识别客户端
client.setConnectionTimeoutInMillis(15000)#设置建立连接的超时时间
client.setSocketTimeoutInMillis(15000)#设置通过打开的连接传输数据的超时时间

#打开文件
def getFileContent(apth):
    with open(apth, 'rb') as fp:
        return fp.read()

#语音识别操作
def distingHandle(apth):
    tranceFile = tranceMp3ToWav(apth)#将下载的微信语音聊天MP3文件转码
    result = client.asr(getFileContent(tranceFile), 'wav', 16000, {'dev_pid':1536,})#进行语音识别操作
    os.remove(tranceFile)#识别成功后删除转码文件
    if result['err_no'] == 0:
        return result['result'][0]
    else:
        return 'ERROR'


