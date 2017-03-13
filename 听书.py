# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 22:04:28 2016

@author: 独处
"""

#瑕疵：为了实现记忆功能，就用了一个log文件来存储进度。但是由于是单线程的缘故，而且
#不是很熟悉文件的操作，每次都是打开一个文件，写入，然后关闭。假如能够实现只打开一次
#而不断写入，像log文件一样就可以。如果需要持续改进的话，可能需要去考虑Log这个module。
#现在只是非常粗糙的版本，改进空间是增加GUI，在一个固定的文件夹保存Log文件。这样就想
#听什么书，就可以听什么书了。


from win32com import client
import time
import os
S = client.Dispatch("SAPI.SpVoice")

book = "双城记-狄更斯"#去掉了.txt的文件名

if not os.path.isfile(book+"Log.txt"):
    with open(book + "Log.txt","w") as log:
        log.write(str("0"))


log = open(book +"Log.txt","r")
a = log.readline()
log.close()
begin = 0 if a ==""else int(a)

with open(book + ".txt","rt",encoding='utf8') as f:
    lines = f.readlines()
for order in range(begin,len(lines)):
    S.Speak(lines[order])
    if int(time.time())% 7 == 0 :
        print(order)
        with open(book + "Log.txt","w") as log:
            log.write(str(order)) 


#with open('somefile.txt', 'rt', encoding='utf8') as f:








