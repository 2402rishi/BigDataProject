#!/usr/bin/env python

from pylab import *
import sys
import string
import numpy as np
import sys
import matplotlib.pyplot as plt
import re
from operator import add

file1 = open("./Output/weather.out", "r")
file2 = open("./Output/crimeeveryday.out", "r") 

x1 = []
y1 = []
sum= []
i = 1

for line in file1:
	line = line.strip().replace("(","").replace(")","").replace("'","")
	date, temp = line.split(" ")
	temp = float(temp)
	x1.append(temp)
	sum.append(i)
	i = i+1

plt.plot(sum, x1, color='orange')
plt.ylim(-1,100)
plt.xlim(-100, 3700) 
plt.xlabel('each day')
plt.ylabel('each day Temp')
plt.title('Crime Scatter Plot for NYC')
plt.show()

	
for line in file2:
	line = line.strip().replace("(","").replace(")","").replace("'","")
	date, count = line.split(",")
	y1.append(count)

plt.plot(sum, y1, color='blue')
plt.ylim(-10,3000)
plt.xlim(-100, 3700) 
plt.xlabel('each day')
plt.ylabel('Number of Crimes')
plt.title('Crime Scatter Plot for NYC')
plt.show()	


print str(x1) + " " + str(y1)
