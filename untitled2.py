# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 17:06:35 2018

@author: PC-XXX
"""

# encoding=utf-8
import time
import hashlib
from tkinter import *
import tkinter.messagebox

import tkinter.fileDialog
import platform


db = {}

#处理注册
def newuser(name,pwd):
    while True:
        if db.has_key(name):
            tkMessageBox.showinfo(title='失败', message='already has this name')
            continue
        else:
            break

    m = hashlib.md5()
    m.update(pwd)
    # print m
    # print m.hexdigest()
    db[name] = [m.hexdigest(),time.strftime("%Y %m %d %H %M", time.localtime())]
    tkMessageBox.showinfo(title='成功', message='注册成功')

#处理直接登录
def olduser(name,pwd):

    m = hashlib.md5()
    m.update(pwd)
    # print m
    pwd = m.hexdigest()
    passwd = db[name][0]
    if passwd == pwd:
        tkMessageBox.showinfo(title='成功', message='welcome back'+name)
        ti = time.strftime("%Y %m %d %H %M", time.localtime())
        lis1 = ti.split(' ')
        lis2 = db[name][1].split(' ')
        # print lis1
        # print lis2
        if lis1[0] == lis2[0]:
            if lis1[1] == lis2[1]:
                if lis1[2] == lis2[2]:
                    if int(lis1[3])-4<int(lis2[3]):
                        # print 'you alraedy logged in at %s' %db[name][1]
                        tkMessageBox.showinfo(title='成功', message='you already logged in at %s ' % db[name][1])
        db[name][1] = ti
    else:
        tkMessageBox.showinfo(title='失败', message='登录失败')

#删除用户，返回一个提示框
def delete(name):
    del db[name]
    tkMessageBox.showinfo(title='成功', message='删除：'+name)

#展示所有用户，返回提示框
def showuser():
    string1 = ''
    for key in db:
        string1 = string1+key
        string1 = string1+' '+db[key][0]
        string1 = string1+'\n'

    tkMessageBox.showinfo(title='用户信息', message=string1)

#处理注册窗口
def signin():
    win1 = Toplevel()
    l1 = Label(win1, text="注册")
    l1.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
    l2 = Label(win1, text="姓名：")
    l2.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
    sheet_text1 = StringVar()
    sheet1 = Entry(win1, textvariable=sheet_text1)
    sheet1.pack()

    l3 = Label(win1, text="密码：")
    l3.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
    sheet_text2 = StringVar()
    sheet2 = Entry(win1, textvariable=sheet_text2)
    sheet2.pack()

    def on_click1():
        name = sheet_text1.get()
        pwd = sheet_text2.get()
        #调用处理新用户窗口
        newuser(name,pwd)

    Button(win1, text="press", command=on_click1).pack()

#处理登录窗口
def login():
    # win1 = Tk.winfo_toplevel(root)
    #焦点绑定到当前窗口，否则无法获取输入
    win1 = Toplevel()
    l4 = Label(win1, text="登录")
    l4.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
    l5 = Label(win1, text="姓名：")
    l5.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
    sheet_text3 = StringVar()
    sheet3 = Entry(win1, textvariable=sheet_text3)
    sheet3.pack()

    l6 = Label(win1, text="密码：")
    l6.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
    sheet_text4 = StringVar()
    sheet4 = Entry(win1, textvariable=sheet_text4)
    sheet4.pack()

    def on_click2():
        name = sheet_text3.get()
        pwd = sheet_text4.get()
        olduser(name,pwd)



    Button(win1, text="press", command=on_click2).pack()

#退出程序
def quit1():
    root.quit()

#删除用户窗口
def deuser():
    win1 = Toplevel()
    l4 = Label(win1, text="登录")
    l4.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
    l5 = Label(win1, text="姓名：")
    l5.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
    sheet_text3 = StringVar()
    sheet3 = Entry(win1, textvariable=sheet_text3)
    sheet3.pack()


    def on_click5():
        name = sheet_text3.get()
        delete(name)

    Button(win1, text="press", command=on_click5).pack()

if __name__ == '__main__':
    root = Tk()
    root.title('用户登录窗口')
    root.geometry('500x400')

    #分别进入不同的窗口
    Button(root, text="注册", command=signin).pack()
    Button(root, text="登录", command=login).pack()
    Button(root, text="退出", command=quit1).pack()
    Button(root, text="所有用户", command=showuser).pack()
    Button(root, text="删除用户", command=deuser).pack()

    root.mainloop()
