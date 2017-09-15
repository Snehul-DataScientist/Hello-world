    # -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 10:32:55 2016

@author: Ram
"""
import re
import pandas as pd
import codecs
import os
from os.path import basename
import unicodedata
import numpy as np
import collections
import json
import argparse
from nltk.tag import pos_tag
import regex
from nltk.tree import Tree
from nltk.chunk import ne_chunk
from collections import Counter
from geotext import GeoText

#import nltk.data
from nltk import tokenize
import pdb
import glob
import nameparser
import nltk
import markovify
import pathos
import timeit
from nameparser.parser import HumanName


from multiprocessing import Pool

from os import listdir 
import csv

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')



def SentenceSplit(listeEle):
    sent_l = []
    ret_str = ""
    sent_list = tokenizer.tokenize(listeEle) #into sentence 
    return(sent_list)
    
def PreprocessingSent(list8):
    list4 =[]
    for j in range(0,len(list8)):
        list3 = SentenceSplit(list8[j])

        list4.append(list3)
    for i in range(0,len(list4)):
        list4[i] = "".join(list4[i])
        
    return(list4)


# getting records
def Recordwise(dev):
    address = []
    occupation = []
    surname = []
    given =  [] 
    prefix = []
    suffix = []
    raw = []
    Namelist = []
    s4list = []
    
    try:
        for i in range(0, len(dev)):
            #joining lines split 
            # print dev[i]
            findNum = regex.search(r"^(\d{3,4}){s<=1,i<=1,d<=1}", dev[i])
            findNum3 = regex.search(r"^(\d{3,4}){s<=1,i<=1,d<=1}", dev[i+1])
            if findNum is not None and findNum3 is not None:
                s4 = dev[i]            
                s4list.append(s4)
                # print (s4list)

            elif findNum is not None and dev[i+1] != '':
                #checks for number if not found adds that line
                s4 = (dev[i] + " "+ dev[i+1]).strip()
                # if two numbers come adjacent then add the previous line. line followed by number case
                xcv = regex.search(r"^(\d{1,4} \d{1,4}){s<=1,i<=1,d<=1}", s4)
                if xcv is not None:
                    s4 = dev[i] + " "+ dev[i-1].strip()
                    s4list.append(s4)
                    # print (s4list)
                else:
                    findNum1 = regex.search(r"^(\d{1,4}){s<=1,i<=1,d<=1}", s4)
                    if findNum1 is not None:
                        # check for the next line whether starts with number
                        findNum2 = regex.search(r"^(\d{1,4}){s<=1,i<=1,d<=1}", dev[i+2])#i+2 changed to i+1
                        if findNum2 is None:
                            #if the line does not start add that number
                            s4 = s4 + " "+ dev[i+2].strip()#i+2 changed to i+1
                            s4list.append(s4)
                            # print (s4list)
                        else:
                            s4list.append(s4)
                            # print (s4list)
            elif findNum is not None and dev[i+1] == '':
                s4 = dev[i]            
                s4list.append(s4)
                # print (s4list)
            
        s4list.append(s4)
        # print (s4list)

    except:
        s4list
            
    return(s4list)

#remove unwanted characters in beginning of records
def Remjunk(text):
    try:
        remjunk = regex.search(r"^(.*?)\d{1,4}", text)
        #regex updated for errors in key
        # remjunk = regex.search(r"(^(.*?)\d{3,4}){s<=1,i<=1,d<=1}", text)
        if remjunk != []:
            cleanText = text.replace(remjunk.group(1),'')
            return cleanText
        else:
            return text
    except:
        return text

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)



    



