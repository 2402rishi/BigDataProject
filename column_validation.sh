cd ./columnsValidation
spark-submit CMPLNT_NUM.py /user/rda311/NYPD_Complaint_Data_Historic.csv
hfs -getmerge CMPLNT_NUM.out CMPLNT_NUM.out
spark-submit CMPLNT_FR_DT.py /user/rda311/NYPD_Complaint_Data_Historic.csv
hfs -getmerge CMPLNT_FR_DT.out CMPLNT_FR_DT.out
spark-submit CMPLNT_FR_TM.py /user/rda311/NYPD_Complaint_Data_Historic.csv
hfs -getmerge CMPLNT_FR_TM.out CMPLNT_FR_TM.out
spark-submit CMPLNT_TO_DT.py /user/rda311/NYPD_Complaint_Data_Historic.csv
hfs -getmerge CMPLNT_TO_DT.out CMPLNT_TO_DT.out
spark-submit CMPLNT_TO_TM.py /user/rda311/NYPD_Complaint_Data_Historic.csv
hfs -getmerge CMPLNT_TO_TM.out CMPLNT_TO_TM.out
spark-submit RPT_DT.py /user/rda311/NYPD_Complaint_Data_Historic.csv
hfs -getmerge RPT_DT.out RPT_DT.out
spark-submit KY_CD.py /user/rda311/NYPD_Complaint_Data_Historic.csv
hfs -getmerge KY_CD.out KY_CD.out
spark-submit OFNS_DESC.py /user/rda311/NYPD_Complaint_Data_Historic.csv
hfs -getmerge OFNS_DESC.out OFNS_DESC.out
spark-submit PD_CD.py /user/rda311/NYPD_Complaint_Data_Historic.csv
hfs -getmerge PD_CD.out PD_CD.out
spark-submit PD_DESC.py /user/rda311/NYPD_Complaint_Data_Historic.csv
hfs -getmerge PD_DESC.out PD_DESC.out
spark-submit CRM_ATPT_CPTD_CD.py /user/rda311/NYPD_Complaint_Data_Historic.csv
hfs -getmerge CRM_ATPT_CPTD_CD.out CRM_ATPT_CPTD_CD.out
spark-submit LAW_CAT_CD.py /user/rda311/NYPD_Complaint_Data_Historic.csv
hfs -getmerge LAW_CAT_CD.out LAW_CAT_CD.out
spark-submit JURIS_DESC.py /user/rda311/NYPD_Complaint_Data_Historic.csv
hfs -getmerge JURIS_DESC.out JURIS_DESC.out
spark-submit BORO_NM.py /user/rda311/NYPD_Complaint_Data_Historic.csv
hfs -getmerge BORO_NM.out BORO_NM.out
spark-submit ADDR_PCT_CD.py /user/rda311/NYPD_Complaint_Data_Historic.csv
hfs -getmerge ADDR_PCT_CD.out ADDR_PCT_CD.out
spark-submit LOC_OF_OCCUR_DESC.py /user/rda311/NYPD_Complaint_Data_Historic.csv
hfs -getmerge LOC_OF_OCCUR_DESC.out LOC_OF_OCCUR_DESC.out
spark-submit PREM_TYP_DESC.py /user/rda311/NYPD_Complaint_Data_Historic.csv
hfs -getmerge PREM_TYP_DESC.out PREM_TYP_DESC.out
spark-submit PARKS_NM.py /user/rda311/NYPD_Complaint_Data_Historic.csv
hfs -getmerge PARKS_NM.out PARKS_NM.out
spark-submit HADEVELOPT.py /user/rda311/NYPD_Complaint_Data_Historic.csv
hfs -getmerge HADEVELOPT.out HADEVELOPT.out
spark-submit Lat_Lon.py /user/rda311/NYPD_Complaint_Data_Historic.csv
hfs -getmerge Lat_Lon.out Lat_Lon.out
