# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 11:43:37 2018
在MySQL的gridno字段旁添加一个ID字段，使得每个中文字符的网格名称都有对应的ID
@author: SZU
"""

import pymysql
import pandas as pd
import matplotlib.pyplot as plt

month = ['2016-05', '2016-06', '2016-07', '2016-08', '2016-09', '2016-10',
         '2016-11', '2016-12', '2017-01', '2017-02', '2017-03', '2017-04',
         '2017-05', '2017-06', '2017-07', '2017-08', '2017-09']
#number = [12, 60, 39, 94, 667, 94, 74, 63, 4, 40, 165, 374, 193, 67, 50, 64, 83]
number = []

def get_number(grid_name):
    conn = pymysql.connect(host='localhost', user='root', passwd='5623', db='grid',charset='utf8')
    cursor = conn.cursor()
    for i in month:        
        sql ="WHERE `time` LIKE '%%s%' AND `gridno` LIKE '%s'" %(i, grid_name)
        try:
            num = cursor.execute(sql)
            #df = pd.read_sql(sql,conn)
        except Exception as e:
            print(e)

    number.append(num)
    conn. close()
    return number
    

def get_line_chart():
    plt.figure(figsize=(18,4),dpi=80)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.plot(month,number ,linewidth=5)  
    plt.xlabel("月份",fontsize=14)  
    plt.ylabel("数量",fontsize=14)  
    plt.title('固戍74网格事件数量折线图', fontsize=20)
    plt.legend()
    plt.savefig("固戍74网格事件数量折线图.jpg")
    plt.show()
    
get_line_chart()