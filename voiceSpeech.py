#语音合成
from aip import AipSpeech #引入百度语音识别SDK
import time

# 实例化语音识别客户端
APP_ID = '16119934'
API_KEY = '9jx6ujnZEbYoqXsg6j517kjq'
SECRET_KEY = 'ICGqlErts4SsSjuyAqmnuPuUK5PeTG1i'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
#配置AipSpeech的网络请求参数
client.setConnectionTimeoutInMillis(15000)
client.setSocketTimeoutInMillis(15000)

def voiceSpeech(text):
    result = client.synthesis(text, 'zh', 1, {
        'spd': 5, 'pit': 5, 'vol': 6, 'per': 1,
    })
    voiceFileName = './voice/%s.mp3' % time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    if not isinstance(result, dict):
        with open(voiceFileName, 'wb') as f:
            f.write(result)
        return voiceFileName