from __future__ import print_function
from pyspark import SparkContext
from datetime import datetime, timedelta
from csv import reader
import sys
def convert_to_date(x):
	x=x.strip()
	year=int(x[0:4])
	return year
def convert_to_month(x):
	x=x.strip()
	month=int(x[4:6])
	return month
def convert_to_day(x):
	x=x.strip()
	day=int(x[6:8])
	return day
if __name__ == "__main__":
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x:reader(x)).filter(lambda x: convert_to_date(x[2])==2012).map(lambda x:(convert_to_month(x[2]),x[3])).reduceByKey(lambda x,y: (float(x)+float(y))/2).sortByKey(True)
    lines.saveAsTextFile('2012weather.out')