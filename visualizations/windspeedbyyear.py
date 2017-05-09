from __future__ import print_function
from pyspark import SparkContext
from csv import reader
import datetime
import sys
def convert_to_year(x):
	x=x.strip()
	year=x[0:4]
	return year
def convert_to_month(x):
	x=x.strip()
	month=x[4:6]
	return month
def convert_to_day(x):
	x=x.strip()
	day=x[6:8]
	return day
def windspeed(x):
	if float(x)== 999.9:
		return 0
	else:
		return x
if __name__ == "__main__":
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    lines = lines.mapPartitions(lambda x: reader(x)).map(lambda x:('%s-%s-%s'%(convert_to_day(x[2]),convert_to_month(x[2]),convert_to_year(x[2])),windspeed(x[16]))).reduceByKey(lambda x, y: (float(x)+float(y))/2).sortBy(lambda x: datetime.datetime.strptime(x[0], '%d-%m-%Y'))
    lines.saveAsTextFile('weather.out')