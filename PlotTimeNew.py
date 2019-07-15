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
import numpy as np

from datetime import datetime
from datetime import timedelta

# folder_type = "Rosette uClassify Grammar F"
base_src =  os.getcwd()
folder = "MasterData"
folder_src = "DataFiles/" + folder + "/"
os.chdir(folder_src)
labels_timing = ['Random', 'Ogma', 'Ogma-No Backtrack']
# print jacc_thresh.dict_jacc[]
fmt = '%H:%M:%S.%f'
print glob.glob("*")
for folder_type in glob.glob('*'):
    src = folder_src + folder_type + "/"
# src = "DataFiles/MasterData/"+ folder_type + "/"
    X1 = []
    Y1 = []

    X2 = []
    Y2 = []


    X3 = []
    Y3 = []

    jacc_thresh_val = str(jacc_thresh.dict_jacc[folder_type])
    os.chdir(base_src)
    os.chdir(src)
    timing_info = []
    for f in glob.glob('*'):
        print f

    for f in glob.glob('ErrorDataRandom*.csv'):
        # print f
        f1 = open(f, 'r')
        file_reader1 = csv.reader(f1, delimiter=',')
        for line in file_reader1:
            # print line
            if int(line[5]) < 1:
                X1.append(parser.parse(line[6]))
            # X1.append(int(line[4]))
            # Y1.append(int(line[5]))
        print (X1[-1], X1[0])
        timing_info1 = (X1[-1] - X1[0])
        if (X1[-1] - X1[0]) < timedelta(0):
            timing_info1 += timedelta(days=1)
        print timing_info1
        timing_info.append(float(timing_info1.total_seconds()/60))

    for f in glob.glob('ErrorDataDirected*.csv') or glob.glob('ErrorDataJaccard*.csv'):
        f2 = open(f, 'r')
        file_reader2 = csv.reader(f2, delimiter=',')
        for line in file_reader2:
            if int(line[5]) < 1:
                X2.append(parser.parse(line[6]))
            # X2.append(int(line[4]))
            # Y2.append(int(line[5]))
        print (X2[-1], X2[0])
        timing_info2 = (X2[-1] - X2[0])
        if (X2[-1] - X2[0]) < timedelta(0):
            timing_info2 += timedelta(days=1)
        print timing_info2
        timing_info.append(float(timing_info2.total_seconds()/60))

    for f in glob.glob('ErrorDataNoBacktrackDirected*.csv'):
        f3 = open(f, 'r')
        file_reader3 = csv.reader(f3, delimiter=',')
        for line in file_reader3:
            if int(line[5]) < 1:
                X3.append(parser.parse(line[6]))
            # X3.append(int(line[4]))
            # Y3.append(int(line[5]))
        print (X3[-1], X3[0])
        timing_info3 = (X3[-1] - X3[0])
        if (X3[-1] - X3[0]) < timedelta(0):
            timing_info3 += timedelta(days=1)
        print timing_info3
        timing_info.append(float(timing_info3.total_seconds()/60))


    print timing_info

    print "---------"
    print folder_type
    print len(X1), len(X2),len(X3)
    print "---------"


    # plt.clf()
    # fig = plt.figure()
    # index = np.arange(len(labels_timing))
    # plt.bar(index, timing_info)
    # plt.legend(loc='upper left')
    # fig.suptitle('Time taken to generate 100 errors for\n' + folder_type + ' (Jaccard Index < ' + jacc_thresh_val + ')')
    # plt.xticks(index, labels_timing)
    # plt.ylabel('Time (Minutes)')
    # if folder == "MasterData Positive Start":
    #     os.chdir("/Users/sakshiudeshi/Documents/SUTD/Research/LaTeX/GMLFuzz/figs/master-error-start-time-new-100")
    # else:
    #     os.chdir("/Users/sakshiudeshi/Documents/SUTD/Research/LaTeX/GMLFuzz/figs/master-non-error-start-time-new-100")
    #
    # fig.savefig(folder_type.replace(' ', '-') + '.png', dpi=250)
    # # plt.close()
