#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
选当前坐标系
选目标坐标系
'''
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox 
import tkinter.filedialog
import pandas as pd
import coordinateTransform
import xlsx_result
from tkinter import END
from tkinter import scrolledtext
from PIL import Image, ImageTk  # pillow 模块

win = tk.Tk()
win.title("数据预处理工具")    # 添加标题
tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='坐标系转换')      # Add the tab


tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text='属性数据统计')      # Make second tab visible

tabControl.pack(expand=1, fill="both")

#---------------Tab1------------------#
def get_file_name():
    filename = tkinter.filedialog.askopenfilename(filetypes = [('Excel', 'xlsx')])
    name.set(filename)
    get_col_list()

def get_col_list():
    df = pd.read_excel(name.get())
    L = df.columns.values.tolist()
    lngChosen['values'] = L
    latChosen['values'] = L
    addressChosen['values'] = L
    
def trans():   
    coordinateTransform.xls_Transform(name.get(),lng.get(),lat.get(), coorChosen.get(), coorChosen2.get())       
    coordinateTransform.get_placeName_coordinate(name.get(), address.get(), addcoorChosen.get())
    tkinter.messagebox.showinfo('转换成功',"已完成坐标转换\n 已根据地名地址生成WGS84坐标系经纬度")
                                
                                
monty = ttk.LabelFrame(tab1, text="坐标系转换工具")
monty.grid(column=2, row=2, padx=0, pady=0)       # padx  pady   该容器外围需要留出的空余空间
#aLabel = ttk.Label(monty, text="A Label")


ttk.Label(monty, text="1.打开excel文件:").grid(column=0, row=0, sticky='W')      # 设置其在界面中出现的位置  column代表列   row 代表行
ttk.Label(monty, text="2.选择经度所在的列").grid(column=0, row=2,sticky='W')    # 添加一个标签，并将其列设置为1，行设置为0
ttk.Label(monty, text="3.选择纬度所在的列:").grid(column=0, row=4, sticky='W') 
ttk.Label(monty, text="4.选择当前坐标系:").grid(column=0, row=6, sticky='W')
ttk.Label(monty, text="5.选择转换坐标系:").grid(column=0, row=8, sticky='W')


ttk.Label(monty, text="选择地名地址:").grid(column=1, row=4, sticky='W')
ttk.Label(monty, text="选择目标坐标系:").grid(column=1, row=6, sticky='W')



# 按钮
ttk.Button(monty, text = "路径选择", command = get_file_name,width=10).grid(column = 1,row=1, sticky='W')
ttk.Button(monty, text = "转换", command = trans,width=10).grid(column = 1,row=9, sticky='W')

# 文本框
name = tk.StringVar()     # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理部件上面的字符；不过一般用在按钮button上。改变StringVar，按钮上的文字也随之改变。
nameEntered = ttk.Entry(monty, width=18, textvariable=name)   # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
nameEntered.grid(column=0, row=1, sticky=tk.W)       # 设置其在界面中出现的位置  column代表列   row 代表行
nameEntered.focus()     # 当程序运行时,光标默认会出现在该文本框中

# 创建经纬度的下拉列表
lng = tk.StringVar()
lngChosen = ttk.Combobox(monty, width=18, textvariable=lng, state='readonly')
lngChosen['values'] = ('无')     # 设置下拉列表的值
lngChosen.grid(column=0, row=3)      # 设置其在界面中出现的位置  column代表列   row 代表行
lngChosen.current(0)    # 设置下拉列表默认显示的值，0为 lng['values'] 的下标值

lat = tk.StringVar()
latChosen = ttk.Combobox(monty, width=18, textvariable=lat, state='readonly')
latChosen['values'] = ('无')     # 设置下拉列表的值
latChosen.grid(column=0, row=5)      # 设置其在界面中出现的位置  column代表列   row 代表行
latChosen.current(0)    # 设置下拉列表默认显示的值，0为 lng['values'] 的下标值

# 创建坐标系选择的下拉列表
coordinate = tk.StringVar()
coorChosen = ttk.Combobox(monty, width=18, textvariable=coordinate, state='readonly')
coorChosen['values'] = (['百度坐标系', 'WGS84坐标系', '火星坐标系', 'CGCS2000坐标系'])     # 设置下拉列表的值
coorChosen.grid(column=0, row=7)      # 设置其在界面中出现的位置  column代表列   row 代表行
coorChosen.current(0)    # 设置下拉列表默认显示的值，0为 lng['values'] 的下标值

coordinate2 = tk.StringVar()
coorChosen2 = ttk.Combobox(monty, width=18, textvariable=coordinate2, state='readonly')
coorChosen2['values'] = (['百度坐标系', 'WGS84坐标系', '火星坐标系', 'CGCS2000坐标系'])     # 设置下拉列表的值
coorChosen2.grid(column=0, row=9)      # 设置其在界面中出现的位置  column代表列   row 代表行
coorChosen2.current(0)


addcoorChosen = tk.StringVar()
addcoorChosen = ttk.Combobox(monty, width=18, textvariable=addcoorChosen, state='readonly')
addcoorChosen['values'] = (['百度坐标系', 'WGS84坐标系', '火星坐标系', 'CGCS2000坐标系'])     # 设置下拉列表的值
addcoorChosen.grid(column=1, row=7)      # 设置其在界面中出现的位置  column代表列   row 代表行
addcoorChosen.current(0)

address = tk.StringVar()
addressChosen = ttk.Combobox(monty, width=18, textvariable=address, state='readonly')
addressChosen['values'] = ('无')     # 设置下拉列表的值
addressChosen.grid(column=1, row=5)      # 设置其在界面中出现的位置  column代表列   row 代表行
addressChosen.current(0) 
#---------------Tab1------------------#




#---------------Tab2------------------#
monty4 = ttk.LabelFrame(tab2, text = '属性数据统计')
monty4.grid(column=0, row=0, padx=4, pady=4, sticky = 'WE')



def showResult():
    path = tk.filedialog.askopenfilename(filetypes=[("xlsx格式","xlsx")])
    xlsx_result.show_result(path)
    scr4.insert(tk.INSERT, "文件读取完毕\n")
    scr4.insert(tk.INSERT, "属性字段为：\n%s\n"%xlsx_result.colList)
    scr4.insert(tk.INSERT, "数据量统计如下：\n")
    scr4.insert(tk.INSERT, "数据唯一性检查：\n")
    scr4.insert(tk.INSERT, "重复数据有%s个\n"%xlsx_result.data_duplicates)
    scr4.insert(tk.INSERT, "占总数据量的%s\n"%xlsx_result.duplicate_percent)
    scr4.insert(tk.INSERT, "数据表共有%s行、%s列\n"%(xlsx_result.row, xlsx_result.col))
    scr4.insert(tk.INSERT, "缺失数据共有%s条\n"%xlsx_result.data_null)
    scr4.insert(tk.INSERT, "字段异常缺失率检查：\n")
    scr4.insert(tk.INSERT, "缺失率大于30%的字段为：\n")
    scr4.insert(tk.INSERT, " %s\n"%xlsx_result.List_null)
    pass

def showPie():
    xlsx_result.get_pie_chart()
    showpie=tk.Toplevel()
    pic_name= 'pie_chart.jpg'
    image = Image.open(pic_name)  
    img=ImageTk.PhotoImage(image)  
    canvas1 = tk.Canvas(showpie, width = image.width,height = image.height, bg = 'white')
    canvas1.create_image(0,0,image = img,anchor="nw")
    canvas1.create_image(image.width,0,image = img,anchor="nw")
    canvas1.pack()  
    showpie.mainloop() 

def delText():
    scr4.delete(1.0, END)
    pass


#选择文件按钮
selectFileButton = ttk.Button(monty4,text="打开文件",width=10,command=showResult)   
selectFileButton.grid(column=0,row=1,rowspan=2,ipady=7)


#生成饼状图按钮
pieChartButton = ttk.Button(monty4, text ='属性数据统计饼状图',width=18,command=showPie)
pieChartButton.grid(column=1,row=1,rowspan=2,ipady=7)

# 滚动显示结果 
scrolW  = 35; scrolH  =  15
scr4 = scrolledtext.ScrolledText(monty4, width=scrolW, height=scrolH, wrap=tk.WORD)
scr4.grid(column=0, row=5, sticky='WE', columnspan=3)
#清除信息按钮
selectFileButton = ttk.Button(monty4,text="清除信息",width=10,command=delText)   
selectFileButton.grid(column=2,row=8,rowspan=2,ipady=7)
#---------------Tab2------------------#



win.mainloop()      # 当调用mainloop()时,窗口才会显示出来