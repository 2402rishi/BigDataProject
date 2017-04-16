cd ./columnsValidation
spark-submit CMPLNT_NUM.py /user/rda311/NYPD_Complaint_Data_Historic.csv
spark-submit CMPLNT_FR_DT.py /user/rda311/NYPD_Complaint_Data_Historic.csv
spark-submit CMPLNT_FR_TM.py /user/rda311/NYPD_Complaint_Data_Historic.csv
spark-submit CMPLNT_TO_DT.py /user/rda311/NYPD_Complaint_Data_Historic.csv
spark-submit CMPLNT_TO_TM.py /user/rda311/NYPD_Complaint_Data_Historic.csv
spark-submit RPT_DT.py /user/rda311/NYPD_Complaint_Data_Historic.csv
spark-submit KY_CD.py /user/rda311/NYPD_Complaint_Data_Historic.csv
spark-submit OFNS_DESC.py /user/rda311/NYPD_Complaint_Data_Historic.csv
spark-submit PD_CD.py /user/rda311/NYPD_Complaint_Data_Historic.csv
spark-submit PD_DESC.py /user/rda311/NYPD_Complaint_Data_Historic.csv
spark-submit CRM_ATPT_CPTD_CD.py /user/rda311/NYPD_Complaint_Data_Historic.csv
spark-submit LAW_CAT_CD.py /user/rda311/NYPD_Complaint_Data_Historic.csv
spark-submit JURIS_DESC.py /user/rda311/NYPD_Complaint_Data_Historic.csv
spark-submit BORO_NM.py /user/rda311/NYPD_Complaint_Data_Historic.csv
spark-submit ADDR_PCT_CD.py /user/rda311/NYPD_Complaint_Data_Historic.csv
spark-submit LOC_OF_OCCUR_DESC.py /user/rda311/NYPD_Complaint_Data_Historic.csv
spark-submit PREM_TYP_DESC.py /user/rda311/NYPD_Complaint_Data_Historic.csv
spark-submit PARKS_NM.py /user/rda311/NYPD_Complaint_Data_Historic.csv
spark-submit HADEVELOPT.py /user/rda311/NYPD_Complaint_Data_Historic.csv
spark-submit Lat_Lon.py /user/rda311/NYPD_Complaint_Data_Historic.csv
cd ..
mkdir output
cd ./output
hadoop fs -getmerge CMPLNT_NUM.out CMPLNT_NUM.out
hadoop fs -getmerge CMPLNT_FR_DT.out CMPLNT_FR_DT.out
hadoop fs -getmerge CMPLNT_FR_TM.out CMPLNT_FR_TM.out
hadoop fs -getmerge CMPLNT_TO_DT.out CMPLNT_TO_DT.out
hadoop fs -getmerge CMPLNT_TO_TM.out CMPLNT_TO_TM.out
hadoop fs -getmerge RPT_DT.out RPT_DT.out
hadoop fs -getmerge KY_CD.out KY_CD.out
hadoop fs -getmerge OFNS_DESC.out OFNS_DESC.out
hadoop fs -getmerge PD_CD.out PD_CD.out
hadoop fs -getmerge PD_DESC.out PD_DESC.out
hadoop fs -getmerge CRM_ATPT_CPTD_CD.out CRM_ATPT_CPTD_CD.out
hadoop fs -getmerge LAW_CAT_CD.out LAW_CAT_CD.out
hadoop fs -getmerge JURIS_DESC.out JURIS_DESC.out
hadoop fs -getmerge BORO_NM.out BORO_NM.out
hadoop fs -getmerge ADDR_PCT_CD.out ADDR_PCT_CD.out
hadoop fs -getmerge LOC_OF_OCCUR_DESC.out LOC_OF_OCCUR_DESC.out
hadoop fs -getmerge PREM_TYP_DESC.out PREM_TYP_DESC.out
hadoop fs -getmerge PARKS_NM.out PARKS_NM.out
hadoop fs -getmerge HADEVELOPT.out HADEVELOPT.out
hadoop fs -getmerge Lat_Lon.out Lat_Lon.out
