hadoop fs -rm -r borough_name.out
hadoop fs -rm -r Date.out
hadoop fs -rm -r keycode.out
hadoop fs -rm -r prem_desc.out
hadoop fs -rm -r Time.out
hadoop fs -rm -r DateinBrooklyn.out
hadoop fs -rm -r KeysinBrooklyn.out
hadoop fs -rm -r TimeinBrooklyn.out
hadoop fs -rm -r crimeeveryday.out
hadoop fs -rm -r weather.out
hadoop fs -rm -r 2006crimes.out
hadoop fs -rm -r 2007crimes.out
hadoop fs -rm -r 2008crimes.out
hadoop fs -rm -r 2009crimes.out
hadoop fs -rm -r 2010crimes.out
hadoop fs -rm -r 2011crimes.out
hadoop fs -rm -r 2012crimes.out
hadoop fs -rm -r 2013crimes.out
hadoop fs -rm -r 2014crimes.out
hadoop fs -rm -r 2015crimes.out
hadoop fs -rm -r 2006weather.out
hadoop fs -rm -r 2007weather.out
hadoop fs -rm -r 2008weather.out
hadoop fs -rm -r 2009weather.out
hadoop fs -rm -r 2010weather.out
hadoop fs -rm -r 2011weather.out
hadoop fs -rm -r 2012weather.out
hadoop fs -rm -r 2013weather.out
hadoop fs -rm -r 2014weather.out
hadoop fs -rm -r 2015weather.out
cd ./spark
spark-submit borough_name.py /user/rda311/clean.csv
spark-submit Date.py /user/rda311/clean.csv
spark-submit keycode.py /user/rda311/clean.csv
spark-submit prem_desc.py /user/rda311/clean.csv
spark-submit Time.py /user/rda311/clean.csv
spark-submit brooklyn_date.py /user/rda311/clean.csv
spark-submit brooklyn_key.py /user/rda311/clean.csv
spark-submit brooklyn_time.py /user/rda311/clean.csv
spark-submit crimeeveryday.py /user/rda311/clean.csv
spark-submit windspeedbyyear.py /user/rda311/weather.csv
spark-submit crime2006.py /user/rda311/clean.csv
spark-submit crime2007.py /user/rda311/clean.csv
spark-submit crime2008.py /user/rda311/clean.csv
spark-submit crime2009.py /user/rda311/clean.csv
spark-submit crime2010.py /user/rda311/clean.csv
spark-submit crime2011.py /user/rda311/clean.csv
spark-submit crime2012.py /user/rda311/clean.csv
spark-submit crime2013.py /user/rda311/clean.csv
spark-submit crime2014.py /user/rda311/clean.csv
spark-submit crime2015.py /user/rda311/clean.csv
spark-submit 2006weather.py /user/rda311/weather.csv
spark-submit 2007weather.py /user/rda311/weather.csv
spark-submit 2008weather.py /user/rda311/weather.csv
spark-submit 2009weather.py /user/rda311/weather.csv
spark-submit 2010weather.py /user/rda311/weather.csv
spark-submit 2011weather.py /user/rda311/weather.csv
spark-submit 2012weather.py /user/rda311/weather.csv
spark-submit 2013weather.py /user/rda311/weather.csv
spark-submit 2014weather.py /user/rda311/weather.csv
spark-submit 2015weather.py /user/rda311/weather.csv
cd ..
hadoop fs -getmerge borough_name.out borough_name.out
hadoop fs -getmerge Date.out Date.out
hadoop fs -getmerge keycode.out keycode.out
hadoop fs -getmerge prem_desc.out prem_desc.out
hadoop fs -getmerge Time.out Time.out
hadoop fs -getmerge DateinBrooklyn.out DateinBrooklyn.out
hadoop fs -getmerge KeysinBrooklyn.out KeysinBrooklyn.out
hadoop fs -getmerge TimeinBrooklyn.out TimeinBrooklyn.out
hadoop fs -getmerge crimeeveryday.out crimeeveryday.out
hadoop fs -getmerge weather.out weather.out
hadoop fs -getmerge 2006crimes.out 2006crimes.out  
hadoop fs -getmerge 2007crimes.out 2007crimes.out
hadoop fs -getmerge 2008crimes.out 2008crimes.out
hadoop fs -getmerge 2009crimes.out 2009crimes.out
hadoop fs -getmerge 2010crimes.out 2010crimes.out
hadoop fs -getmerge 2011crimes.out 2011crimes.out
hadoop fs -getmerge 2012crimes.out 2012crimes.out
hadoop fs -getmerge 2013crimes.out 2013crimes.out
hadoop fs -getmerge 2014crimes.out 2014crimes.out
hadoop fs -getmerge 2015crimes.out 2015crimes.out
hadoop fs -getmerge 2006weather.out 2006weather.out
hadoop fs -getmerge 2007weather.out 2007weather.out
hadoop fs -getmerge 2008weather.out 2008weather.out
hadoop fs -getmerge 2009weather.out 2009weather.out
hadoop fs -getmerge 2010weather.out 2010weather.out
hadoop fs -getmerge 2011weather.out 2011weather.out
hadoop fs -getmerge 2012weather.out 2012weather.out
hadoop fs -getmerge 2013weather.out 2013weather.out
hadoop fs -getmerge 2014weather.out 2014weather.out
hadoop fs -getmerge 2015weather.out 2015weather.out
hadoop fs -rm -r borough_name.out
hadoop fs -rm -r Date.out
hadoop fs -rm -r keycode.out
hadoop fs -rm -r prem_desc.out
hadoop fs -rm -r Time.out
hadoop fs -rm -r DateinBrooklyn.out
hadoop fs -rm -r KeysinBrooklyn.out
hadoop fs -rm -r TimeinBrooklyn.out
hadoop fs -rm -r crimeeveryday.out
hadoop fs -rm -r weather.out
hadoop fs -rm -r 2006crimes.out
hadoop fs -rm -r 2007crimes.out
hadoop fs -rm -r 2008crimes.out
hadoop fs -rm -r 2009crimes.out
hadoop fs -rm -r 2010crimes.out
hadoop fs -rm -r 2011crimes.out
hadoop fs -rm -r 2012crimes.out
hadoop fs -rm -r 2013crimes.out
hadoop fs -rm -r 2014crimes.out
hadoop fs -rm -r 2015crimes.out
hadoop fs -rm -r 2006weather.out
hadoop fs -rm -r 2007weather.out
hadoop fs -rm -r 2008weather.out
hadoop fs -rm -r 2009weather.out
hadoop fs -rm -r 2010weather.out
hadoop fs -rm -r 2011weather.out
hadoop fs -rm -r 2012weather.out
hadoop fs -rm -r 2013weather.out
hadoop fs -rm -r 2014weather.out
hadoop fs -rm -r 2015weather.out