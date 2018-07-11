# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 11:09:51 2018

@author: YJT
"""
import arcpy,os,os.path,init

def projectRaster(rootPath):
    try:
        
        ##arcpy工作目录
        root_path = rootPath
        arcpy.env.workspace = root_path

        ##待处理文件所在目录(相对于根目录)
        input_path = r"安监"
        output_path = "data"

        ##源坐标系 "CGCS2000_3_Degree_GK_CM_123E" 
        sourceSR = arcpy.SpatialReference("CGCS2000 3 Degree GK CM 123E")
        ##目标坐标系(WGS 1984 Web Mercator Auxiliary Sphere)
        targetSR = arcpy.SpatialReference("WGS 1984 Web Mercator (auxiliary sphere)")

        ##遍历目录，查找栅格数据
        files = os.listdir(root_path+os.sep+input_path)
        for f in files:
            if os.path.splitext(f)[1].upper() == ".shp":
                fileName = os.path.splitext(f)[0] + ".shp"
                in_dataset = input_path + os.sep + fileName
                out_dataset = output_path + os.sep + fileName

                print "begin project "+in_dataset+" from: " +sourceSR.name+" to: "+targetSR.name
                
                arcpy.ProjectRaster_management(in_dataset, out_dataset, targetSR, "NEAREST",\
                                       "#", "#", "#",sourceSR)

        print "project success!"
        
    except arcpy.ExecuteError:
        print "Project Raster example failed."
        print arcpy.GetMessages()

################################################
if __name__ == '__main__':

    #指定处理文件根目录
    root_path = r"E:\SpecData40"
    projectRaster(root_path)