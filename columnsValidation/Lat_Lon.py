    #!/usr/bin/python
from __future__ import print_function
from pyspark import SparkContext
from csv import reader
import sys
import math
import sys
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

Latmax=40.917577
Latmin=40.477399
Lonmin=-74.25909
Lonmax=-73.700009 
def isInNYC(point):
    if(point.x<Latmin or point.x>Latmax):
      return False
    if(point.y<Lonmin or point.y> Lonmax):
      return False
    return True

def check(x):
    if x== "" or x== " "or x=="\t":
        return "","NULL","OTHER","NULL"
    x=x.strip("'")
    x=x.replace("(","")
    x=x.replace(")","")
    lat,lon=x.split(",")
    lat=lat.strip()
    lon=lon.strip()
    lat=float(lat)
    lon=float(lon)
    if isInNYC(Point(lat,lon)) :
        return x,"TEXT/INT","Location","VALID"
    else:
        return x,"TEXT/INT","Location","INVALID"
    print (lat,lon)
if __name__ == "__main__":
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    header = lines.take(1) #extract header
    lines = lines.filter(lambda x : x!= header)
    lines = lines.mapPartitions(lambda x: reader(x)).map(lambda x: '%s\t%s\t%s\t%s'%(check(x[23])))
    lines.saveAsTextFile('Lat_Lon.out')

