# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:56:35 2017

@author: snehalpatil
"""

import pandas as pd
import numpy as np
import pdb 
import os
import sys
import Output_processing_1
import Output_processing2
from iteration_utilities import flatten
from Output_processing_1 import *
from Output_processing2 import *
from itertools import izip
import datetime
   
def x2y2calc(df): ####Calculating x2 and y2 co-ordinates
    try:
       df['x2']=df['x1'] + df['width1']
       df['y2']=df['y1'] - df['Height1']
    except:
       pass
    return df
#############Matching the words and gettiing the co=ordinates from the dataframe#######################
def word_coord(word):
    try:
        tdf=df[df['txt1'].str.contains(word, regex=False)]
        if tdf.empty:    
            coord=rowname=""
        else:
            tdf=tdf.iloc[0,3:7]
            coord=str(tdf[0])+","+str(tdf[1])+","+str(tdf[2])+","+str(tdf[3])
            rowname=tdf.name
    except:
        pass
    return (coord, rowname)
    
def worddict(wordlist):
    try:
        wordlist=wordlist.split()    
    
        worddictlist=[]
    
        for word in wordlist:        
            wordcoord={word:word_coord(word)[0]}
            worddictlist.append(wordcoord)
            idx=word_coord(word)[1]
            if idx !="":
                df.drop(word_coord(word)[1], inplace=True)
    except:
        pass
    return (worddictlist)
    
def stringlist(rowstringlist):
    try:
        stringdictlist=[]
        for string in rowstringlist:
            strdict=worddict(string)
            stringdictlist.append(strdict)
    except:
        pass
    return(stringdictlist) 
#########################################################################################    
################For getting the last name f ########################################
    #################################################################################
######Extraction of respective words and co-ordinates from the dataframe###################
#########################################################################################
def last_name(df4):   
    try:
        g=[]
        y=[]
        file_name=[]
        for i in range(len(df4)):
            leng =len(df4[i][3])
            if leng > 1:
                j = leng - 1
                fir_nam = df4[i][3][0] 
                file_n = df4[0][0] 
                las_nam = df4[i][3][j] 
                g.append(fir_nam)
                y.append(las_nam)
                file_name.append(file_n)
                
                
            else:
                l = df4[i][3]
                file_n = df4[0][0] 
                las = "NA"
                g.append(l)
                y.append(las)
                file_name.append(file_n)
           
        df_v = pd.DataFrame({"FileName":file_name, "Last_name_1": g, "Last_name_2" :y})
    except:
        pass
    return df_v     
###################For getting the firstname######################  
    
def first_name(df4):
    try:    
        g=[]
        y=[]
        file_name=[]
        for i in range(len(df4)):
            leng =len(df4[i][2])
            if leng > 1:
                j = leng - 1
                fir_nam = df4[i][2][0] 
                las_nam = df4[i][2][j] 
                file_n = df4[0][0]
                # pdb.set_trace() 
                g.append(fir_nam)
                y.append(las_nam)
                file_name.append(file_n)
                
                
            else:
                l = df4[i][2]
                file_n = df4[0][0] 
                las = "NA"
                g.append(l)
                y.append(las)
                file_name.append(file_n)
           
        df_va = pd.DataFrame({"First_name": g, "First_name_1" :y})
    except:
        pass
    return df_va     
##############################################################33
######Extracting occupation as well as address#############
def occ(df4):
    try:
        g=[]
        y=[]
        file_name=[]
        df_vali=pd.DataFrame() 
        for i in range(len(df4)):
            leng =len(df4[i][6])
            if leng > 1:
                j = leng - 1
                fir_occ = df4[i][6][0] 
                las_occ = df4[i][6][j]
                file_n = df4[0][0] 
                g.append(fir_occ)
                y.append(las_occ)
                file_name.append(file_n)
                
            else:
                l = df4[i][6]
                file_n = df4[0][0]
                las = "NA"
                g.append(l)
                y.append(las)
                file_name.append(file_n)
       
        df_vali = pd.DataFrame({"Occupation_1": g, "Occupation_2" :y})
    except:
          pass
    return df_vali
    
##########################################################
def prefix(df4):
    try:
        g=[]
        y=[]
        file_name=[]
        df_vali=pd.DataFrame() 
        for i in range(len(df4)):
            leng =len(df4[i][4])
            if leng > 1:
                j = leng - 1
                fir_occ = df4[i][4][0] 
                las_occ = df4[i][4][j]
                file_n = df4[0][0] 
                g.append(fir_occ)
                y.append(las_occ)
                file_name.append(file_n)
                
            else:
                l = df4[i][4]
                file_n = df4[0][0]
                las = "NA"
                g.append(l)
                y.append(las)
                file_name.append(file_n)
       
        df_validd = pd.DataFrame({"Prefix_1": g, "Prefix_2" :y})
    except:
        pass
    return df_validd
##################################################3
    
def suffix(df4):
    try:
        g=[]
        y=[]
        file_name=[]
        df_vali=pd.DataFrame() 
        for i in range(len(df4)):
            leng =len(df4[i][5])
            if leng > 1:
                j = leng - 1
                fir_occ = df4[i][5][0] 
                las_occ = df4[i][5][j]
                file_n = df4[0][0] 
                g.append(fir_occ)
                y.append(las_occ)
                file_name.append(file_n)
                
            else:
                l = df4[i][5]
                file_n = df4[0][0]
                las = "NA"
                g.append(l)
                y.append(las)
                file_name.append(file_n)
       
        df_val = pd.DataFrame({"Suffix_1": g, "Suffix_2" :y})
    except:
        pass
    return df_val
######################################################
def add(df4):
    try:
        g=[]
        y=[]
        file_name=[]
        df_vali=pd.DataFrame() 
        for i in range(len(df4)):
            leng =len(df4[i][7])
            if leng > 1:
                j = leng - 1
                fir_occ = df4[i][7][0] 
                las_occ = df4[i][7][j]
                file_n = df4[0][0] 
                g.append(fir_occ)
                y.append(las_occ)
                file_name.append(file_n)
                
            else:
                l = df4[i][7]
                file_n = df4[0][0]
                las = "NA"
                g.append(l)
                y.append(las)
                file_name.append(file_n)
       
        df_valid = pd.DataFrame({"add_1": g, "add_2" :y})
    except:
        pass
    return df_valid
#########################################################
######################################################################################### 
    
    
def main_processing(df,df2):
    try:
        df3=pd.DataFrame({'row':df2.as_matrix(columns=None).tolist()})   
        df4=df3['row'].apply(stringlist) 
        df_va=first_name(df4)
        df_v=last_name(df4)
        df_vali=occ(df4)
        df_valid=add(df4)
        df_validd=prefix(df4)
        df_val=suffix(df4)
        frames = [df_va, df_v, df_vali,df_valid,df_validd,df_val,df2]
        result = pd.concat(frames,axis=1)  
        result1=result
        A=Output_processing_1.firs_cord(result1)
        B=Output_processing_1.firs1_cord(result1)
        C=Output_processing_1.las1_cord(result1)
        D=Output_processing_1.las2_cord(result1)
        E=Output_processing_1.Occ1_cord(result1)
        F=Output_processing_1.Occ2_cord(result1)
        G=Output_processing_1.add1_cord(result1)
        H=Output_processing_1.add2_cord(result1)
        I=Output_processing_1.prefix_cord(result1)
        J=Output_processing_1.prefix2_cord(result1)
        K=Output_processing_1.suffix_cord(result1)
        L=Output_processing_1.suffix2_cord(result1)
        frames=[A,B,C,D,E,F,G,H,I,J,K,L,df2]
        f_result = pd.concat(frames,axis=1)
        final_result=f_result[['FileName','Sno','GivenName','GivenName_xy1','GivenName_xy2','SurName','lastName_xy1','lastName_xy2','Prefix','Prefix_xy1','Prefix_xy2','Suffix','Suffix_1_xy1','Suffix_2_xy2','Occupation','Occ_xy1','Occ_xy2','Address','Add_xy1','Add_xy2']]
        GivenName_x1y1x2y2=Output_processing2.final_x2y2_Firstname(final_result)
        SurName_x1y1x2y2=Output_processing2.final_x2y2_lastname(final_result)
        Occupation_x1y1x2y2=Output_processing2.final_x2y2_occ(final_result)
        Address_x1y1x2y2=Output_processing2.final_x2y2_add(final_result)
        M=Output_processing2.prefix(final_result)
        N=Output_processing2.suffix(final_result)   
        frames=[GivenName_x1y1x2y2,SurName_x1y1x2y2,Occupation_x1y1x2y2,Address_x1y1x2y2,M,N,final_result]
        final_result1 = pd.concat(frames,axis=1)   
        final_result2=final_result1[['FileName','Sno','GivenName','GivenName_x1y1x2y2','SurName','SurName_x1y1x2y2','Prefix','Prefix_x1y1x2y2','Suffix','Suffix_x1y1x2y2','Occupation','Occupation_x1y1x2y2','Address','Address_x1y1x2y2']]
        final_result2.to_csv(out_dir_path+file_base+"_output.csv", encoding='utf-8', index=False)
    except:
        pass

   
if __name__ == '__main__':  
    
    
    # mypath = "/home/snehalpatil/Desktop"
    # in_dir_path = mypath + '/ANCESTORY/1.2.Format2_extraction_Ramcode/output2/' ###extracted words
    # in_dir_path2 = mypath + '/ANCESTORY/1.json_to_csv/output2/'
    # out_dir_path = mypath + '/ANCESTORY/5.Finding co-ordinates-Ances_Model_april7/output/output160/'

    # mypath = "/home/snehalpatil/Desktop"
    # in_dir_path = '/home/ronakshah/Ram/Ancestery.com/Output/2017-05-05/CSV1/' ###extracted words
    # in_dir_path2 = '/home/ronakshah/Ram/Ancestery.com/Output/2017-05-05/CSV2/'
    # out_dir_path = '/home/ronakshah/Ram/Ancestery.com/Output/2017-05-05/CSV3/'
    
    dt = datetime.datetime.now()
    dt = dt.date()
    # print (dt)
    in_dir_path = sys.argv[1]
    in_dir_path2 = sys.argv[2]
    out_dir_path = sys.argv[3]



    csvfiles = []
    outputlist = []

    csvfiles = os.listdir(in_dir_path)
    # print (csvfiles)
    
    # for path, subdirs, files in os.walk(in_dir_path):
    #     for name in [f for f in files if f.endswith(".csv")]:
    #         csvfiles.append(path +name)
            
    for i in range (0, len(csvfiles)):
        output = os.path.basename(csvfiles[i])
        outputlist.append(output)
        

    outputlist.sort()
        
            
    csvfiles1 = []
    outputlist1 = []


    # for path, subdirs, files in os.walk(in_dir_path2):
    #     for name in [f for f in files if f.endswith(".csv")]:
    #         csvfiles1.append(path +'/'+name)

    csvfiles1 = os.listdir(in_dir_path2)
    # print (csvfiles1)
            
    for i in range (0, len(csvfiles1)):
        output1 = os.path.basename(csvfiles1[i])
        outputlist1.append(output1)
        

    outputlist1.sort()
    for file in outputlist1:
        file_base=os.path.basename(file).split("_FR")[0]
        #file_base=os.path.basename(file).split(".single")[0]
        path=in_dir_path2+file_base + "_FR_orgimage.json_output.csv"
        #path=in_dir_path2+file_base
        #path1=in_dir_path+str(dt)+file_base
        path1=in_dir_path+str(dt)+file_base + "_FR_formatted.txt_output.csv"

        flag_path1 = False
        if os.path.exists(path):
            df = pd.read_csv(path, dtype={'Filename': object},sep=',',keep_default_na=False)
            # pdb.set_trace()
            df=x2y2calc(df) 
            flag_path1 = True
        else:
            print "Path doesn't exist:",path
        
        flag_path2 = False
        if os.path.exists(path1):
            df2 = pd.read_csv(path1, dtype={'Filename': object},sep=',',keep_default_na=False)
            flag_path2 = True
        else:
            print "Path doesn't exist:",path1
        
        if flag_path1 and flag_path2:
            main_processing(df,df2)
    
    

    
  
