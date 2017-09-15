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
import string

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
    Snolist = []

    
    for i in range (0, len(text)):
        try:    
            # sentt = text[i].translate(None, string.punctuation)
            # pdb.set_trace()
            # print sentt
            words = nltk.word_tokenize(text[i])
            tagged = nltk.pos_tag(words[:5])
            chunkGram = r"""Chunk: {<CD.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            # chunked.draw()
            leaflst = []
            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                # print(subtree)
                for leaf in subtree.leaves():
                    leaflst.append(leaf[0])
                    # print (leaflst)
                    leafcount = any(char.isdigit() for char in leaflst)
                    # pdb.set_trace()
                    if leafcount == True:
                        if len(leaflst) == 3:
                            break
                    else:
                        if len(leaflst) == 2:
                            break
                    
            fetchName = " ".join(leaflst)
            
            anyNum = regex.search(r"\d{1,5}", fetchName)
            try:
                if anyNum is not None:
                    Sno = anyNum[0]
                    Snolist.append(Sno)
                else:
                    Sno = " "
                    Snolist.append(Sno)
            except:
                Sno = " "
            fetchNames = regex.sub(Sno,' ', fetchName.strip())
            try:
                Given_Name = HumanName(fetchNames.strip()).first.strip() +" "+HumanName(fetchNames.strip()).middle.strip()
                if Given_Name != '':
                    Given_Name = Given_Name.split(' ')[0] +" "+Given_Name.split(' ')[1]
                    Given_Namelist.append(Given_Name.strip())
                else:
                    Given_Name = " "
                    Given_Namelist.append(Given_Name)
                Surname = HumanName(fetchNames.strip()).last.strip()
                if Surname != '':
                    Surnamelist.append(Surname)
                else:
                    Surname = " "
                    Surnamelist.append(Surname)
                Prefix = HumanName(fetchNames.strip()).title.strip()
                if Prefix != '':
                    Prefixlist.append(Prefix)
                else:
                    Prefix = " "
                    Prefixlist.append(Prefix)
                Suffix = HumanName(fetchNames.strip()).suffix.strip()
                if Suffix != '' and len(Suffix) < 5:
                    Suffixlist.append(Suffix)
                else:
                    Suffix = " "
                    Suffixlist.append(Suffix)
            except:
                pass
            

            

        except:
            fetchNames = " "
            fetchNameslist.append(fetchNames)
            Given_Name = " "
            Surname = " "
            Prefix = " "
            Suffix = " "
            Given_Namelist.append(Given_Name)
            Surnamelist.append(Surname)
            Prefixlist.append(Prefix)
            Suffixlist.append(Suffix)
            Snolist.append(Sno)


    # print (fetchNameslist)
    # print (Snolist)
        
    # return fetchNameslist, Given_Namelist, Surnamelist, Prefixlist, Suffixlist, Snolist    
    return Given_Namelist, Surnamelist, Prefixlist, Suffixlist, Snolist
    
    

    
    
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
          cvb = regex.search(r"(?e)(" + w +")"+ "{d<=1,i<=1,s<=1}", text1)
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
    

            if subject.index(w)  == len(subject) - 1 and ind2 == 0:
                # print "look for object"
                for u in p_object1:
                    vbn = regex.search(r"(?e)\b" + u.lower() +r"?\b"+ "{d<=1,i<=1,s<=1}", text1)
                    if vbn is not None:
                        vbn = vbn.group(0)
                        ind2 = text1.index(vbn)
                        startlist.append(vbn)
                        startlist = startlist[0]
                        startindlist.append(ind2)
                        startindlist = startindlist[0]



          
          except:
              pass
    return startlist,startindlist

def occend(text1):
    endlist = []    
    endindlist = []
    sortendindlist = []

            
    for u in p_object1:
        # vbn = regex.search(r"(?e)(^" + u.lower() +")"+ "{i<=2,s<=2}", func(text1))
        
        #updates as on May 30 searching from half of text 
        # vbn = regex.search(r"(?e)" + "(" +u.lower()+ ")" +r""+ "{d<=1,i<=1,s<=1}", text1[len(text1)/2:])
        
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

        # if p_object1.index(w)  == len(p_object1) - 1 and ind4 == 0:
        #         # print "look for subject"
        #         for u in subject:
        #             vbn = regex.search(r"(?e)\b" + u.lower() +r"?\b", text1)
        #             if vbn is not None:
        #                 vbn = vbn.group(0)
        #                 ind4 = text1.index(vbn)
        #                 endlist.append(vbn)
        #                 endlist = endlist[0]
        #                 endindlist.append(ind4)
        #                 endindlist = endindlist[0]
    
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
            if ind1 != 0 and ind2 != 0:
                occupants = text[i][ind1:ind2]
                occupantslist.append(occupants)
            elif start == end[0]:
                occupants = text[i][ind1:ind2]
                occupantslist.append(occupants)
            elif ind1 != [] and ind2 == 0:
                if start.startswith('Dw') and start.endswith('ng'):
                    # mistext = start +" "+"house"
                    # mistext = start
                    occupants = start
                    occupantslist.append(occupants)
                else:
                    occupants = start
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
                # print text1[i]
                # str1= text1[i]
                # text1[i] = text1[i].replace(')','')
                # text1[i] = text1[i].replace('(','')
                # text1[i] = text1[i].replace(':','')
                # text1[i] = text1[i].replace('\\','')
                # text1[i] = text1[i].replace('-','')
                # text1[i] = text1[i].replace('*','')
                # text1[i] = text1[i].replace('?','')
                # text1[i] = text1[i].replace('[','')
                # text1[i] = text1[i].replace(']','')

                # text1[i] = text1[i].replace(')','\)')
                # text1[i] = text1[i].replace('(','\(')
                # text1[i] = text1[i].replace(':','\:')
                # text1[i] = text1[i].replace('\\','\\\\')
                # text1[i] = text1[i].replace('-','\-')
                # text1[i] = text1[i].replace('*','\*')
                # text1[i] = text1[i].replace('?','\?')
                # text1[i] = text1[i].replace('[','\[')
                # text1[i] = text1[i].replace(']','\]')

                '''
                text2[i] = text2[i].replace('\\','\\\\')
                text2[i] = text2[i].replace(')','\)')
                text2[i] = text2[i].replace('(','\(')
                text2[i] = text2[i].replace(':','\:')
                text2[i] = text2[i].replace('-','\-')
                text2[i] = text2[i].replace('*','\*')
                text2[i] = text2[i].replace('?','\?')
                text2[i] = text2[i].replace('[','\[')
                text2[i] = text2[i].replace(']','\]')

                text3[i] = text3[i].replace('\\','\\\\')
                text3[i] = text3[i].replace(')','\)')
                text3[i] = text3[i].replace('(','\(')
                text3[i] = text3[i].replace(':','\:')
                text3[i] = text3[i].replace('-','\-')
                text3[i] = text3[i].replace('*','\*')
                text3[i] = text3[i].replace('?','\?')
                text3[i] = text3[i].replace('[','\[')
                text3[i] = text3[i].replace(']','\]')

                text4[i] = text4[i].replace('\\','\\\\')
                text4[i] = text4[i].replace(')','\)')
                text4[i] = text4[i].replace('(','\(')
                text4[i] = text4[i].replace(':','\:')
                text4[i] = text4[i].replace('-','\-')
                text4[i] = text4[i].replace('*','\*')
                text4[i] = text4[i].replace('?','\?')
                text4[i] = text4[i].replace('[','\[')
                text4[i] = text4[i].replace(']','\]')
                
                text5[i] = text5[i].replace('\\','\\\\')
                text5[i] = text5[i].replace(')','\)')
                text5[i] = text5[i].replace('(','\(')
                text5[i] = text5[i].replace(':','\:')
                text5[i] = text5[i].replace('-','\-')
                text5[i] = text5[i].replace('*','\*')
                text5[i] = text5[i].replace('?','\?')
                text5[i] = text5[i].replace('[','\[')
                text5[i] = text5[i].replace(']','\]')
                '''
                if text2[i] != ' ':
                    t2= re.escape(str(text2[i]).strip())
                else:
                    t2=""
                if text3[i] != ' ':
                    t3= re.escape(str(text3[i]).strip())
                else:
                    t3=""
                if text4[i] != ' ':
                    t4= re.escape(str(text4[i]).strip())
                else:
                    t4=""
                 # print text1[i]
                if text2[i] != " ":
                    abc = re.sub(t2,'', text1[i])
                else:
                    abc = re.sub(t2,'', text1[i])
                if text4[i] != ' ':
                    abc = re.sub(t4,'', abc)
                else:
                    abc = re.sub(t4,'', abc)
                #Place of Abode from column 2 April 10
                findPOA = re.search(t4+r"(.*?)"+t3, text1[i])
                # addtext1 = regex.search(str(text3[i])+r"(.*?)$", text1[i])
                if findPOA is not None:
                    POA = findPOA.group(1).strip()
                    
                    # POA = POA.replace('\\','\\\\')
                    # POA = POA.replace(')','\)')
                    # POA = POA.replace('(','\(')
                    # POA = POA.replace(':','\:')
                    # POA = POA.replace('-','\-')
                    # POA = POA.replace('*','\*')
                    # POA = POA.replace('?','\?')
                    # POA = POA.replace('[','\[')
                    # POA = POA.replace(']','\]')

                    # address1 = re.sub('\.','',POA).strip()
                    address1 = POA.strip()
                #updates for address missing May 30
                else:
                    POA = re.search(t3+r"(.*?)$", abc)
                    if POA is not None:
                        address1 = POA.group(1)
                    else:
                        POA = " "
                        address1 = " "
                    
                
                if text3[i] != ' ':
                    addtext1 = re.search(t3+r"(.*?)$", abc)
                    if addtext1 is not None:
                        addText = addtext1.group(1)
                    else:
                        addText = " "
                elif POA != ' ':
                    addtext1 = re.search(re.escape(POA)+r"(.*?)$", abc)
                    if addtext1 is not None:
                        addText = addtext1.group(1)
                    else:
                        addText = " "
                else:
                    addText = " "

                    
                # addText = regex.sub(address1,'',addText)
                #Takes Data up to 199 characters
                #addText = addText[0:199]
                #addTextlist.append(addText)


                # if text5[i] != '':
                #     abc = regex.sub(text5[i],' ', abc)
                # else:
                #     abc = regex.sub(text5[i],'', abc)
                # if text3[i] != '':
                #     xcv = regex.sub(text3[i],' ', abc.strip())
                # else:
                #     xcv = regex.sub(text3[i],'', abc.strip())
                
            # except:
            #     POA = " "
            #     address1 = " "
            #     abc = " "
            #     xcv = " "
            except:
                if POA == None:
                    POA = " "
                if address1 == None:
                    address1 = " "
                pass
            '''
            findNum = regex.search(r"(\d{1,4}(.*?)\,){i<=1,d<=1}",xcv.strip())
            if findNum is not None:
                Sno = findNum.group(1).strip()
            else:
                Sno = " "
            '''
            # addText = regex.sub(Sno," ", xcv.strip())
            #Data cleaning on March 29
            # addText = regex.sub('\.','',xcv.strip())

            # Sno = Sno.replace(',','')
            # Sno = Sno.strip()
            # Snolist.append(Sno)
            POAlist.append(address1) 
            addText = addText[0:199]
            addTextlist.append(addText)
        
    except:
        addTextlist.append(" ")
        POAlist.append(" ")
    # print addTextlist , POAlist
    return POAlist, addTextlist