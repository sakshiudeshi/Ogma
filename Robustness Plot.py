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
folder = "MasterData"
folder_src = "DataFiles/" + folder + "/"
os.chdir(folder_src)
# print jacc_thresh.dict_jacc[]
# print glob.glob("*")
folder_types = ["uClassify Aylien Grammar E", "Rosette Aylien Grammar A"]
for folder_type in glob.glob("*"):
    src = folder_src + folder_type + "/"
# src = "DataFiles/MasterData/"+ folder_type + "/"
    X1 = []
    Y1 = []

    X2 = []
    Y2 = []

    jacc_thresh_val = str(jacc_thresh.dict_jacc[folder_type])
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
            Y1.append(int(line[3] == 'True') + 1)
            # Y1.append(int(line[5]))


    for f in glob.glob('ErrorDataDirected*.csv') or glob.glob('ErrorDataJaccard*.csv'):
        f2 = open(f, 'r')
        file_reader2 = csv.reader(f2, delimiter=',')
        for line in file_reader2:
            # X2.append(parser.parse(line[6]))
            Y2.append(int(line[3] == 'True') + 3)


    # print X1


    plt.clf()
    fig = plt.figure()
    # width = 1 / 1.5
    # y = range(1000)
    k = range(len(Y1))

    plt.step(range(len(Y1)), Y1, label='random')
    plt.step(range(len(Y2)), Y2, color="r", linestyle = "--", label='Ogma')
    plt.axis([130, 300, 0, 4.5], "equal")
    # plt.plot(X2, Y2, linestyle='-.', label='directed')
    plt.legend(loc='upper left')
    fig.suptitle('Errors in ' + folder_type + '\n (Jaccard Index < ' + jacc_thresh_val + ')')
    plt.xlabel('Iteration')
    plt.yticks([1, 2, 3, 4], ["False", "True", "False", "True"])
    plt.ylabel('Error State at given iteration')
    if folder == "MasterData Positive Start":
        os.chdir("/Users/sakshiudeshi/Documents/SUTD/Research/Grammar ML/figs/robustness-master-error-start")
    else:
        os.chdir("/Users/sakshiudeshi/Documents/SUTD/Research/Grammar ML/figs/robustness-master-non-error-start")

    fig.savefig(folder_type.replace(' ', '-') + '.png', dpi=250)
    plt.close()
