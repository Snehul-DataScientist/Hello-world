#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 16:23:02 2017

@author: bhaktikhude
version 2
"""

import os
import sys 
import shutil
import pdb

#in_dir_path = "/home/bhaktikhude/Desktop/FetchFiles/SA/input"
#in_dir_path = sys.argv[1]
#op_dir_path = "/home/bhaktikhude/Desktop/FetchFiles/SA/submit"
#op_dir_path = sys.argv[2]


def file_fetch_rename(in_dir_path, op_dir_path):
    textFiles = []
    pdfFiles = []
    filenames = os.listdir(in_dir_path)
    for name in [fi for fi in filenames if fi.lower().endswith("pdf.multi.txt")]:
            textFiles.append(os.path.join(in_dir_path, name))
    for filename in textFiles:
        shutil.copy(filename, op_dir_path)
        shutil.move(os.path.join(op_dir_path,os.path.basename(filename)), os.path.join(op_dir_path,os.path.basename(filename).split(".")[0]+".txt"))
    for name in [fi for fi in filenames if fi.lower().endswith("pdf.multi.pdf")]:
            pdfFiles.append(os.path.join(in_dir_path, name))
    for filename in pdfFiles:
        shutil.copy(filename, op_dir_path)
        shutil.move(os.path.join(op_dir_path,os.path.basename(filename)), os.path.join(op_dir_path,os.path.basename(filename).split(".")[0]+".pdf")) 
    return
    
    
                
def copy_folder(ip_dir_path, op_dir_path):
    #pdb.set_trace()
    filenames = os.listdir(ip_dir_path)
    for filename in filenames:
        shutil.copy(os.path.join(ip_dir_path,filename), op_dir_path)
    #shutil.rmtree(ip_dir_path)
    return
