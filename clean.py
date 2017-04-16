from __future__ import print_function
from pyspark import SparkContext
from csv import reader
import sys
import re
import datetime
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
def validity_complaint_number(x):
	if x is "" or x is " ":
		return False
	elif re.match('[1-9][0-9]+$',x):
		return True
	else :
		return False
def validity_date_event(x):
	if x is "" or x is " ":
		return False
	else :
            y=x
            x=x.split("/")
            try:
                year=int(x[2])
                month=int(x[0])
                day= int(x[1])
                if year >=2006 and year <=2016 :
                    try:  
                        newDate= datetime.datetime(year,month,day)
                        return True
                    except :
                        return False
                else :
                    return False
            except:
                return False
def validity_reported_time(x):
    if x is "" or x is " ":
        return False
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
                        return True
                except :
                        return False
            except:
                return False
#4 is same as date_event
#5 is same as reported time
#6 is same as date event
def validity_key_code(x):
	if x is "" or x is " ":
		return False
	elif re.match('[0-9][0-9][0-9]$',x):
		return True
	else :
		return False
def validity_string(x):
    if x is "" or x is " ":
        return False
    else:
        return True
#9 is same as key code
#10 is same as string
def validity_crime_status(x):
    if x is "" or x is " ":
        return False
    else:
        attempt_list=['COMPLETED',"ATTEMPTED"]
        if x not in attempt_list:
            return False
        else :
            return True
def validity_offense_level(x):
    if x is "" or x is " ":
        return False
    else:
        list_of_crimes=['FELONY',"MISDEMEANOR","VIOLATION"]
        if x not in list_of_crimes:
            return False
        else :
            return True
#13 is same as string
def validity_borough(x):
    if x is "" or x is " ":
        return False
    else:
        list_of_boroughs=['BRONX',"BROOKLYN","MANHATTAN","QUEENS","STATEN ISLAND"]
        if x not in list_of_boroughs:
            return False
        else :
            return True
def validity_address(x):
    if x is "" or x is " ":
        return False
    elif re.match('[1-9][0-9]+$',x):
        return True
    else :
        return False
def validity_location(x):
    if x is "" or x is " ":
        return False
    else:
        Location=['FRONT OF','INSIDE','OPPOSITE OF','OUTSIDE','REAR OF']
        if x not in Location:
            return False
        else :
            return True
#17 is same as string
#18 is same as string
#19 is same as string
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

def check_location(x):
    if x== "" or x== " "or x=="\t":
        return False
    x=x.strip("'")
    x=x.replace("(","")
    x=x.replace(")","")
    lat,lon=x.split(",")
    lat=lat.strip()
    lon=lon.strip()
    try:
        lat=float(lat)
        lon=float(lon)
        if isInNYC(Point(lat,lon)) :
            return True
        else:
            return False
    except :
        return False

def checker(x):
	if validity_complaint_number(x[0]) and validity_date_event(x[1]) and validity_reported_time(x[2]) and validity_key_code(x[6]) and validity_string(x[7]) and validity_key_code(x[8]) and validity_string(x[9]) and validity_crime_status(x[10]) and validity_offense_level(x[11]) and validity_string(x[12]) and validity_borough(x[13]) and validity_address(x[14]) and validity_location(x[15]) and validity_string(x[16]) and check_location(x[23])  :
		return True 
	else :
		return False
def toCSVLine(data):
    for i in range(len(data)):
        if "," in str(data[i]) :
            data[i]='"'+data[i]+'"'
    return ','.join(d for d in data)
if __name__ == "__main__":
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    header = lines.take(1) #extract header
    lines = lines.filter(lambda x : x!= header)
    lines = lines.mapPartitions(lambda x: reader(x)).map(lambda x: (x,checker(x))).filter(lambda x: x[1]==True).map(lambda x: toCSVLine(x[0]))

    lines.saveAsTextFile('clean.csv')