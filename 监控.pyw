# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 16:26:50 2016

@author: diffe
"""

from PIL import ImageGrab
from datetime import datetime
import os
import time
import yagmail
import random
defaultRoot = "E://Control/"


def mail(file,addr = "differlong@163.com"):
    user = "differlong@pku.edu.cn"
    password = "miracle2016"
    yag = yagmail.SMTP(user=user,password=password,host="smtp.pku.edu.cn",port="25")
    
    now = time.localtime()
    nowStr = "%d:%d"%(now.tm_hour,now.tm_min)
    subject = "想偷偷瞄一眼他在做什么吗？（{}）".format(nowStr)
    contents = "您好！我是萌萌哒的监控机器人，想偷偷瞄一眼他在干什么，让我来告诉你"
    attachments = [file]
    yag.send(to=addr,subject=subject,contents=contents,attachments=attachments)
    yag.close()
    print("Mail has been sent!!")

def saveGrab(defaultRoot=defaultRoot,isMail=True):
    if not os.path.isdir(defaultRoot):
        os.mkdir(defaultRoot)
    img = ImageGrab.grab()
    now = datetime.now()
    day = "%d_%d_%d/"%(now.year,now.month,now.day)
    curTime = "%d：%d"%(now.hour,now.minute)
    if not os.path.isdir(defaultRoot+day):
        os.mkdir(defaultRoot+day)
    name = curTime + ".jpg"
    img.save(defaultRoot + day + name,"jpeg")
    if isMail==True:
        random.seed(now.second)
        if random.randint(1,100)==23:
            mail(file=defaultRoot+day+name,addr="gloriachou.pku.edu.cn")

while True:
    saveGrab()
    time.sleep(60*10)

