#此文件负责音频文件转码

from pydub import AudioSegment
import io
import os


#将mp3文件转换为wav文件
def tranceMp3ToWav(fileName):
    #读取待转换的文件
    with open(fileName,'rb') as fh:
        data = fh.read()
    #获取文件名和文件后缀
    spliText = os.path.splitext(fileName)
    #生成转换后的新文件名称
    newName = '%s.wav'%spliText[0]
    #执行文件格式转换操作
    au = AudioSegment.from_mp3(io.BytesIO(data))
    au.export(newName,format='wav')
    #删除原始文件
    os.remove(fileName)
    #输出转换好的新文件名称
    return newName


