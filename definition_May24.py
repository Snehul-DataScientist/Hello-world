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

import preprocess

from preprocess import *


from multiprocessing import Pool

from os import listdir 
import csv

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')



dwellbow = ["street.", "street,", "street", "St.", "lane", "road,", "road", "place,", "place.", "place", "..Abingdon", "Abingdon"]

#getting Voter names
def myName(text):
    fetchNameslist = []
    Given_Namelist = []
    Surnamelist = []
    Prefixlist = []
    Suffixlist = []

    try:
        for i in range (0, len(text)):
            '''
            places = GeoText(text[i])
            if places.cities != []:
                text[i] = text[i].split(places.cities[0])[0]
            '''
            # if places.countries != []:
            #     text[i] = text[i].split(places)[0]
            fetchName1 = regex.search(r"^(\d{1,4}(.*?)\t|\d{1,4}(.*?)\.|\d{1,4}(.*?) \d{1,4}|\d{1,4}(.*?)$)", text[i])
            try:
                if fetchName1 is not None:
                    fetchName = fetchName1.group(1)
                    fetchName = re.sub("\..", " ", fetchName)
                    for u in dwellbow:
                        if u in fetchName:
                            if u != 'Abingdon':
                                fetchName2 = fetchName.split(" ")
                                w = fetchName2.index(u)
                                try:
                                    fetchName = " ".join([x for x in fetchName2 if fetchName2.index(x) < w-1])
                                    
                                except:
                                    pass
                            else:
                                fetchName2 = fetchName.split(" ")
                                w = fetchName2.index(u)
                                try:
                                    fetchName = " ".join([x for x in fetchName2 if fetchName2.index(x) < w])
                                    
                                except:
                                    pass

                    xcv = regex.search(r"^(\d{1,4}){i<=1,d<=1}", fetchName)
                    if xcv is not None:
                        fetchName = fetchName.split(xcv[-1])[1]
                        fetchName
                        if '.' in fetchName:
                            fetchName = fetchName.split('.')[0]
                        fetchName = fetchName.strip()
                        #March 31 if numbers are present remove
                        if preprocess.hasNumbers(fetchName) == True:
                            fetchName = ''.join([i for i in fetchName if not i.isdigit()]).strip()
                        # fetchName = fetchName.split(' ')
                        fetchNameslist.append(fetchName)
                        try:
                            Given_Name = HumanName(fetchName).first.strip() +" "+HumanName(fetchName).middle.strip()
                            if Given_Name != '':
                                Given_Name = Given_Name.split(' ')[0] +" "+Given_Name.split(' ')[1]
                                Given_Namelist.append(Given_Name)
                            else:
                                Given_Name = " "
                                Given_Namelist.append(Given_Name)
                            Surname = HumanName(fetchName).last.strip()
                            if Surname != '':
                                Surnamelist.append(Surname)
                            else:
                                Surname = " "
                                Surnamelist.append(Surname)
                            Prefix = HumanName(fetchName).title.strip()
                            if Prefix != '':
                                Prefixlist.append(Prefix)
                            else:
                                Prefix = " "
                                Prefixlist.append(Prefix)
                            Suffix = HumanName(fetchName).suffix.strip()
                            if Suffix != '' and len(Suffix) < 5:
                                Suffixlist.append(Suffix)
                            else:
                                Suffix = " "
                                Suffixlist.append(Suffix)

                        except:
                            pass


                    else:
                        fetchName
                        try:
                            if '\t' in fetchName:
                                fetchName = fetchName.split('\t')[0]
                            else:
                                fetchName
                        except:
                            pass
                        fetchNameslist.append(fetchName)
                        try:
                            Given_Name = HumanName(fetchName).first.strip()
                            if Given_Name != '':
                                Given_Namelist.append(Given_Name)
                            else:
                                Given_Name = " "
                                Given_Namelist.append(Given_Name)
                            Surname = HumanName(fetchName).last.strip()
                            if Surname != '':
                                Surnamelist.append(Surname)
                            else:
                                Surname = " "
                                Surnamelist.append(Surname)
                            Prefix = HumanName(fetchName).title.strip()
                            if Prefix != '':
                                Prefixlist.append(Prefix)
                            else:
                                Prefix = " "
                                Prefixlist.append(Prefix)
                            Suffix = HumanName(fetchName).suffix.strip()
                            if Suffix != '':
                                Suffixlist.append(Suffix)
                            else:
                                Suffix = " "
                                Suffixlist.append(Suffix)

                        except:
                            pass

                else:
                    fetchName = " "
                    fetchNameslist.append(fetchName)
                    Given_Name = " "
                    Surname = " "
                    Prefix = " "
                    Suffix = " "
                    Given_Namelist.append(Given_Name)
                    Surnamelist.append(Surname)
                    Prefixlist.append(Prefix)
                    Suffixlist.append(Suffix)
            except:
                    fetchName = " "
                    fetchNameslist.append(fetchName)
                    Given_Name = " "
                    Surname = " "
                    Prefix = " "
                    Suffix = " "
                    Given_Namelist.append(Given_Name)
                    Surnamelist.append(Surname)
                    Prefixlist.append(Prefix)
                    Suffixlist.append(Suffix)
        return fetchNameslist, Given_Namelist, Surnamelist, Prefixlist, Suffixlist
    except:
        pass
        fetchName = " "
        fetchNameslist.append(fetchName)


subject = ["Freehold", "Leasehold", "Copyhold", "Dwelling", "Fret Sold", "Occupier", "Undivided", "Share"]

