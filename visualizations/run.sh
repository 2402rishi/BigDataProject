cd ./spark
spark-submit borough_name.py /user/rda311/clean.csv
spark-submit Date.py /user/rda311/clean.csv
spark-submit keycode.py /user/rda311/clean.csv
spark-submit prem_desc.py /user/rda311/clean.csv
spark-submit Time.py /user/rda311/clean.csv
hadoop fs -getmerge borough_name.out
hadoop fs -getmerge Date.out
hadoop fs -getmerge keycode.out
hadoop fs -getmerge prem_desc.out
hadoop fs -getmerge Time.out