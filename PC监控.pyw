# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 09:24:47 2016

@author: Differlong

version 0.1

改进空间：
未来可以增加摄像头，可以改善算法，比如增加一个监控文件夹，每10分钟截屏，如果达到某种条件，就把所有的图片打包发送！！！！
这个是真变态！！！
"""

import yagmail
from PIL import ImageGrab
import time
from win32com.client import Dispatch

sound = Dispatch("SAPI.SpVoice")

defaultPicName = "grab.jpg"



def grab():
    img = ImageGrab.grab()
    img.save(defaultPicName,"jpeg")

def mail(addr = "gloriachou.pku.edu.cn",file=defaultPicName):
    user = "differlong@pku.edu.cn"
    password = ""#邮箱密码
    yag = yagmail.SMTP(user=user,password=password,host="smtp.pku.edu.cn",port="25")
    
    now = time.localtime()
    nowStr = "%d:%d"%(now.tm_hour,now.tm_min)
    subject = "看看他这么晚了（{}），都在干什么？".format(nowStr)
    contents = "您好！我是萌萌哒的监控机器人，看看这个晚了你的男朋友在干什么吧。竭诚为您服务！"
    attachments = [file]
    yag.send(to=addr,subject=subject,contents=contents,attachments=attachments)
    yag.close()

def mainloop():
    while True:
        now = time.localtime()
        if 60 *now.tm_hour + now.tm_min > 23*60 + 0 or 60*now.tm_hour+now.tm_min < 5*60 + 0:
            grab()
            mail()
            sound.speak("现在电脑处于监控状态，没有事情尽快睡觉，后果自负！")
        time.sleep(60*10)
        
        
        
if __name__ == "__main__":
    mainloop()