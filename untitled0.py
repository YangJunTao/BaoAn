# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 20:41:58 2018

@author: PC-XXX
"""
import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost', user='root', passwd='5623', db='grid',charset='utf8')
cursor = conn.cursor()

sql = "SELECT * FROM `2017-04` WHERE `gridno` LIKE '%罗租%' "
data = pd.read_sql(sql, conn)