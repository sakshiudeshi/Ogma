import csv
import matplotlib.pyplot as plt
X1 = []
Y1 = []

X2 = []
Y2 = []

f1 = open("DataFiles/ErrorDataRandom2018-10-12 16:42:03.178864.csv", 'r')
file_reader1 = csv.reader(f1, delimiter=',')

f2 = open("DataFiles/ErrorDataJaccard2018-10-12 15:28:14.782307.csv", 'r')
file_reader2 = csv.reader(f2, delimiter=',')

for line in file_reader1:
    # print line
    X1.append(int(line[4]))
    Y1.append(int(line[5]))

for line in file_reader2:
    X2.append(int(line[4]))
    Y2.append(int(line[5]))

fig = plt.figure()
plt.plot(X1, Y1, linestyle='--', label='random')
plt.plot(X2, Y2, linestyle='-.', label='directed')
plt.legend(loc='upper left')
fig.suptitle('Combined Errors in uClassify and Rosette (Jaccard Index < 0.3)')
plt.xlabel('Number of Inputs Generated')
plt.ylabel('Number of Errors')
fig.savefig('DataFiles/CombinedFalseStartErrors-1000iters')
plt.show()
