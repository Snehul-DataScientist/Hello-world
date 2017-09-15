# -*- coding: utf-8 -*-
"""
Created on Thu May 18 12:41:44 2017

@author: snehalpatil
"""

import pandas as pd
import numpy as np
import pdb 
import os
from iteration_utilities import flatten

############Here we are aplitting the string and taking the first co-ord and last cord instance of the string t
##########OUtput processing2##############################

def cell_is_valid(cell):
    if len(cell) == 1:
        if len(cell[0].split(',')) == 4:
            return True
        else:
            return False
    else:
        return False

def final_x2y2_Firstname(final_result):
    l=[]
    m=[]
    n=[]
    q=[]
    f_co_ord=[]
    for i in range(len(final_result)):
        w = final_result['GivenName_xy1'][i]
        w1 = final_result['GivenName_xy2'][i]   
        if cell_is_valid(w) and cell_is_valid(w1):          
            t=w[0].split(',')
            t1=w1[0].split(',')  
            l=[t[0],t1[0]]
            m=[t[1],t1[1]]
            n=[t[2],t1[2]]
            q=[t[3],t1[3]]
            co_ord= min(l,key=int) + '$'+ min(m,key=int)+ '$' + max(n,key=int) + '$'+ max(q,key=int)
            f_co_ord.append(co_ord)
        elif cell_is_valid(w) and (not cell_is_valid(w1)):
            h=w[0].split(',') 
            co_ord2 = h[0] + '$'+ h[1] + '$'+ h[2] + '$'+ h[3]
            f_co_ord.append(co_ord2)
        elif (not cell_is_valid(w)) and cell_is_valid(w1):
            h=w1[0].split(',') 
            co_ord2 = h[0] + '$'+ h[1] + '$'+ h[2] + '$'+ h[3]
            f_co_ord.append(co_ord2)
        else:
            co_ord11 = ""
            f_co_ord.append(co_ord11)
    df8 = pd.DataFrame({"GivenName_x1y1x2y2": f_co_ord})
    return df8
#######################Check for last name#######################
def final_x2y2_lastname(final_result):
    f_co_ord=[]
    for i in range(len(final_result)):
        w = final_result['lastName_xy1'][i]
        w1 = final_result['lastName_xy2'][i]
        #print w,w1
      
        if (len(w) >= 1):
            t=w[0].split(',')
            if (len(t) >= 4):
                co_ord = t[0] + '$'+ t[1] + '$'+ t[2] + '$'+ t[3]
                #print co_ord
                f_co_ord.append(co_ord)
            else:
                co_ord1 = ""
                f_co_ord.append(co_ord1)
        else:
            co_ord1 = ""
            f_co_ord.append(co_ord1)
    df11 = pd.DataFrame({"SurName_x1y1x2y2": f_co_ord})
    return df11
    
def final_x2y2_occ(final_result):
    f_co_ord=[]
    for i in range(len(final_result)):
        w = final_result['Occ_xy1'][i]
        w1 = final_result['Occ_xy2'][i]
      
        if (len(w) >= 1) and (len(w1) >= 1):
            t=w[0].split(',')
            t1=w1[0].split(',')
            if (len(t) >= 4) and (len(t1) >= 4):
                l=[t[0],t1[0]]
                m=[t[1],t1[1]]
                n=[t[2],t1[2]]
                q=[t[3],t1[3]]
                co_ord= min(l,key=int) + '$'+ min(m,key=int)+ '$' + max(n,key=int) + '$'+ max(q,key=int)
                f_co_ord.append(co_ord)
            else:
                co_ord1 = ""
                f_co_ord.append(co_ord1)
        else:
            co_ord1 = ""
            f_co_ord.append(co_ord1)
    df12 = pd.DataFrame({"Occupation_x1y1x2y2": f_co_ord})
    return df12
    
def final_x2y2_add(final_result):
    f_co_ord=[]
    for i in range(len(final_result)):
        w = final_result['Add_xy1'][i]
        w1 = final_result['Add_xy2'][i]
      
        if (len(w) >= 1) and (len(w1) >= 1):
            t=w[0].split(',')
            t1=w1[0].split(',')
            if (len(t) >= 4) and (len(t1) >= 4):
                co_ord = t[0] + '$'+ t[1] + '$'+ t1[2] + '$'+ t1[3]
                #print co_ord
                f_co_ord.append(co_ord)
            else:
                co_ord1 = ""
                f_co_ord.append(co_ord1)
        else:
            co_ord1 = ""
            f_co_ord.append(co_ord1)
    df13 = pd.DataFrame({"Address_x1y1x2y2": f_co_ord})
    return df13
    
def prefix(final_result):
    f_co_ord=[]
    for i in range(len(final_result)):
        w = final_result['Prefix_xy1'][i]
        w1 = final_result['Prefix_xy2'][i]
      
        if (len(w) >= 1) and (len(w1) >= 1):
            t=w[0].split(',')
            t1=w1[0].split(',')
            if (len(t) >= 4) and (len(t1) >= 4):
                co_ord = t[0] + '$'+ t[1] + '$'+ t1[2] + '$'+ t1[3]
                #print co_ord
                f_co_ord.append(co_ord)
            else:
                co_ord1 = ""
                f_co_ord.append(co_ord1)
        else:
            co_ord1 = ""
            f_co_ord.append(co_ord1)
    df13 = pd.DataFrame({"Prefix_x1y1x2y2": f_co_ord})
    return df13
    
def suffix(final_result):
    f_co_ord=[]
    for i in range(len(final_result)):
        w = final_result['Suffix_1_xy1'][i]
        w1 = final_result['Suffix_2_xy2'][i]
      
        if (len(w) >= 1) and (len(w1) >= 1):
            t=w[0].split(',')
            t1=w1[0].split(',')
            if (len(t) >= 4) and (len(t1) >= 4):
                co_ord = t[0] + '$'+ t[1] + '$'+ t1[2] + '$'+ t1[3]
                #print co_ord
                f_co_ord.append(co_ord)
            else:
                co_ord1 = ""
                f_co_ord.append(co_ord1)
        else:
            co_ord1 = ""
            f_co_ord.append(co_ord1)
    df13 = pd.DataFrame({"Suffix_x1y1x2y2": f_co_ord})
    return df13
    
