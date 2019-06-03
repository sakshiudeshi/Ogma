import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 15})
import os
import GrammarErrorRates

# data to plot
n_groups = 3
dict_error_rate = GrammarErrorRates.dict_error_rates

grams = ["A", "B", "C", "D", "E", "F"]

for gram in grams:
    Grammar_type = "Grammar" + gram

    Error_rate_dir = (dict_error_rate[Grammar_type + "-RA-D"],
                      dict_error_rate[Grammar_type + "-UA-D"],
                      dict_error_rate[Grammar_type + "-RU-D"])

    Error_rate_random = (dict_error_rate[Grammar_type + "-RA-R"],
                         dict_error_rate[Grammar_type + "-UA-R"],
                         dict_error_rate[Grammar_type + "-RU-R"])

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
                     label='Ogma')

    rects2 = plt.bar(index + bar_width, Error_rate_random, bar_width,
                     edgecolor='black',
                     alpha=opacity,
                     color="white",
                     label='Random')

    # fig = plt.figure()
    os.chdir("/Users/sakshiudeshi/Documents/SUTD/Research/LaTeX/GMLFuzz/figs")
    plt.xlabel("Grammar " + gram + " Errors")
    plt.ylabel('Error rates')
    # plt.title("Grammar " + gram + " Errors")
    # fig.suptitle()
    plt.xticks(index + bar_width/2, ("R-A", "U-A", "R-U"))
    plt.legend()
    # plt.show()
    plt.savefig(Grammar_type + '.png', dpi=250, bbox_inches='tight')
    # plt.show()