hadoop fs -rm -r borough_name.out
hadoop fs -rm -r Date.out
hadoop fs -rm -r keycode.out
hadoop fs -rm -r prem_desc.out
hadoop fs -rm -r Time.out
cd ./spark
spark-submit borough_name.py /user/rda311/clean.csv
spark-submit Date.py /user/rda311/clean.csv
spark-submit keycode.py /user/rda311/clean.csv
spark-submit prem_desc.py /user/rda311/clean.csv
spark-submit Time.py /user/rda311/clean.csv
cd ..
hadoop fs -getmerge borough_name.out borough_name.out
hadoop fs -getmerge Date.out Date.out
hadoop fs -getmerge keycode.out keycode.out
hadoop fs -getmerge prem_desc.out prem_desc.out
hadoop fs -getmerge Time.out Time.out
hadoop fs -rm -r borough_name.out
hadoop fs -rm -r Date.out
hadoop fs -rm -r keycode.out
hadoop fs -rm -r prem_desc.out
hadoop fs -rm -r Time.out