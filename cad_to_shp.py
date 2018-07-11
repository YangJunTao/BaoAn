# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 19:47:50 2018

@author: SZU
"""

import arcpy
import os
from arcpy import env
from arcpy import interop

# 转换文件夹地址
input_cad_folder = "E:\\"
output_gdb_folder = "E:\\"
output_folder="E:\\"

for found_file in os.listdir(input_cad_folder):
    if found_file.endswith(".dwg"):

        print "Converting: "+found_file
        input_cad_dataset = os.path.join(input_cad_folder, found_file)
        print "Converting: "+input_cad_dataset
        output_gdb = found_file.split(".")[0] +".gdb"
        output_gdb_path = os.path.join(output_gdb_folder, output_gdb)
        print "Converting: "+output_gdb_path
        try:
            interop.QuickImport(input_cad_dataset, output_gdb_path)
            env.workspace = output_gdb_path
            fcs = arcpy.ListFeatureClasses("*")
            output_shp_path=output_folder+output_gdb.split(".")[0]
            print "Create: "+output_shp_path
            os.makedirs(output_shp_path)
            for fc in fcs: 
                outfc = arcpy.ValidateTableName(fc)
                print "Create: "+outfc
                arcpy.FeatureClassToShapefile_conversion([outfc], output_shp_path) 
        except:
            print arcpy.GetMessages()