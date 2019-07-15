import matplotlib.pyplot as plt
import os
import numpy as np
aves= []
arrs = [50, 100, 150, 200, 250] + [300, 350, 400, 450, 500]

arr_p = []
for i in arrs:
    arr_p.append(str(i*100/2000) + "%")

for n in arrs:
    with open('error_count_' + str(n) + '.txt') as f:
        lines = f.read().splitlines()
    nums = []
    for i in lines:
        nums.append(int(i))
    ave = reduce(lambda x, y: x + y, nums) / len(nums)
    print ave
    aves.append(ave)

index = np.arange(len(aves))
plt.clf()
fig = plt.figure()
plt.bar(index, aves)
plt.xticks(index, arr_p)
plt.ylabel("Errors")
os.chdir("/Users/sakshiudeshi/Documents/SUTD/Research/LaTeX/GMLFuzz/figs/")
fig.savefig('retraining.png', dpi=250)
# for i in arr_p:
#     print i

