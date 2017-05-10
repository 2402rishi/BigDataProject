#!/usr/bin/env python

from pylab import *
import sys
import string
import numpy as np
import sys
import matplotlib.pyplot as plt
import re
from operator import add



x1 = [ 47848, 44850, 66739, 54373, 70295]
y1 = [ 807718 , 1148607 ,715798 , 738977 ,196755]
points = [1,2,3,4,5]

	
	
LABELS = ["Bronx", "Brooklyn", "Manhattan", "Queens", "Staten Island"]
print str(x1) + "  " + str(y1) 
 

p1=plt.plot( points, x1, label = "Income", color='orange', linestyle='solid', linewidth = 3, marker='o', markersize=5)
p2=plt.plot( points, y1, label= "Crime",color='blue', linestyle='solid', linewidth = 3, marker='o',  markersize=5)
#plt.legend([p1, p2], ["line 2", "line 1"])
plt.legend(loc='best', numpoints=1, handlelength=0)
plt.xticks(points, LABELS)
plt.ylim(0,1210000)
plt.xlim(0.5, 5.5) 
plt.xlabel('Borroughs')
plt.ylabel('Number of Crimes and Income')
plt.title('Crime Scatter Plot for NYC')
plt.show()
