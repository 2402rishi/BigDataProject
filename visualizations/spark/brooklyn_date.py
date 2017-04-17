
from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext
from csv import reader


if __name__ == "__main__":
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    rows = lines.mapPartitions(lambda x: reader(x))
	violation = rows.filter(lambda x : (str(x[13]) == "BROOKLYN"))
    violation_code = violation.map(lambda x: ((x[1]),1))
    violation_count = violation_code.reduceByKey(add)
	

    #convert Voilation_count to RDD and dictionary for formatting
    #result = sc.parallelize(Voilation_count)
    counts = violation_count.map(lambda x: str(x[0]).replace("'","").replace('(','').replace(')','') + '\t' + str(x[1]))

    counts.saveAsTextFile("DateinBrooklyn.out")

    sc.stop()

