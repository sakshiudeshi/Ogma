# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.ticker import MaxNLocator
# from collections import namedtuple
#
#
#
# values = [0.603, 0.639, 0.807, 0.854]
# tags = ("Non Error\nRandom", "Error\nRandom", "Non Error\nDirected", "Error\nDirected")
#
# y_pos = np.arange(len(tags))
#
# plt.bar(y_pos, values, align='center', alpha=0.5, color="black")
# plt.xticks(y_pos, tags)
# plt.ylabel('Error rates')
# plt.title('Types')
# plt.colors()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
import os

# data to plot
n_groups = 2

Grammar_type = "RQ3"

Error_rate_random = (0.603, 0.639)
Error_rate_dir = (0.807, 0.854)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 1

rects1 = plt.bar(index, Error_rate_dir, bar_width,
                 edgecolor='black',
                 alpha=opacity,
                 color='white',
                 hatch="//",
                 label='Directed')

rects2 = plt.bar(index + bar_width, Error_rate_random, bar_width,
                 edgecolor='black',
                 alpha=opacity,
                 color="white",
                 label='Random')

# fig = plt.figure()
os.chdir("/Users/sakshiudeshi/Documents/SUTD/Research/LaTeX/GMLFuzz/figs")
# plt.xlabel(Grammar_type)
plt.ylabel('Number of errors')
plt.title("Start Condition\nSensitivity")
# fig.suptitle()
plt.xticks(index + bar_width/2, ("Non Error\nStart", "Error Start"))
plt.legend()
# plt.show()
plt.savefig(Grammar_type + '.png', dpi=250, bbox_inches='tight')
# plt.show()