# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 15:33:14 2017

@author: snehalpatil
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
import pdb
import string


    
def extract(outputlist,in_dir_path_json,out_dir_path_json):
    # pdb.set_trace()
    for file in outputlist:
        path=in_dir_path_json+"/"+file
        result = pd.read_csv(path, dtype={'Filename': object},sep=',',keep_default_na=False)
        parser = argparse.ArgumentParser(description='Ancestory.com')
        final_struct=[]
        try:
            temp = { "Extracted_values":[],"documentname":result["FileName"][0], "DocType": "Content"}
            for i in range(len(result["Prefix"])):
                        temp1 = {"Sno":result["Sno"][i],"GivenName":result["GivenName"][i].translate(None, string.punctuation)[:50],"GivenName_x1y1x2y2":result["GivenName_x1y1x2y2"][i],"SurName":result["SurName"][i].translate(None, string.punctuation)[:50],
                                "SurName_x1y1x2y2":result["SurName_x1y1x2y2"][i],"Prefix":result["Prefix"][i],
                                "Prefix_x1y1x2y2":result["Prefix_x1y1x2y2"][i],"Suffix":result["Suffix"][i],
                                "Suffix_x1y1x2y2":result["Suffix_x1y1x2y2"][i],"Occupation":result["Occupation"][i],
                                "Occupation_x1y1x2y2":result["Occupation_x1y1x2y2"][i],"Address":result["Address"][i][:199],"Address_x1y1x2y2":result["Address_x1y1x2y2"][i]}
                        temp["Extracted_values"].append(temp1)
            final_struct.append(temp)
                        
            with codecs.open(os.path.join(out_dir_path_json+file+".json"),'w') as writer:
                try:
                    json.dump(final_struct, writer, indent=4, separators=(',', ': '))
                    print('output.json written in directory ')
                except UnicodeDecodeError:
                    print("unicode error raised")
                    json.dump(final_struct, writer, indent=4,
                            separators=(',', ': '), ensure_ascii=False)
        except:
            pass
    
    
    
