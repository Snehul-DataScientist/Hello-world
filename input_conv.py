import nltk
import pandas as pd
import datetime
import pandas.io.data as web
import string
import os
import time
import shutil

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

import nltk.data
from nltk import tokenize
import pdb
import glob
import nameparser
import nltk
import pathos
import timeit
from nameparser.parser import HumanName



from nltk.tokenize import sent_tokenize, word_tokenize


os.chdir('/home/ramakrishnabhat/Ram/Ancestery.com/46928 OCR - Berkshire Electoral Rolls- Sample images/input/OCR-16May2017/Output_Format_1')

'''
train_text = codecs.open("46928_553244-00002.j2k.00001.single.ecmdoc_formatted.txt", "rb", "utf-8", 'ignore').read()
train_text = train_text.replace('\r\n',' ')
train_text = train_text.replace('\t','')
train_text = re.sub(r'[^\x00-\x7F]','', train_text.encode('utf-8').strip())
train_text = ' '.join(train_text.split())

print (train_text)


import nltk
from nltk.corpus import state_union

from nltk.tokenize import PunktSentenceTokenizer


custom_sent_tokenizer = PunktSentenceTokenizer(train_text)


sample_text = """"\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\nABINGDON POLLING DISTRICT.\r\n15\r\n\r\nfjlAWaa OF JftreRteHAlel.\r\n\r\n\r\nCltrlaOan Nama ard Surname Select, Una, er other tike Place In ttilc ParlJ, for TawtHUnL\r\nand Nu .beref llouae I If any), where the i'roparty u eltuite\r\nof each PLACE 01 ABODE, NATUBS or QniXIFICATIOX. or Name of the Property, If known by any, or Name .,1 occu\r\nVoter at fail length. then prlnglenant; the Name, or If the4ualtncelt.,.ioou.i.t of a Kent -Cliai .\r\nof the Owner, of Ike l*rn|.erty our lehicfc\r\n.1\r\nauch Item i. leeutng, or eoiuo of thcia, and iho Me iolau o.\r\nthe\r\nPioperty,\r\nJOG Angell, Robert Marcham\r\nFreehold bouse & smith's Self and\r\n367 Ayers. Thomas Marcham shop others\r\nFreehold houses and gardens. Bolion Hammans and others\r\n3'.i Can.pion, Chamberlain Abingdon\r\nFreehold collages and laud . Legg and others\r\n.169 Dutfiold. Charles Philip Marcham\r\nFreehold land Marcham, Wm. Powell\r\n370 Ecley. James Mm chain\r\nOccupier of mill and land\r\n371\r\nFranklin. John 23\r\nManning street, Edgewaro Freehold cottage and garden . Harriet Franklin\r\nroad, London\r\nGodfrey, William . . Marcham Freehold houses Self and others\r\n372\r\n373 Hull, George Tnhncy warren Two freehold collages North Marcham\r\nstreet.\r\n374 Maxted, John Edward Marcham , .\r\nOccupier of maltlumsp and land Marcham\r\n375 Morland, Benjamin Shabbington, Bucks Freehold\r\nhouse and land Sheepstead house\r\n376 Payne, Edwin\r\nAbingdon Freehold mill and hind James Ecley, Marcham mill\r\n377 Powell. William, jun.\r\nMarcham\r\n\t Occupier of house and land In the village\r\n378 Randolph. Herbert Marcham\r\n(Clerk) \t Freehold house and land Vicarage and Thomas\r\n379 Simpson, Samuel Abingdon Two Ay res\r\n.. freehold cottages Gossnrd's ford, Marcham\r\n3S0 Simpson, Thomas Abingdon Freehold\r\ncottage Gossard's ford, Marcham\r\n"""




sample_text = re.sub(r'[^\x00-\x7F]','', sample_text.encode('utf-8').strip())
sample_text = re.sub(' +', ' ',sample_text)
sample_text = re.sub('\r\n', ' ',sample_text)
sample_text = re.sub('\n ', '\n',sample_text)
sample_text = sample_text.encode('utf-8')


print (sample_text)



def process_content(text):
    try:
        # tokenized = custom_sent_tokenizer.tokenize(text)
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            # chunkGram = r"""Chunk1: {<NNP.?>*<CD><NNP>+<NN>?}"""
            # chunkGram = r"""Chunk1: {<CD.?>*<NNP>?}"""
            chunkGram = r"""Chunk1: {<CD>+<NNP>+<NNP>}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            print (tagged)
            print (chunked)
            chunked.draw()

            for subtree in chunked.subtrees():
                print (subtree)
            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                print subtree

        return chunked

    except Exception as e:
        print (str(e))


Chunked = process_content(sample_text)

findNum = regex.search(r"(\n\w \d{1,4}|\n\d{1,4})",sample_text)

print (findNum)



tok_sen = nltk.tokenize.sent_tokenize(text)


print (tok_sen)


text = "This is for n-gram model"
n = 3

def ngram(text, n):
    gramlst = []
    text = text.split()
    for i in range (0, len(text)):
        text1 = text[i:n]
        i = i+1
        gramlst.append(text1)
    return gramlst, n


trigram  = ngram(text,3)
print (trigram)

'''

dt = datetime.datetime.now()
dt = dt.date()
dttime = time.strftime("%H:%M:%S")

