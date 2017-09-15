# -*- coding: utf-8 -*-
"""
Created on Thu May  4 10:57:16 2017

@author: snehalpatil
"""

import os
import sys
import pdb
import shutil
import csv_json_v2
from csv_json_v2 import *


import time

import xml.etree.cElementTree as ET

id_for_files = {}

def json_conv_box(in_dir_path_json,out_dir_path_json):       
    csvfiles = []
    outputlist = []
    
    for path, subdirs, files in os.walk(in_dir_path_json):
        for name in [f for f in files if f.endswith(".csv")]:
            csvfiles.append(path +name)
            
    for i in range (0, len(csvfiles)):
        output = os.path.basename(csvfiles[i])
        outputlist.append(output) 
    return outputlist


if __name__ == '__main__':
    # mypath = "/home/snehalpatil/Desktop"
        
    
    ####################################
    # in_dir_path_json = mypath + '/ANCESTORY/5.Finding co-ordinates-Ances_Model_april7/output/output160/' ###extracted words
    # out_dir_path_json = mypath + '/ANCESTORY/4.Box_office_json/output/'
    ####################################
    

    ####################################
    # in_dir_path_json = '/home/ronakshah/Ram/Ancestery.com/Output/2017-05-05/CSV3/' ###extracted words
    # out_dir_path_json = '/home/ronakshah/Ram/Ancestery.com/Output/2017-05-05/temp_JSON/'
    ####################################

    in_dir_path_json = sys.argv[1]
    out_dir_path_json = sys.argv[2]


    outputlist=json_conv_box(in_dir_path_json,out_dir_path_json)
    # pdb.set_trace()
    csv_json_v2.extract(outputlist,in_dir_path_json,out_dir_path_json)   
    
    






