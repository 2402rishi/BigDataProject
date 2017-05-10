#!/usr/bin/env python

from pylab import *
import sys
import string
import numpy as np
import sys
import matplotlib.pyplot as plt
import re
from operator import add

file1 = open("./Output/2015weather.out", "r")
file2 = open("./Output/2015crimes.out", "r") 

x1 = []
y1 = []


for line in file1:
	line = line.strip()
	date, temp = line.split(",")
	temp = float(temp) * 100
	x1.append(temp)

	
for line in file2:
	line = line.strip()
	date, count = line.split(",")
	y1.append(count)
	
	
LABELS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print str(x1) + "  " + str(y1) 
 

plt.plot(LABELS, x1, color='green', linestyle='solid', linewidth = 1)
plt.plot(LABELS, y1, color='blue', linestyle='solid', linewidth = 1)
plt.xticks(LABELS, LABELS, rotation='vertical')
 
# setting x and y axis range
#plt.ylim(0,5000)
#plt.xlim(0, 13)
 
plt.ylim(0,36000)
plt.xlim(0, 13) 
 
# naming the x axis
plt.xlabel('months of 2015')
# naming the y axis
plt.ylabel('Number of Crimes and Temp')
 
# giving a title to my graph
plt.title('Crime Scatter Plot for NYC')
 
# function to show the plot
plt.show()