p_object1 = ["Houses", "Premises", "Workshops", "Buildings", "Lands", "Gardens", "Homes", 
            "Meadow Lands", "Mills", "Vicarages", "Glebes", "Tenements", "Summer Houses",
            "Benefices","Cottages", "Shops", "Glebe Lands", "Orchards", "Messuages",
            "Farm-buildings","Yards", "stables"]

counts = ["One", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
            "Fourteen", "Fifteen"]


#getting Occupation names

def occstart(text1):
    startlist = []
    startindlist = []
    
    
    for l in counts:
        # if l.lower() in text1.lower():
        #   xcv = regex.search(r"(?e)(^" + l +")"+ "{i<=1,s<=1}", text1)
          xcv = regex.search(r"(?e)(" + l +")", text1)
          try:
            if xcv is not None:
                xcv = xcv.group(0)
                # print xcv
                
                ind1 = text1.index(xcv)
                startlist.append(xcv)
                startlist = startlist[0]
                startindlist.append(ind1)
                startindlist = startindlist[0]
                # return startlist,startindlist

            else:
                xcv = " "
                ind1 = 0
            # return startlist,startindlist  
                
          except:
              pass
            # return startlist,startindlist
          
            
    
    for w in subject:
        # if w.lower() in text1.lower():
        #   cvb = regex.search(r"(?e)(^" + w +")"+ "{i<=1,s<=1}", text1)
          cvb = regex.search(r"(?e)(" + w +")", text1)
          try:
            if cvb is not None:
                cvb = cvb.group(0)
                # print cvb
                
                ind2 = text1.index(cvb)
                startlist.append(cvb)
                startlist = startlist[0]
                startindlist.append(ind2)
                startindlist = startindlist[0]
                
            else:
                cvb = " "
                ind2 = 0
    

          except:
              pass
    return startlist,startindlist

def occend(text1):
    endlist = []    
    endindlist = []
    sortendindlist = []

            
    for u in p_object1:
        # vbn = regex.search(r"(?e)(^" + u.lower() +")"+ "{i<=2,s<=2}", func(text1))
        vbn = regex.search(r"(?e)\b" + u.lower() +r"?\b", text1)
        # if u.lower() in text1.lower():
        try:
            if vbn is not None:
                vbn = vbn.group(0)
                # print vbn
                
                ind4 = text1.rfind(vbn)
                endlist.append(vbn)
                endindlist.append(ind4)

            else:
                vbn = " "
                ind4 = 0
                
        except:
            pass
    
    # return endlist,endindlist
        
    try:
        if len(endindlist) > 1:
            endindlist.sort()
            endlist = endlist[-1]
            endindlist = endindlist[-1] + len(endlist) 
            # print endlist,endindlist
            return endlist,endindlist
        else:
            endindlist = endindlist[-1] + len(endlist[-1]) 
            return endlist,endindlist
    
    except:
        endlist = " "
        endindlist = 0
        return endlist,endindlist


def occupant(text):
    occupantslist = []
    try:
        for i in range (0, len(text)):
            start,ind1 = occstart(text[i])
            end,ind2 = occend(text[i])
            if ind1 and ind2 is not None:
                occupants = text[i][ind1:ind2]
                occupantslist.append(occupants)
            else:
                occupants = " "
                occupantslist.append(occupants)


        return occupantslist

    except:
        pass

# getting addresslist

def address(text1,text2,text4,text5,text3):
    addTextlist = []
    Snolist = []
    POAlist = []
    try:
        for i in range (0, len(text1)):
            try:
                text1[i] = text1[i].replace(')','')
                text1[i] = text1[i].replace('(','')
                text1[i] = text1[i].replace(':','')
                text1[i] = text1[i].replace('\\','')
                text1[i] = text1[i].replace('-','')
                text1[i] = text1[i].replace('*','')
                text1[i] = text1[i].replace('?','')
                text1[i] = text1[i].replace('[','')
                text1[i] = text1[i].replace(']','')
                #Place of Abode from column 2 April 10
                findPOA = regex.search(str(text2[i])+r"(.*?)"+str(text3[i]), text1[i])
                if findPOA is not None:
                    POA = findPOA.group(1).strip()
                    address1 = regex.sub('\.','',POA).strip()
                else:
                    POA = " "
                    address1 = " "
                    
                abc = regex.sub(text2[i],' ', text1[i])
                abc = regex.sub(text4[i],' ', abc)
                abc = regex.sub(text5[i],' ', abc)
                xcv = regex.sub(text3[i],' ', abc.strip())
            except:
                POA = " "
                address1 = " "
                abc = " "
                xcv = " "
            findNum = regex.search(r"(\d{1,4}(.*?)\,){i<=1,d<=1}",xcv.strip())
            if findNum is not None:
                Sno = findNum.group(1).strip()
            else:
                Sno = " "
            addText = regex.sub(Sno," ", xcv.strip())
            #Data cleaning on March 29
            addText = regex.sub('\.','',addText)
            addText = regex.sub(address1,'',addText)
            #Takes Data up to 199 characters
            addText = addText[0:199].strip()
            addTextlist.append(addText)
            Sno = Sno.replace(',','')
            Sno = Sno.strip()
            Snolist.append(Sno)
            POAlist.append(address1) 
        return POAlist, addTextlist,Snolist
    except:
        text1 = " "
        Sno = " "
        address1 = " "
        addTextlist.append(text1)
        Snolist.append(Sno) 
        POAlist.append(address1)
