#!/usr/bin/env python

from pylab import *
import sys
import string
import numpy as np
import sys
import matplotlib.pyplot as plt
import re
from operator import add

file = open("DateinBrooklyn.out", "r") 

x_axis = []
y_axis = []
year_crime_mapping = {}


for line in file:
	line = line.strip()
	a, y = line.split('\t', 1)
	b = a.split('/')
	if (len(b) == 3 and b[2].isdigit):
		x = int(b[2])
	
		if x >= 2006 and x<2016:
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
x = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]
LABELS = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]

y_axis = dict.values()
print y_axis
 
# plotting the points 
plt.plot(LABELS, y_axis, color='green', linestyle='dashed', linewidth = 5,
         marker='o', markerfacecolor='blue', markersize=15)
plt.xticks(x, LABELS, rotation='vertical')
 
# setting x and y axis range
plt.ylim(0,150000)
plt.xlim(2005.5, 2015.5)
 
# naming the x axis
plt.xlabel('years from 2006 - 2015 in BROKKLYN')
# naming the y axis
plt.ylabel('Number of Crimes in BROKKLYN ')
 
# giving a title to my graph
plt.title('Crime Scatter Plot for NYC')
 
# function to show the plot
plt.show()
