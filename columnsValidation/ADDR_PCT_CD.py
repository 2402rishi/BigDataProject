from __future__ import print_function
from pyspark import SparkContext
from csv import reader
import sys
import re
def validity(x):
    if x is "" or x is " ":
        return "NULL"
    elif re.match('[1-9]+',x):
        return "VALID"
    else :
        return "INVALID"
def convert(x):
    try:
        return int(x),"INT","ADDRESS",validity(x)
    except:
        return "","NULL","OTHER","NULL"
if __name__ == "__main__":
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    header = lines.take(1) #extract header
    lines = lines.filter(lambda x : x!= header)
    lines = lines.mapPartitions(lambda x: reader(x)).map(lambda x: '%s\t%s\t%s\t%s'%(convert(x[14])))
    lines.saveAsTextFile('ADDR_PCT_CD.out')