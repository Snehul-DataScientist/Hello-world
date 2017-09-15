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
import datetime


import xml.etree.cElementTree as ET

id_for_files = {}

def file_fetch_rename(IN_dir_path, OUT_dir_path):
    textFiles = []
    imgFiles = []
    filenames = os.listdir(IN_dir_path)
    for name in [fi for fi in filenames if fi.lower().endswith("_fr_formatted.txt")]:
        textFiles.append(os.path.join(IN_dir_path, name))
    for filename in textFiles:
        shutil.copy(filename, OUT_dir_path)
        shutil.move(os.path.join(OUT_dir_path,os.path.basename(filename)), os.path.join(OUT_dir_path,os.path.basename(filename).split(".")[0]+"_fr_formatted.txt"))
    for name in [fi for fi in filenames if fi.lower().endswith(".jpg")]:
            imgFiles.append(os.path.join(IN_dir_path, name))
    for filename in imgFiles:
        shutil.copy(filename, OUT_dir_path)
        shutil.move(os.path.join(OUT_dir_path,os.path.basename(filename)), os.path.join(OUT_dir_path,os.path.basename(filename).split(".")[0]+".JPG")) 
    return




def file_fetch_json(IN_dir_path1,OUT_dir_path11,foldr_base):
    jsonFiles = []
    filenames = os.listdir(IN_dir_path1)
    
    for name in [fi for fi in filenames if fi.lower().endswith("_output.csv.json")]:
        jsonFiles.append(os.path.join(IN_dir_path1, name))
    
    for filename in jsonFiles:
        fi = os.path.basename(filename).split("_output")[0]
        # print fi
        
        for i in range(len(foldr_base)):
            if fi == foldr_base[i]:
                shutil.copy(os.path.join(IN_dir_path1,os.path.basename(filename)),os.path.join(OUT_dir_path11 +"/"+ fi))
        #shutil.copy(os.path.join(IN_dir_path1,os.path.basename(filename)),os.path.join(OUT_dir_path1+ fi +"_j2k"))

            else:
                pass
    return

def getBasePath(path):
    if path.strip(' ')[-1] == "/":
        path = path[:-1]

    path = '/'.join(path.split('/')[:-1])
    return path + "/"


if __name__ == '__main__':
    dt = datetime.datetime.now()
    dt = dt.date()
    dttime = time.strftime("%H:%M:%S")
    temp_JSON = sys.argv[1]
    Archive = sys.argv[2]
    out_dir_path = sys.argv[3]
    in_dir_path = sys.argv[4]
    batch = sys.argv[5]
    basepath = getBasePath(out_dir_path)
        
        
    Ocrpath = in_dir_path + "/" +  batch

    #Ocrpath = mypath + 'OCR-30Mar2017'
    for path,subdirs,files in os.walk(Ocrpath):
        Batch = subdirs[0].split('-')[0]
        break

    Out_dir_path = out_dir_path+'/'+Batch +'/'
    Arc_dir_path = basepath + 'JETOUT/Archive/'+'/'+Batch +'/'
    Error_dir_path = basepath + 'JETOUT/Error/'+'/'+Batch +'/'
    
##############Creating output batchwise#####################################################################
    
    folders = [ name for name in os.listdir(Ocrpath) if os.path.isdir(os.path.join(Ocrpath, name)) ]

    print "Execution Started "+ time.strftime("%H:%M:%S")
    for fldr in folders: 
        # print fldr
        print fldr
        IN_dir_path = os.path.join(Ocrpath,fldr)        
        OUT_dir_path = os.path.join(Out_dir_path,fldr)  
        ARC_dir_path = os.path.join(Arc_dir_path,fldr)  
        if not os.path.exists(OUT_dir_path):
            os.makedirs(OUT_dir_path)  
        if not os.path.exists(ARC_dir_path):
            os.makedirs(ARC_dir_path)  
        if not os.path.exists(Error_dir_path):
            os.makedirs(Error_dir_path)  
        file_fetch_rename(IN_dir_path, OUT_dir_path)                                        
        file_fetch_rename(IN_dir_path, ARC_dir_path)                                        

    folders1 = [ name for name in os.listdir(Out_dir_path) if os.path.isdir(os.path.join(Out_dir_path, name)) ]
    foldr_base =[]
    for foldr in folders1:
        # f_base = foldr
        f_base = foldr.split("_j2k")[0]        
        foldr_base.append(f_base)
        # IN_dir_path1="/home/snehalpatil/Desktop/ANCESTORY/4.Box_office_json/output/"   ####from temp json_path
        # IN_dir_path1=mypath + 'Ancestery.com/Output/JETOUT/temp_JSON'####from temp json_path
        #IN_dir_path1 = sys.argv[1]
        #OUT_dir_path1 =mypath + 'Output/BO_OUT/'+str(dt)+ str(dttime)+'/'+Batch +'/' ###to outputput folders
                

        # Arc_dir_path = mypath + '/Ancestery.com/Output/JETOUT/Archive/ + foldr'
        #ARC_dir_path1 = sys.argv[2]

        OUT_dir_path11 = out_dir_path + "/" + foldr.split('-')[0] + "/"
    ARC_dir_path = Arc_dir_path

    file_fetch_json(temp_JSON, ARC_dir_path,foldr_base)
    file_fetch_json(temp_JSON, OUT_dir_path11,foldr_base)

    clt_path = out_dir_path + "/" + "cltfiles/"
    if not os.path.exists(clt_path):
	os.makedirs(clt_path)

    f = open(clt_path + Batch+'.clt','wb+')
    f.write("")
    f.close()
    
    













 
