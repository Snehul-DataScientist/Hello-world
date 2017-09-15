# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 15:08:15 2017

@author: snehalpatil
"""

import pandas as pd
import numpy as np
import pdb 
import os
from iteration_utilities import flatten



def firs_cord(result1):
    giv=[]
    vav=[]    
    for i in range(len(result1)):
        # pdb.set_trace()
        w=result1['First_name'][i]
        if len(w) == 1:
            if type(w) == dict:
                y = w.keys()
                v= w.values()
                giv.append(y)
                vav.append(v)
            else:
                w1=result1['First_name'][i][0]
                y1=w1.keys()
                y2=w1.values()
                giv.append(y1)
                vav.append(y2)
        else:
            j1=""
            j2=""
            giv.append(j1)
            vav.append(j2)   
    df6 = pd.DataFrame({"First_Name_c": giv, "GivenName_xy1" :vav})
    return df6

def firs1_cord(result1):
    giv=[]
    vav=[]    
    for i in range(len(result1)):
        w=result1['First_name_1'][i]
        if len(w) == 1:
            if type(w) == dict:
                y = w.keys()
                v= w.values()
                giv.append(y)
                vav.append(v)
            else:
                w1=result1['First_name_1'][i][0]
                y1=w1.keys()
                y2=w1.values()
                giv.append(y1)
                vav.append(y2)
        else:
            j1=""
            j2=""
            giv.append(j1)
            vav.append(j2)   

    df7 = pd.DataFrame({"First_Name2_c": giv, "GivenName_xy2" :vav})
    return df7

def las1_cord(result1):
    giv=[]
    vav=[]    
    for i in range(len(result1)):
        w=result1['Last_name_1'][i]
        if len(w) == 1:
            if type(w) == dict:
                y = w.keys()
                v= w.values()
                giv.append(y)
                vav.append(v)
            else:
                y1=w[0].keys()
                y2=w[0].values()
                giv.append(y1)
                vav.append(y2)
        else:
             j1=""
             j2=""
             giv.append(j1)
             vav.append(j2)
    df8 = pd.DataFrame({"LastName1_c": giv, "lastName_xy1" :vav})
    return df8
  

def las2_cord(result1):
    giv=[]
    vav=[]    
    for i in range(len(result1)):
        w=result1['Last_name_2'][i]
        if len(w) == 1:
            if type(w) == dict:
                y = w.keys()
                v= w.values()
                giv.append(y)
                vav.append(v)
            else:
                w1=result1['Last_name_2'][i][0]
                y1=w1.keys()
                y2=w1.values()
                giv.append(y1)
                vav.append(y2)
        else:
             j1=""
             j2=""
             giv.append(j1)
             vav.append(j2)
    df9 = pd.DataFrame({"LastName2_c": giv, "lastName_xy2" :vav})
    return df9

def Occ1_cord(result1):
    giv=[]
    vav=[]    
    for i in range(len(result1)):
        w=result1['Occupation_1'][i]
        if len(w) == 1:
            if type(w) == dict:
                y = w.keys()
                v= w.values()
                giv.append(y)
                vav.append(v)
            else:
                w1=result1['Occupation_1'][i][0]
                y1=w1.keys()
                y2=w1.values()
                giv.append(y1)
                vav.append(y2)
        else:
             j1=""
             j2=""
             giv.append(j1)
             vav.append(j2)
    df10 = pd.DataFrame({"OccName1_c": giv, "Occ_xy1" :vav})
    return df10
    
def Occ2_cord(result1):
    giv=[]
    vav=[]    
    for i in range(len(result1)):
        w=result1['Occupation_2'][i]
        if len(w) == 1:
            if type(w) == dict:
                y = w.keys()
                v= w.values()
                giv.append(y)
                vav.append(v)
            else:
                w1=result1['Occupation_2'][i][0]
                y1=w1.keys()
                y2=w1.values()
                giv.append(y1)
                vav.append(y2)
        else:
            j1=""
            j2=""
            giv.append(j1)
            vav.append(j2)
          
    #print len(giv),len(vav)
    df11 = pd.DataFrame({"OccName2_c": giv, "Occ_xy2" :vav})
    return df11

def add1_cord(result1):
    giv=[]
    vav=[]    
    for i in range(len(result1)):
        w=result1['add_1'][i]
        if len(w) == 1:
            if type(w) == dict:
                y = w.keys()
                v= w.values()
                giv.append(y)
                vav.append(v)
            else:
                w1=result1['add_1'][i][0]
                y1=w1.keys()
                y2=w1.values()
                giv.append(y1)
                vav.append(y2)
        else:
            j1=""
            j2=""
            giv.append(j1)
            vav.append(j2)
    #print len(giv),len(vav)
    df12 = pd.DataFrame({"AddName1_c": giv, "Add_xy1" :vav})
    return df12    
 
def add2_cord(result1):
    giv=[]
    vav=[]    
    for i in range(len(result1)):
        w=result1['add_2'][i]
        if type(w) == dict:
            y = w.keys()
            v= w.values()
            giv.append(y)
            vav.append(v)
        else:
            y1=list(flatten(w))
            y2=""
            giv.append(y1)
            vav.append(y2)
    #print len(giv),len(vav)
    df13 = pd.DataFrame({"AddName2_c": giv, "Add_xy2" :vav})
    return df13      
    
def prefix_cord(result1):
    giv=[]
    vav=[]    
    for i in range(len(result1)):
        w=result1['Prefix_1'][i]
        if len(w) == 1:
            if type(w) == dict:
                y = w.keys()
                v= w.values()
                giv.append(y)
                vav.append(v)
            else:
                w1=result1['Prefix_1'][i][0]
                y1=w1.keys()
                y2=w1.values()
                giv.append(y1)
                vav.append(y2)
        else:
            j1=""
            j2=""
            giv.append(j1)
            vav.append(j2)
    #print len(giv),len(vav)
    df13 = pd.DataFrame({"PrefixName2_c": giv, "Prefix_xy1" :vav})
    return df13   

def prefix2_cord(result1):
    giv=[]
    vav=[]    
    for i in range(len(result1)):
        w=result1['Prefix_2'][i]
        if len(w) == 1:
            if type(w) == dict:
                y = w.keys()
                v= w.values()
                giv.append(y)
                vav.append(v)
            else:
                w1=result1['Prefix_2'][i][0]
                y1=w1.keys()
                y2=w1.values()
                giv.append(y1)
                vav.append(y2)
        else:
            j1=""
            j2=""
            giv.append(j1)
            vav.append(j2)
    #print len(giv),len(vav)
    df13 = pd.DataFrame({"PrefixName2_c": giv, "Prefix_xy2" :vav})
    return df13      

def suffix_cord(result1):
    giv=[]
    vav=[]    
    for i in range(len(result1)):
        w=result1['Suffix_1'][i]
        if len(w) == 1:
            if type(w) == dict:
                y = w.keys()
                v= w.values()
                giv.append(y)
                vav.append(v)
            else:
                w1=result1['Suffix_1'][i][0]
                y1=w1.keys()
                y2=w1.values()
                giv.append(y1)
                vav.append(y2)
        else:
            j1=""
            j2=""
            giv.append(j1)
            vav.append(j2)
    #print len(giv),len(vav)
    df13 = pd.DataFrame({"suffixName1_c": giv, "Suffix_1_xy1" :vav})
    return df13   
    
def suffix2_cord(result1):
    giv=[]
    vav=[]    
    for i in range(len(result1)):
        w=result1['Suffix_2'][i]
        if len(w) == 1:
            if type(w) == dict:
                y = w.keys()
                v= w.values()
                giv.append(y)
                vav.append(v)
            else:
                w1=result1['Suffix_2'][i][0]
                y1=w1.keys()
                y2=w1.values()
                giv.append(y1)
                vav.append(y2)
        else:
            j1=""
            j2=""
            giv.append(j1)
            vav.append(j2)
    #print len(giv),len(vav)
    df13 = pd.DataFrame({"suffix_name2_c": giv, "Suffix_2_xy2" :vav})
    return df13   