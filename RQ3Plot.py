import numpy as np
import matplotlib.pyplot as plt
import os


opacity = 1
values = [0.629, 0.639, 0.821, 0.854]
tags = ("Non Error\nRandom", "Error\nRandom", "Non Error\nDirected", "Error\nDirected")

y_pos = np.arange(len(tags))

plt.bar(y_pos, values, align='center',edgecolor='black',
                 alpha=1,
                 color="white",)
plt.xticks(y_pos, tags)
plt.ylabel('Error Rates')
plt.title('Types')
os.chdir("/Users/sakshiudeshi/Documents/SUTD/Research/LaTeX/GMLFuzz/figs")
plt.savefig('RQ3.png', dpi=250, bbox_inches='tight')