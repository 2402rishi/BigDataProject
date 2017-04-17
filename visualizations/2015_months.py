#!/usr/bin/env python

from pylab import *
import sys
import string
import numpy as np
import sys
import matplotlib.pyplot as plt
import re
from operator import add

file = open("Date.out", "r") 

x_axis = []
y_axis = []
year_crime_mapping = {}


for line in file:
	line = line.strip()
	a, y = line.split('\t', 1)
	b = a.split('/')
	if (len(b) == 3 and b[2].isdigit):
		x = int(b[0])
	
		if int(b[2]) == 2015:
			if x in year_crime_mapping:
				count = year_crime_mapping[x]
				year_crime_mapping[x] = int(count) + int(y)
			else:
				year_crime_mapping[x] = y


year_crime = sorted(year_crime_mapping)
print year_crime_mapping
dict = {}
for k in year_crime:
    dict[k] = year_crime_mapping[k]		
print dict	
# x axis values
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
LABELS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

y_axis = dict.values()
print y_axis
 
# plotting the points 
plt.plot(LABELS, y_axis, color='green', linestyle='dashed', linewidth = 5,
         marker='o', markerfacecolor='blue', markersize=15)
plt.xticks(x, LABELS, rotation='vertical')
 
# setting x and y axis range
plt.ylim(10000,55000)
plt.xlim(0, 13)
 
# naming the x axis
plt.xlabel('months of 2015')
# naming the y axis
plt.ylabel('Number of Crimes')
 
# giving a title to my graph
plt.title('Crime Scatter Plot for NYC')
 
# function to show the plot
plt.show()
