# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:17:06 2016

@author: Differlong
"""

def generateId():
    i = 0
    while True:
        yield i
        i+=1

newId = generateId()


from gtts import gTTS
with open("越女剑.txt","r") as file:
    for line in file:
        pList = line.split("。")
        for p in pList:
            if p=="":
                continue
            tts = gTTS(p,lang="zh")
            tts.save("data/越女剑{}.mp3".format(str(next(newId))))
