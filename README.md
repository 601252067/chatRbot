##这是一个微信个人号陪聊机器人


>**支持功能**

1.天气查询

2.讲笑话

3.讲故事

4.成语接龙

5.脑筋急转弯

6.说歇后语

7.说绕口令

8.说顺口溜

9.其他更好玩的功能开发中...


>**文件说明**

`BaiDuVoice.py`为语音识别转文字文件

`ffmpeg.exe`为语音文件格式转换所用的扩展文件

`friend_replay.py`为自动回复消息文件

`itchat.kpl`为信息文件

`tranceFile.py`为音频文件转码文件

`voicSpeech.py`为语音合成文件


>**消息回复说明**

1.可以接收好友的文字消息和语音消息

2.接收到语音消息后回复的内容以`.MP3`文件回复

3.接收到文字消息后会以文字消息回复


>**关于ffmpeg.exe文件使用说明**

我是在win10平台使用此文件,linux平台没有测试,所以只说win平台

此文件需要将文件目录配置到环境变量中

配置成功后打开pycharm时,右键->以管理员身份运行,就可以正常使用了