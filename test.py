# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 16:53:33 2018

@author: SZU
"""
from urllib import parse
import json
import hashlib
from urllib.request import urlopen
from tkinter import *   #引用Tk模块
import tkinter.messagebox
root = Tk()             #初始化Tk()


root.title("生成经纬度")
root.geometry('240x130')
label = Label(root, width=15, height=3, text="在下方输入地址名称").pack()

def buttonMessage():
    message = getLocation()
    tkinter.messagebox.showinfo(title="经纬度",message=message)
                
var = StringVar()
e = Entry(root, textvariable = var)
e.pack()
b = Button(root, text="确定",command = buttonMessage)
b.pack()

def getLocation():
    address = var.get()#.encode('unicode-escape').decode('string_escape')  
    queryStr = '/geocoder/v2/?address=%s&output=json&ak=kN3ruwt5fXbPiG90s4ANB2OLsXc0QdWg' % address 
     # 对queryStr进行转码，safe内的保留字符不转换
    encodedStr = parse.quote(queryStr, safe="/:=&?#+!$,;'@()*[]") 
     # 在最后直接追加上yoursk
    rawStr = encodedStr + 'kN3ruwt5fXbPiG90s4ANB2OLsXc0QdWg' 
     #计算sn
    sn = (hashlib.md5(parse.quote_plus(rawStr).encode("utf8")).hexdigest())  
     #由于URL里面含有中文，所以需要用parse.quote进行处理，然后返回最终可调用的url
    url = parse.quote("http://api.map.baidu.com"+queryStr+"&sn="+sn, safe="/:=&?#+!$,;'@()*[]")  
    req = urlopen(url)
    res = req.read().decode() 
    temp = json.loads(res)
    lat = temp['result']['location']['lat']
    lng = temp['result']['location']['lng']
    return "经度："+str(lat)+"，纬度："+str(lng)


    
root.mainloop()         #进入消息循环

