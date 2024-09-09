from functools import partial
import matplotlib.pyplot as plt
import matplotlib
import sys
import pandas as pd
import numpy as np
print(sys.argv)
filename=sys.argv[1]
xAxis=sys.argv[2]
yAxis=sys.argv[3]
title=sys.argv[4]
print(filename)
df = pd.read_csv(filename)
graph = df.plot(x=xAxis,y=yAxis,marker="o",ls="-",legend=None,xticks=df[xAxis])
plt.xticks(fontsize=10)
plt.ylabel(yAxis)
plt.title(title)
plt.ticklabel_format(style="plain",axis="y")
if len(sys.argv)> 5:
    plt.xscale("log", base=2)
    plt.xticks(df[xAxis], df[xAxis], fontsize=8)
    plt.yscale("log", base=2)
    #yTicks = [0.25, 0.5, 1, 2, 4, 8,, 128, 256 16, 32]
    yTicks = [0.25, 0.5, 1, 2, 4, 8, 16]
    plt.yticks(yTicks, yTicks)
for i, y in enumerate(df[yAxis]):
    print(df[xAxis][i], df[yAxis][i])
    plt.annotate(round(df[yAxis][i], 3), (df[xAxis][i]*1, df[yAxis][i]* 0.85))
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
# fig, ax = plt.subplots()
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
# ax.spines['left'].set_visible(False)
graph.figure.savefig(filename + ".png")