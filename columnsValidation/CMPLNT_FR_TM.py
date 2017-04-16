from __future__ import print_function
from pyspark import SparkContext
from csv import reader
import sys
import re
import datetime
def validity(x):
    if x is "" or x is " ":
        return "","NULL","OTHER","NULL"
    else :
            y=x
            x=x.split(":")
            try:
                hour=int(x[0])
                minutes=int(x[1])
                seconds= int(x[2])
                if hour == 24 and minutes== 0 and seconds == 0:
                    hour=0
                try:  
                        newTime= datetime.time(hour,minutes,seconds)
                        return y,"Time","Reported Time","VALID"
                except :
                        return y,"OTHER","OTHER","INVALID"
            except:
                return y,"OTHER","OTHER","INVALID"
if __name__ == "__main__":
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    header = lines.take(1) #extract header
    lines = lines.filter(lambda x : x!= header)
    lines = lines.mapPartitions(lambda x: reader(x)).map(lambda x: '%s\t%s\t%s\t%s'%(validity(x[2])))
    lines.saveAsTextFile('CMPLNT_FR_TM.out')