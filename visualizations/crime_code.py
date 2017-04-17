#!/usr/bin/env python

from pylab import *
import sys
import string
import random
import randomcolor
import numpy as np
import sys
import matplotlib.pyplot as plt
import re
from operator import add

file = open("keycode.out", "r") 
year_crime_mapping = {}


for line in file:
	line = line.strip()
	a, y = line.split('\t', 1)
	if (a.isdigit):
			if a in year_crime_mapping:
				count = year_crime_mapping[a]
				year_crime_mapping[a] = int(count) + int(y)
			else:
				year_crime_mapping[a] = y


year_crime = sorted(year_crime_mapping)
dict = {}
for k in year_crime:
    dict[k] = year_crime_mapping[k]		
print dict	
# x axis values
x = list(dict.keys())
y = list(dict.values())
x_cor = []
y_cor = []
LABELS =[]
for i in range(0, len(x)):
	x_cor.append(i)
	LABELS.append(x[i])
for i in range(0, len(y)):
	y_cor.append(y[i])		

plt.plot(x_cor, y_cor, color='green', linestyle='dashed', linewidth = 5, marker='o', markerfacecolor='blue', markersize=15)
plt.xticks ( x_cor, LABELS, rotation = 'vertical')
 
# setting x and y axis range
plt.ylim(-10000,1100000)
plt.xlim(-1, 73)
 
# naming the x axis
plt.xlabel('Crime code')
# naming the y axis
plt.ylabel('Number of Crimes')
 
# giving a title to my graph
plt.title('Crime Scatter Plot for NYC')
 
# function to show the plot
plt.show()
