# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 12:06:18 2018

@author: PC-XXX
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

row = 0
col = 0
data_null = 0
col_duplicate = 0
data_duplicates = 0
duplicate_percent = 0
colList = []
List_null = []
def show_result(data_path):
    global row
    global col
    global data_null
    global col_duplicate
    global data_duplicates
    global duplicate_percent
    global colList
    global List_null
    data = pd.read_excel(data_path)
    for col in data.columns.values.tolist():#删除不需要的属性字段
        if col in ['GPSX', 'GPSY',u'经度', u'纬度', 'RecordID', 'MapID']:
            del data[col]
    colList = [column for column in data]#获取列名   
    row = len(data.index)#行数量
    col = len(data.columns)#列数量
    data_null = int(sum(data.isnull().sum(axis=0)))#缺失数据  
    #字段唯一性检查
    col_duplicate = len(colList) - len(set(colList))
    #数据项唯一性检查
    data_duplicates = np.sum(data.duplicated()==True) #重复数据量
    duplicate_percent = "%.0f%%" % (float(data_duplicates)/float(row)*100)
                            
    #字段异常缺失率检查
    for i in colList:
        col_null = data[i].isnull().sum()
        if col_null > 0.3*row:#筛选缺失率大于30%的字段
            List_null.append(i)
    '''
    修改列名
    data.rename(columns = {'A':'a', 'B':'b'},inplace = True)
    '''
    
    
def get_pie_chart():  
    #画饼状图    
    plt.style.use('ggplot')
    fig = plt.figure(figsize=(8,8))
    labels = [u'所有数据',u'缺失数据']
    sizes = [row*col, data_null ]
    colors=[ '#9999ff', '#ff9999' ]
    explode = [0, 0.1]
    plt.rcParams['font.sans-serif']=['SimHei'] #设置全局字体
    plt.axes(aspect= 'equal')
    plt.xlim( 0, 4)
    plt.ylim( 0, 4)
    plt.pie(x=sizes, labels=labels,textprops = {'fontsize':20, 'color':'k'},
            labeldistance = 1.1,autopct= '%.1f%%',shadow = True,explode=explode, 
            startangle = 90)
    plt.xticks(())
    plt.yticks(())
    plt.title(u"数据缺失率统计饼状图", fontsize = 20)  
    plt.savefig("pie_chart.jpg")

    
