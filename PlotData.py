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

folder_type = "uClassify Aylien Grammar F"
src = "DataFiles/MasterData/"+ folder_type + "/"

jacc_thresh = "0.1"

os.chdir(src)

for f in glob.glob('*'):
    print f

for f in glob.glob('ErrorDataRandom*.csv'):
    print f
    f1 = open(f, 'r')
    file_reader1 = csv.reader(f1, delimiter=',')
    for line in file_reader1:
        # print line
        # X1.append(parser.parse(line[6]))
        X1.append(int(line[4]))
        Y1.append(int(line[5]))


for f in glob.glob('ErrorDataDirected*.csv'):
    f2 = open(f, 'r')
    file_reader2 = csv.reader(f2, delimiter=',')
    for line in file_reader2:
        # X2.append(parser.parse(line[6]))
        X2.append(int(line[4]))
        Y2.append(int(line[5]))




# print type(X1[0])

# print X1[0]
fig = plt.figure()
plt.plot(X1, Y1, linestyle='--', label='random')
plt.plot(X2, Y2, linestyle='-.', label='directed')
plt.legend(loc='upper left')
fig.suptitle('Combined Errors in ' + folder_type + ' (Jaccard Index < '+ jacc_thresh +')')
plt.xlabel('Total no of inputs')
plt.ylabel('Number of Errors')
fig.savefig(folder_type + '.png', dpi=250)
# plt.show()
