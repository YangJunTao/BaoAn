# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 20:35:23 2018

@author: PC-XXX
"""

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
from PIL import Image, ImageTk  # pillow 模块



#由于tkinter中没有ToolTip功能，所以自定义这个功能如下
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))


        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)


    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
            

# Create instance
win = tk.Tk()   
monty = ttk.LabelFrame(tab1, text='打开excel文件，')
monty.grid(column=0, row=0, padx=8, pady=4)

# Add a title       
win.title("网格事件统计工具")
ttk.Label(monty, text="网格编号:").grid(column=0, row=0, sticky='W')


# Adding a Textbox Entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(monty, width=12, textvariable=name)
nameEntered.grid(column=0, row=1, sticky='W')


# Adding a Button
action = ttk.Button(monty,text="确定",width=10,command=clickMe)   
action.grid(column=2,row=1,rowspan=2,ipady=7)


ttk.Label(monty, text="请选择时间:").grid(column=1, row=0,sticky='W')


# Adding a Combobox
time = tk.StringVar()
timeChosen = ttk.Combobox(monty, width=12, textvariable=time)
timeChosen['values'] = ('2016-05', '2016-06', '2016-07', '2016-08', '2016-09', '2016-10',
                         '2016-11', '2016-12', '2017-01', '2017-02', '2017-03', '2017-04',
                         '2017-05', '2017-06', '2017-07', '2017-08', '2017-09')
timeChosen.grid(column=1, row=1)
timeChosen.current(0)  #设置初始显示值，值为元组['values']的下标
timeChosen.config(state='readonly')  #设为只读模式





# Using a scrolled Text control    
scrolW  = 30; scrolH  =  5
scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, row=3, sticky='WE', columnspan=3)




# 一次性控制各控件之间的距离
for child in monty.winfo_children(): 
    child.grid_configure(padx=3,pady=1)
# 单独控制个别控件之间的距离
action.grid(column=2,row=1,rowspan=2,padx=6)

# Disable resizing the GUI
win.resizable(0,0)
win.mainloop()