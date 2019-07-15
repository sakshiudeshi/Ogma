import csv
import os

base_src =  os.getcwd()
print base_src
path = "/Users/sakshiudeshi/Documents/SUTD/Research/Grammar ML/DataFiles/ErrorDataNoBacktrackDirected_Rosette_Aylien_GrammarA2019-06-17 13:07:47.723207.csv"
# path = base_src+file
path_new = "/Users/sakshiudeshi/Documents/SUTD/Research/Grammar ML/DataFiles/Fixed_ErrorDataNoBacktrackDirected_Rosette_Aylien_GrammarA2019-06-17 13:07:47.723207.csv"
f1 = open(path, 'r')
file_reader1 = csv.reader(f1, delimiter=',')

f = open(path_new, "w")
file_writer = csv.writer(f, delimiter=',')

count = 0
for line in file_reader1:
    if line[3] == "True":
        count += 1
        # print count
    line[5] = count
    print line
    file_writer.writerow(line)