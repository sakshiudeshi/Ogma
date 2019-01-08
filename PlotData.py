import csv
import matplotlib.pyplot as plt
import datetime
from dateutil import parser
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
for folder_type in glob.glob('*'):
    src = folder_src + folder_type + "/"
# src = "DataFiles/MasterData/"+ folder_type + "/"
    X1 = []
    Y1 = []

    X2 = []
    Y2 = []

    jacc_thresh_val = str(folder_type)
    os.chdir(base_src)
    os.chdir(src)

    for f in glob.glob('*'):
        print f

    for f in glob.glob('ErrorDataRandom*.csv'):
        # print f
        f1 = open(f, 'r')
        file_reader1 = csv.reader(f1, delimiter=',')
        for line in file_reader1:
            # print line
            # X1.append(parser.parse(line[6]))
            X1.append(int(line[4]))
            Y1.append(int(line[5]))


    for f in glob.glob('ErrorDataDirected*.csv') or glob.glob('ErrorDataJaccard*.csv'):
        f2 = open(f, 'r')
        file_reader2 = csv.reader(f2, delimiter=',')
        for line in file_reader2:
            # X2.append(parser.parse(line[6]))
            X2.append(int(line[4]))
            Y2.append(int(line[5]))





    plt.clf()
    fig = plt.figure()
    plt.plot(X1, Y1, linestyle='--', label='random')
    plt.plot(X2, Y2, linestyle='-.', label='directed')
    plt.legend(loc='upper left')
    fig.suptitle('Combined Errors in ' + folder_type + ' (Jaccard Index < ' + jacc_thresh_val + ')')
    plt.xlabel('Total no of inputs')
    plt.ylabel('Number of Errors')
    fig.savefig(folder_type + '.png', dpi=250)
    plt.close()
