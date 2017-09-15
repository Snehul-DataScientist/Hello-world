import pandas as pd
import sys
import itertools
from xml.dom import minidom
import simplejson as json
import re
import os
import json
import csv
import pandas as pd
import pdb
from pprint import pprint
import pathos
from multiprocessing import Pool
import codecs
import simplejson
    
def extract_data(outputlist):
    for f in outputlist:
        path=f
        file1 = os.path.basename(f)

        #pdb.set_trace()

	########################################################
        #with codecs.open(path, "rb", encoding="utf-8") as json_file:
        #    data = simplejson.load(json_file)
	###########################################################

	
        with open(path) as json_file:
            temp=json_file.read().replace('\xef\xbb\xbf','')
            temp1 = json.dumps(temp)
            data1=json.loads(temp1)
            open(path,'wb+').write(data1.encode('utf8'))
            with codecs.open(path, "rb", encoding="utf-8") as json_file:
                data = simplejson.load(json_file)
            
        #     data = simplejson.load(json_file)
            rootbow = ['Engine', 'PageIndex', 'Blocks', 'Images', 'Height', 'Width', 'Words', 'Front']    
            for key,value in data.items():
                key1lst = []
                value1lst = []
                value2lst = []
                Heightlst = []
                Widthlst = []
                Xlst = []
                Ylst = []
                # print key,value
                for w in rootbow:
                    if w == 'Words':
                        wordslst = (value[0][w])
                        for i in wordslst:
                            for key1,value1 in i.items():
                                if key1 == 'Text':
                                    # key1lst.append(key1)
                                    if value1 != u'':
                                        value1lst.append(value1)
                            for key2,value2 in i.items():
                                 if key2 in ['Rect','rect']:
                                    # key1lst.append(key1)
                                    if value2 != u'':
                                        Heightlst.append(value2['Height'])
                                        Widthlst.append(value2['Width'])
                                        Xlst.append(value2['X'])
                                        Ylst.append(value2['Y'])
                                        value2lst.append(value2)
    
 
        colnames = {'txt1':value1lst, 'Height1':Heightlst, 'width1':Widthlst, 'x1':Xlst, 'y1': Ylst}
        # pdb.set_trace()
        nameslist = ['txt1', 'Height1', 'width1', 'x1', 'y1']
        # print (nameslist)
        result = pd.DataFrame(colnames)
        result.to_csv(out_dir_path+file1+"_output.csv", encoding='utf-8', index=False, cols=nameslist)


if __name__ == '__main__':

    # mypath = "/home/snehalpatil/Desktop"
    # in_dir_path = mypath + '/ANCESTORY/new_input/nfiles/'
    # out_dir_path = mypath + '/ANCESTORY/1.json_to_csv/output/'

    #mypath = "/home/ramakrishnabhat/Ram/"

    # in_dir_path = mypath + 'Ancestery.com/46928 OCR - Berkshire Electoral Rolls- Sample images/input/OCR-30Mar2017/Ancestry OCR Project 2nd delivery'
    # out_dir_path = mypath + 'output/April11/'

    in_dir_path = sys.argv[1]
    out_dir_path = sys.argv[2]

    jsonfiles = []
    outputlist = []


    #getting list of files

    for path, subdirs, files in os.walk(in_dir_path):
        for name in [f for f in files if f.lower().endswith("_fr_orgimage.json")]:
            jsonfiles.append(path+"/"+name)
    # print jsonfiles

    # for i in range (0, len(jsonfiles)):
    #     output = os.path.basename(jsonfiles[i])
    #     outputlist.append(output)

extract_data(jsonfiles)       
      

    
        
    
