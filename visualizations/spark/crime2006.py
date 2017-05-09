from __future__ import print_function
from pyspark import SparkContext
from csv import reader
import datetime
import sys
if __name__ == "__main__":
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x: reader(x)).filter(lambda x:int(str(x[1]).split('/')[2])==2006).map(lambda x:(x[1].split('/')[0],1)).reduceByKey(lambda x,y: x+y).sortByKey(True)
    lines.saveAsTextFile('2006crimes.out')
    