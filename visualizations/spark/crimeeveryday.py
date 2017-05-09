from __future__ import print_function
from pyspark import SparkContext
from csv import reader
import datetime
import sys
if __name__ == "__main__":
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x: reader(x)).map(lambda x:('%s/%s/%s'%(x[1].split('/')[1],x[1].split('/')[0],x[1].split('/')[2]),1)).reduceByKey(lambda x, y: x+y).sortBy(lambda x: datetime.datetime.strptime(x[0], '%d/%m/%Y'))
    lines.saveAsTextFile('crimeeveryday.out')