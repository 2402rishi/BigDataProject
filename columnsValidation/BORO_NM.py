from __future__ import print_function
from pyspark import SparkContext
from csv import reader
import sys
import re
def validity(x):
    if x is "" or x is " ":
        return "","NULL","OTHER","NULL"
    else:
        list_of_boroughs=['BRONX',"BROOKLYN","MANHATTAN","QUEENS","STATEN ISLAND"]
        if x not in list_of_boroughs:
            return x,"TEXT","Borough Name","INVALID"
        else :
            return x,"TEXT","Borough Name","VALID"
if __name__ == "__main__":
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    header = lines.take(1) #extract header
    lines = lines.filter(lambda x : x!= header)
    lines = lines.mapPartitions(lambda x: reader(x)).map(lambda x: '%s\t%s\t%s\t%s'%(validity(x[13])))
    lines.saveAsTextFile('BORO_NM.out')