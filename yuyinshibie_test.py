#!/usr/bin/python
#_*_ coding:utf-8 _*_

from aip import AipSpeech
import tkFileDialog
import os

#API使用参考地址：https://ai.baidu.com/docs#/ASR-Online-Python-SDK/top

APP_ID = '14349685'
API_KEY = 'nuvTxjy3xyQcEI1G6GEuWmrg'
SECRET_KEY = 'SMQUd4tnUrRFE7RttNhWb5W7heYLtBId'

client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)

#读取文件路径
def get_localfile_path():
    default_dir=r"/Users/gomo2016/Desktop"  #设置默认打开目录
    fname=tkFileDialog.askopenfilename(title=u"选择文件",initialdir=(os.path.expanduser((default_dir))))
    print(fname) #返回全文件路径
    #print(tkinter.filedialog.askdirectory())    #返回目录全路径
    return fname

#读取文件
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()
audio = get_file_content(get_localfile_path())

#调取接口,带参数
audios = client.asr(audio,'pcm',16000,{'dev_pid':1536,})
print(audios)

#从字典中取出文字
wd = audios.get('result')
print(wd)
