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
import sys
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

import preprocess
import definition

from preprocess import *
from definition import *


tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')


#Defining FInal Function

def finalFun(list2):
    list4 = preprocess.PreprocessingSent(list2) #Main doc_list sentence spliting
    s4list = list4    
    # s4list = preprocess.Recordwise(list4)
    Given_Namelist, Surnamelist, Prefixlist, Suffixlist, Sno =definition.myName(s4list)  
    # Gensent = bowgen(occupators)
    # Occupationlist = occupant(s4list,Gensent)
    Occupationlist =definition.occupant(s4list)
    Address1,Address2 = definition.address(s4list,Given_Namelist, Surnamelist, Prefixlist,Occupationlist)
    
    
    return Given_Namelist, Surnamelist, Prefixlist, Suffixlist, Occupationlist, Address1,Address2, Sno
        
import multiprocessing as mp

if __name__ == '__main__':  
#    path = "/home/ronakshah/Ram/SplitTest"
    # in_dir_path = "/home/ronakshah/Ram/Ancestery.com/46928 OCR - Berkshire Electoral Rolls- Sample images/input/OCR files/solve"
    # in_dir_path = "/home/ronakshah/Ram/Ancestery.com/46928 OCR - Berkshire Electoral Rolls- Sample images/input/OCR files/format-2"
    # in_dir_path = "/home/ronakshah/Ram/Ancestery.com/46928 OCR - Berkshire Electoral Rolls- Sample images/input/OCR-30Mar2017/Ancestry OCR Project 2nd delivery"

   
   # in_dir_path = "/home/ramakrishnabhat/Ram/Ancestery.com/46928/input/OCR-16May2017/solve1"
    # out_dir_path = "/home/ramakrishnabhat/Ram/Ancestery.com/46928/input/OCR-16May2017/output1/"
    # path = "/home/ronakshah/Ram/Ancestery.com/46928 OCR - Berkshire Electoral Rolls- Sample images/input/OCR files/input2/"
    
    

    #getting list of files
    in_dir_path = sys.argv[1]
    out_dir_path = sys.argv[2]

    txtfiles = []
    outputlist = []
    
    #getting list of files
    txtfiles = os.listdir(in_dir_path)
    
    # for path, subdirs, files in os.walk(in_dir_path):
    #     for name in [f for f in files if f.endswith("_formatted.txt")]:
    #     # for name in [f for f in files if f.endswith("_new.txt")]:
    #         txtfiles.append(path +'/'+name)
    
    for i in range (0, len(txtfiles)):
        output = os.path.basename(txtfiles[i])
        #print (output)
        outputlist.append(output)
    
    Fileprefixlist = []
    Filegivenlist = []
    Filenamelist = []
    Filesurnamelist = []
    Filesuffixlist = []
    Fileoccupationlist = []
    Fileaddresslist = []
    Filesnolist = []
    appended_data = []

        
    for output in txtfiles:
        # print output
        # pdb.set_trace()
        output1 = os.path.basename(output)
        # doc = codecs.open(path + output,"rb","utf-8",'ignore').read()
        doc = codecs.open(in_dir_path +"/"+ output,"rb","utf-8",'ignore').read()
        doc = re.sub(r'[^\x00-\x7F]','', doc.encode('utf-8').strip())
        doc = re.sub(' +', ' ',doc)
        doc = re.sub('\n ', '\n',doc)
        doc = doc.encode('utf-8')

        list1 = doc.splitlines()
        list2 = filter(None, list1)
        list2 = map(preprocess.Remjunk, list2)

        MetaData = ["Place", "Abode","Number", "Name", "Nature", "Qualification", "Description", "Qualifying", "Property", "Elector"]

        try:
            for i in range (0, len(list2)):
                wlist = []
                for w in MetaData:
                    if w.lower() in list2[i].lower():
                        wlist.append(w)
                        if len(wlist) > 3:
                            # print ("start from here")
                            # print (i)
                            docSplitIndex = doc.index(list2[i])
                            docSplit = doc[docSplitIndex:]
			    list1 = docSplit.splitlines()
			    list2 = filter(None, list1)
			    list2 = map(preprocess.Remjunk, list2)
        except:
            docSplit = doc[0:]

        # print docSplit

        '''
        # starting the document with relevant text searching for numbers or nos preceded by single alphabet
        try:
            # updates done on April 4 for Single digits also
            findNum = regex.search(r"(\n\w \d{1,4}|\n\d{1,4})",doc)
            if findNum != []:
                docSplitIndex = doc.index(findNum[0])
                docSplit = doc[docSplitIndex:]
        except:
            docSplit = doc[0:]
        '''

        
        

        Given_Name, Surname, Prefix, Suffix, Occupation, Address1,Address2, Sno = finalFun(list2) #function_call
        

        colnames= {'FileName':output1, 'GivenName':Given_Name, 'SurName' :Surname, 'Prefix' :Prefix, 'Suffix' :Suffix,\
                    'Occupation' : Occupation, 'Address': Address1, 'Address2': Address2, 'Sno': Sno}

        
        nameslist = ['FileName', 'Sno','GivenName','SurName', 'Prefix', 'Suffix', 'Occupation', 'Address', 'Address2']
        # colnames = collections.OrderedDict(colnames)
        print output1
        result = pd.DataFrame(colnames)
        
        import datetime
        dt = str(datetime.datetime.now())
        dt = dt.split(' ')[0]
            # print (result)
	result.to_csv(out_dir_path+dt+os.path.basename(output)+"_output.csv", encoding='utf-8', index=False, cols=nameslist)
                
