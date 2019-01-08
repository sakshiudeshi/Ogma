import csv
import matplotlib.pyplot as plt
import datetime
from dateutil import parser
import subprocess
X1 = []
Y1 = []

X2 = []
Y2 = []

import glob
import os
import jacc_thresh

# folder_type = "Rosette uClassify Grammar F"
base_src =  os.getcwd()
folder_src = "DataFiles/Master Data Jaccard Threshold Variation/"
os.chdir(folder_src)
# print jacc_thresh.dict_jacc[]
print glob.glob("*")
s =  glob.glob('*')
for folder_type in sorted(s):
    os.chdir(folder_type)


    for f in glob.glob('ErrorDataDirected*.csv'):
        last_line = subprocess.check_output(["tail", "-1", f])
        print folder_type
        print "Directed"
        print last_line.split(',')[-3:-1]

    for f in glob.glob('ErrorDataRandom*.csv') or glob.glob('ErrorDataJaccard*.csv'):
        last_line = subprocess.check_output(["tail", "-1", f])
        # print folder_type
        print "Random"
        print last_line.split(',')[-3:-1]
        print

    os.chdir(base_src)
    os.chdir(folder_src)