TXT = '/home/ramakrishnabhat/Ram/Ancestery.com/Output/JETOUT/'+str(dt)+ str(dttime)+'/TXT'
JSON = '/home/ramakrishnabhat/Ram/Ancestery.com/46928 OCR - Berkshire Electoral Rolls- Sample images/input/OCR-16May2017/Output_Format_1/d_46928_553230/imput/JSON'
JPG = '/home/ramakrishnabhat/Ram/Ancestery.com/Output/JETOUT/'+str(dt)+ str(dttime)+'/JPG'
CSV1 = '/home/ramakrishnabhat/Ram/Ancestery.com/Output/JETOUT/'+str(dt)+ str(dttime)+'/CSV1'
CSV2 = '/home/ramakrishnabhat/Ram/Ancestery.com/Output/JETOUT/'+str(dt)+ str(dttime)+'/CSV2'
CSV3 = '/home/ramakrishnabhat/Ram/Ancestery.com/Output/JETOUT/'+str(dt)+ str(dttime)+'/CSV3'
temp_JSON = '/home/ramakrishnabhat/Ram/Ancestery.com/Output/JETOUT/'+str(dt)+ str(dttime)+'/temp_JSON'
Archive = '/home/ramakrishnabhat/Ram/Ancestery.com/Output/JETOUT/'+str(dt)+ str(dttime)+'/Archive'
Output = '/home/ramakrishnabhat/Ram/Ancestery.com/Output/'+str(dt)+ str(dttime)+'/Output'
    

jsonfiles = []
txtfiles = []
jpgfiles = []

in_dir_path = "/home/ramakrishnabhat/Ram/Ancestery.com/46928 OCR - Berkshire Electoral Rolls- Sample images/input/OCR-16May2017/Output_Format_1/d_46928_553454/"
# out_dir_path = "/home/ramakrishnabhat/Ram/Ancestery.com/46928 OCR - Berkshire Electoral Rolls- Sample images/input/OCR-16May2017/Output_Format_1/d_46928_553452/input/"

for path, subdirs, files in os.walk(in_dir_path):
    # for name in [f for f in files if f.lower().endswith("_fr.json")]:
    for name in [f for f in files if f.lower().endswith("_fr_orgimage.json")]:
        jsonfiles.append(path +'/'+name)
        print (jsonfiles)
    for name in [f for f in files if f.lower().endswith("_fr_formatted.txt")]:
        txtfiles.append(path +'/'+name)
        print (txtfiles)
    for name in [f for f in files if f.lower().endswith("jpg")]:
        jpgfiles.append(path +'/'+name)
        print (jpgfiles)
    for i in jsonfiles:
        if jsonfiles != []:
            batch = os.path.basename(i).split('_FR')[0]
            path = in_dir_path +"/"+batch
            if not os.path.exists(path):
                os.makedirs(in_dir_path +"/"+batch)
            shutil.copy(i,in_dir_path +"/"+batch)
    for i in txtfiles:
        if txtfiles != []:
            batch = os.path.basename(i).split('_FR')[0]
            path = in_dir_path + batch
            if not os.path.exists(path):
                os.makedirs(in_dir_path +batch)
            shutil.copy(i,in_dir_path + batch)
    for i in jpgfiles:
        if jpgfiles != []:
            batch = os.path.basename(i).split('.jpg')[0]
            path = in_dir_path + batch
            if not os.path.exists(path):
                os.makedirs(in_dir_path +batch)
            shutil.copy(i,in_dir_path + batch)
            
    
    
# for name in [f for f in files if f.lower().endswith("_fr.json")]:
#     jsonfiles.append(path +'/'+name)
#     for i in jsonfiles:
#         if jsonfiles != []:                    
#             if not os.path.exists(JSON):
#                 os.makedirs(JSON)       
#             shutil.copy(i,JSON)
#             jsonfiles = []
# for name in [f for f in files if f.lower().endswith(".jpg")]:
#     jpgfiles.append(path +'/'+name)
#     for i in jpgfiles:
#         if jpgfiles != []:
#             if not os.path.exists(JPG):
#                 os.makedirs(JPG)       
#             shutil.copy(i,JPG)
#             jpgfiles = []

#         for name in [f for f in files if f.lower().endswith("_fr_formatted.txt")]:
#             txtfiles.append(path +'/'+name)
#             for i in txtfiles:
#                 if txtfiles != []:
#                     if not os.path.exists(TXT):
#                         os.makedirs(TXT)       
#                     shutil.copy(i,TXT)
#                     txtfiles = []

#         for name in [f for f in files if f.endswith(".xls")]:
#             BatchNamelist = []
#             Layoutlist = []
#             # print name
#             if name != []:
#                 readExcel = pd.ExcelFile(in_dir_path + name)
#                 sheetName= readExcel.sheet_names[0]
#                 df = readExcel.parse(sheetName)
#                 for index, row in df.iterrows():
#                     BatchNamelist.append(str(row['Batch Name'].split('d_')[1].strip()))
#                     Layoutlist.append(str(row['Type of Layout'].split('Format')[1].strip()))
#                 dictionary1 = dict(zip(BatchNamelist,Layoutlist))
    
    
    # print(txtfiles)        

# if not os.path.exists(CSV1):
#     os.makedirs(CSV1)       
# if not os.path.exists(CSV2):
#     os.makedirs(CSV2)       
# if not os.path.exists(CSV3):
#     os.makedirs(CSV3)       
# if not os.path.exists(temp_JSON):
#     os.makedirs(temp_JSON)


# if not os.path.exists(Archive):
#     os.makedirs(Archive)
# if not os.path.exists(Output):
#     os.makedirs(Output)       

# TXT = TXT+"/"
# CSV1 = CSV1+"/"
# CSV2 = CSV2+"/"
# CSV3 = CSV3+"/"
# temp_JSON = temp_JSON+"/"
# Archive = Archive+"/"
# Output = Output+"/"
