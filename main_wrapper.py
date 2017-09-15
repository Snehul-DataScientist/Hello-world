import os
import sys

clt_path = sys.argv[2] + "/" + "cltfiles/"
if not os.path.exists(clt_path):
	os.makedirs(clt_path)

batches = os.listdir(sys.argv[1])
for batch in batches:
	os.system('python Ances_wrapper.py ' + sys.argv[1]+ " " + sys.argv[2] + " " + batch)
	f = open(clt_path + batch+'.clt','wb+')
	f.write("")
	f.close()