# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 16:53:33 2018

@author: SZU
"""
import math
import pandas as pd
from urllib import parse
import json
import hashlib
from urllib.request import urlopen


def  xls_Transform(xls_path, lng, lat, co, target_co):
    '''
    xls_path 文件路径
    lng, lat 经度和纬度所在的列名
    co, target_co 原坐标系，目标坐标系
    '''
    df = pd.read_excel(xls_path,encoding='utf-8')
    df['转换后经度'] = None
    df['转换后纬度'] = None
    for i in range(len(df)):
        try:
            if co=='百度坐标系':
                if target_co=='WGS84坐标系':
                    df['转换后经度'][i],df['转换后纬度'][i] = bd09_to_wgs84(float(df[lng][i][:-1]),float(df[lat][i][:-1]))
                elif target_co=='火星坐标系':
                    df['转换后经度'][i],df['转换后纬度'][i] = bd09_to_gcj02(float(df[lng][i][:-1]),float(df[lat][i][:-1]))
            elif co=='WGS84坐标系':
                if target_co=='百度坐标系':
                    df['转换后经度'][i],df['转换后纬度'][i] = wgs84_to_bd09(float(df[lng][i][:-1]),float(df[lat][i][:-1]))
                elif target_co=='火星坐标系':
                    df['转换后经度'][i],df['转换后纬度'][i] = wgs84_to_gcj02(float(df[lng][i][:-1]),float(df[lat][i][:-1]))
            elif co=='火星坐标系':
                if target_co=='WGS84坐标系':
                    df['转换后经度'][i],df['转换后纬度'][i] = gcj02_to_wgs84(float(df[lng][i][:-1]),float(df[lat][i][:-1]))
                elif target_co=='百度坐标系':
                    df['转换后经度'][i],df['转换后纬度'][i] = gcj02_to_bd09(float(df[lng][i][:-1]),float(df[lat][i][:-1]))
            elif co==target_co:
                pass
        except Exception as e:
            pass
    df.to_excel(xls_path, encoding='utf-8')


    
    

def get_placeName_coordinate(xls_path, add, coor):
    '''
    将excel表格中“物业地址”生成各个坐标系的经纬度坐标
    xls_path 文件路径
    add 物业地址所在的列
    co 目标坐标系
    '''
    df = pd.read_excel(xls_path, encoding='utf-8')
    df['%s经度'%add] = None
    df['%s纬度'%add] = None
    
    for i in range(len(df)):
        try:
            address = df[add][i]
            queryStr = '/geocoder/v2/?address=%s&output=json&ak=kN3ruwt5fXbPiG90s4ANB2OLsXc0QdWg' % address 
            encodedStr = parse.quote(queryStr, safe="/:=&?#+!$,;'@()*[]") 
             # 在最后直接追加上yoursk
            rawStr = encodedStr + ',"result":[{"x":113.89585904477322,"y":22.569901714782877}]}' 
             #计算sn
            sn = (hashlib.md5(parse.quote_plus(rawStr).encode("utf8")).hexdigest())  
             #由于URL里面含有中文，所以需要用parse.quote进行处理，然后返回最终可调用的url
            url = parse.quote("http://api.map.baidu.com"+queryStr+"&sn="+sn, safe="/:=&?#+!$,;'@()*[]")  
            req = urlopen(url)
            res = req.read().decode() 
            temp = json.loads(res)
            lat = temp['result']['location']['lat']
            lng = temp['result']['location']['lng']
            if coor=='WGS84坐标系':
                df['%s经度'%add][i], df['%s纬度'%add][i] = bd09_to_wgs84(lng, lat)
            elif coor=='火星坐标系':
                df['%s经度'%add][i], df['%s纬度'%add][i] = bd09_to_gcj02(lng, lat)
            else:
                df['%s经度'%add][i], df['%s纬度'%add][i] = lng, lat
        except Exception as e:
            pass
    df.to_excel(xls_path, encoding='utf-8')
    
    
    
x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 偏心率平方

def gcj02_to_wgs84(lng, lat):
    """
    GCJ02(火星坐标系)转GPS84
    :param lng:火星坐标系的经度
    :param lat:火星坐标系纬度
    :return:
    """
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [lng * 2 - mglng, lat * 2 - mglat]

def _transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
          0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret


def _transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
          0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *
            math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
            math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret

    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [lng * 2 - mglng, lat * 2 - mglat]

def bd09_to_gcj02(bd_lon, bd_lat):
    """
    百度坐标系(BD-09)转火星坐标系(GCJ-02)
    百度——>谷歌、高德
    :param bd_lat:百度坐标纬度
    :param bd_lon:百度坐标经度
    :return:转换后的坐标列表形式
    """
    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
    gg_lng = z * math.cos(theta)
    gg_lat = z * math.sin(theta)
    return [gg_lng, gg_lat]

def gcj02_to_bd09(lng, lat):
    """
    火星坐标系(GCJ-02)转百度坐标系(BD-09)
    谷歌、高德——>百度
    :param lng:火星坐标经度
    :param lat:火星坐标纬度
    :return:
    """
    z = math.sqrt(lng * lng + lat * lat) + 0.00002 * math.sin(lat * x_pi)
    theta = math.atan2(lat, lng) + 0.000003 * math.cos(lng * x_pi)
    bd_lng = z * math.cos(theta) + 0.0065
    bd_lat = z * math.sin(theta) + 0.006
    return [bd_lng, bd_lat]

def bd09_to_wgs84(bd_lon, bd_lat):
    lon, lat = bd09_to_gcj02(bd_lon, bd_lat)
    return gcj02_to_wgs84(lon, lat)


def wgs84_to_bd09(lon, lat):
    lon, lat = wgs84_to_gcj02(lon, lat)
    return gcj02_to_bd09(lon, lat)


def wgs84_to_gcj02(lng, lat):
    """
    WGS84转GCJ02(火星坐标系)
    :param lng:WGS84坐标系的经度
    :param lat:WGS84坐标系的纬度
    :return:
    """
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [mglng, mglat]