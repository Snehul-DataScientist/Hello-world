# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:31:36 2017

@author: snehalpatil
"""
import pandas as pd
import numpy as np
import pdb 
import os
import time
import sys
import shutil
import datetime
import codecs
# import comparer
import xml.etree.cElementTree as ET
# import json_to_csv1
# from json_to_csv1 import *

def getBasePath(in_dir_path):
    in_dir_path = os.path.abspath(in_dir_path)
    in_dir_path = in_dir_path.split('/')
    in_dir_path = '/'.join(in_dir_path[:-1])+'/'
    return in_dir_path

if __name__ == '__main__':
    # print "Execution Started "+ time.strftime("%H:%M:%S")
    dt = datetime.datetime.now()
    dt = dt.date()
    dttime = time.strftime("%H:%M:%S")
    # print (str(dt) + str(dttime))
    
    

    # ##########################################
    # in_dir_path = '/home/ronakshah/Ram/Ancestery.com/46928 OCR - Berkshire Electoral Rolls- Sample images/input/OCR-30Mar2017/Ancestry OCR Project 2nd delivery/'
    in_dir_path = sys.argv[1]
    
    # in_dir_path = mypath + 'Ancestery.com/46928 OCR - Berkshire Electoral Rolls- Sample images/input/OCR files/'
    # out_dir_path = '/home/ronakshah/Ram/Ancestery.com/Output/'
    out_dir_path = sys.argv[2]

    batch = sys.argv[3]

    
    # TXT = mypath + 'Ancestery.com/Output/'+str(dt)+ str(dttime)+'/TXT'
    mypath = getBasePath(in_dir_path)
    # TXT = mypath + 'Ancestery.com/Output/'+str(dt)+ str(dttime)+'/TXT'
    TXT = mypath + 'JETOUT/'+str(dt)+ str(dttime)+'/TXT'
    JSON = mypath + 'JETOUT/'+str(dt)+ str(dttime)+'/JSON'
    JPG = mypath + 'JETOUT/'+str(dt)+ str(dttime)+'/JPG'
    CSV1 = mypath + 'JETOUT/'+str(dt)+ str(dttime)+'/CSV1'
    CSV2 = mypath + 'JETOUT/'+str(dt)+ str(dttime)+'/CSV2'
    CSV3 = mypath + 'JETOUT/'+str(dt)+ str(dttime)+'/CSV3'
    temp_JSON = mypath + 'JETOUT/'+str(dt)+ str(dttime)+'/temp_JSON'
    Archive = mypath + 'JETOUT/'+str(dt)+ str(dttime)+'/Archive'
    #Output = mypath + 'Output/'+str(dt)+ str(dttime)+'/Output'

    jsonfiles = []
    jpgfiles = []
    txtfiles = []
    

    ##########Copy relevant files from OCR directory to Output directory
    print ("Copying files begin"+ time.strftime("%H:%M:%S"))
    for path, subdirs, files in os.walk(in_dir_path):
        subdir = os.path.basename(path)+"/"
        target = os.path.join(out_dir_path,subdir)
        # print (target)
        #print ("Copying files begin"+ time.strftime("%H:%M:%S"))
        for name in [f for f in files if f.lower().endswith("_fr_orgimage.json")]:
            jsonfiles.append(path +'/'+name)
            for i in jsonfiles:
                if jsonfiles != []:                    
                    if not os.path.exists(JSON):
                        os.makedirs(JSON)       
                    shutil.copy(i,JSON)
                    jsonfiles = []
        for name in [f for f in files if f.lower().endswith(".jpg")]:
            jpgfiles.append(path +'/'+name)
            for i in jpgfiles:
                if jpgfiles != []:
                    if not os.path.exists(JPG):
                        os.makedirs(JPG)       
                    shutil.copy(i,JPG)
                    jpgfiles = []

        for name in [f for f in files if f.lower().endswith("_fr_formatted.txt")]:
            txtfiles.append(path +'/'+name)
            for i in txtfiles:
                if txtfiles != []:
                    if not os.path.exists(TXT):
                        os.makedirs(TXT)       
                    shutil.copy(i,TXT)
                    txtfiles = []

        for name in [f for f in files if f.endswith(".xls")]:
            BatchNamelist = []
            Layoutlist = []
            # print name
            if name != []:
                readExcel = pd.ExcelFile(in_dir_path + name)
                sheetName= readExcel.sheet_names[0]
                df = readExcel.parse(sheetName)
                for index, row in df.iterrows():
                    BatchNamelist.append(str(row['Batch Name'].split('d_')[1].strip()))
                    Layoutlist.append(str(row['Type of Layout'].split('Format')[1].strip()))
                dictionary1 = dict(zip(BatchNamelist,Layoutlist))
    
    
    # print(txtfiles)        
    if not os.path.exists(TXT):
        os.makedirs(TXT)       
    if not os.path.exists(JSON):
        os.makedirs(JSON)       
    if not os.path.exists(JPG):
        os.makedirs(JPG)       
    if not os.path.exists(CSV1):
        os.makedirs(CSV1)       
    if not os.path.exists(CSV2):
        os.makedirs(CSV2)       
    if not os.path.exists(CSV3):
        os.makedirs(CSV3)       
    if not os.path.exists(temp_JSON):
        os.makedirs(temp_JSON)
    # if not os.path.exists(Archive):
    #     os.makedirs(Archive)
    # if not os.path.exists(Output):
    #     os.makedirs(Output)       
    TXT = TXT+"/"
    CSV1 = CSV1+"/"
    CSV2 = CSV2+"/"
    CSV3 = CSV3+"/"
    temp_JSON = temp_JSON+"/"
    Archive = Archive+"/"
    #Output = Output+"/"


    Type_1 = [1,2,4,5,9]
    Type_2 = [3,6,7,8,10]

    # print (dictionary1)

    '''

    try:
        for key, value in dictionary1.iteritems():
            print (key, value)
            if int(value) in Type_1:
                os.system('python ancestmain_debug.py ' + TXT+" " + " " + CSV1)
                os.system('python jsonextra_multiple_vfinal.py ' + JSON+" " + " " + CSV2)
                os.system('python Ances_cord_v2.py ' + CSV1+" " + " " + CSV2+" "+" "+CSV3)
                os.system('python csv_jon_v1.py ' + CSV3+" " + " " + temp_JSON)
                os.system('python wrapper_ancesv2.py ' + temp_JSON+" " + " " + Archive+" "+" "+Output)
            else:
                os.system('python ancestmain_T2.py ' + TXT+" " + " " + CSV1)
                os.system('python jsonextra_multiple_vfinal.py ' + JSON+" " + " " + CSV2)
                os.system('python Ances_cord_v2.py ' + CSV1+" " + " " + CSV2+" "+" "+CSV3)
                os.system('python csv_jon_v1.py ' + CSV3+" " + " " + temp_JSON)
                os.system('python wrapper_ancesv2.py ' + temp_JSON+" " + " " + Archive+" "+" "+Output)
    except:
        pass

    '''
    
    try:
    #os.system('python ancestmain_debug.py ' + TXT+" " + " " + CSV1)
        # pdb.set_trace()
        os.system('python ancestmain_debug.py ' + TXT+" " + " " + CSV1)
        os.system('python jsonextra_multiple_vfinal.py ' + JSON+" " + " " + CSV2)
        os.system('python Ances_cord_v2.py ' + CSV1+" " + " " + CSV2+" "+" "+CSV3)
        os.system('python csv_jon_v1.py ' + CSV3+" " + " " + temp_JSON)
        os.system('python wrapper_ancesv2.py ' + temp_JSON+" " + " " + Archive+" "+" "+out_dir_path + " " + in_dir_path + " " + batch )
        # os.system('python wrapper_ancesv2.py ' + temp_JSON+" " + " " + Archive)
    except:
        pass

    
