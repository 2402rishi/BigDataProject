#!/usr/bin/env python

from pylab import *
import sys
import string
import numpy as np
import sys
import matplotlib.pyplot as plt
import re
from operator import add

file = open("TimeinBrooklyn.out", "r") 

x_axis = []
y_axis = []
year_crime_mapping = {}


for line in file:
	line = line.strip()
	a, y = line.split('\t', 1)
	b = a.split(':')
	if (len(b) == 3 and b[0].isdigit):
		x = int(b[0])
		if x == 24:
			x=0
		if x >=0 and x <=24 :
			if x in year_crime_mapping:
				count = year_crime_mapping[x]
				year_crime_mapping[x] = int(count) + int(y)
			else:
				year_crime_mapping[x] = y


year_crime = sorted(year_crime_mapping)
dict = {}
for k in year_crime:
    dict[k] = year_crime_mapping[k]		
print dict	
# x axis values
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
LABELS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y_axis = dict.values()

 
# plotting the points 
plt.plot(LABELS, y_axis, color='green', linestyle='dashed', linewidth = 5,
         marker='o', markerfacecolor='blue', markersize=15)
plt.xticks(x, LABELS, rotation='vertical')
 
# setting x and y axis range
plt.ylim(10000,70000)
plt.xlim(-1, 24)
 
# naming the x axis
plt.xlabel('time of crime in BROOKLYN overall')
# naming the y axis
plt.ylabel('Number of Crimes')
 
# giving a title to my graph
plt.title('Crime Scatter Plot for NYC')
 
# function to show the plot
plt.show()
