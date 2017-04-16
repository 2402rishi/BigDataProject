from __future__ import print_function
from pyspark import SparkContext
from csv import reader
import sys
import re
def validity(x):
    if x is "" or x is " ":
        return "","NULL","OTHER","NULL"
    else:
        list_of_crimes=['FELONY',"MISDEMEANOR","VIOLATION"]
        if x not in list_of_crimes:
            return x,"TEXT","OFFENSE LEVEL","INVALID"
        else :
            return x,"TEXT","OFFENSE LEVEL","VALID"
if __name__ == "__main__":
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    header = lines.take(1) #extract header
    lines = lines.filter(lambda x : x!= header)
    lines = lines.mapPartitions(lambda x: reader(x)).map(lambda x: '%s\t%s\t%s\t%s'%(validity(x[11])))
    lines.saveAsTextFile('LAW_CAT_CD.out')