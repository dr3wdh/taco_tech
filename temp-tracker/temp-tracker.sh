#!/bin/bash

##loop temp sensor date on interval, log to file

#vars
PRE=/home/pi/sandbox/temp-tracker
OUT_FILE=$PRE/output.txt
TEMP_EXEC=$PRE/get-temp.py

while [ true ]
do
	temp=`/usr/bin/python $TEMP_EXEC`
	count_dt=$(date "+%Y-%m-%d %H:%M:%S")
	echo "$count_dt | $temp" >> $OUT_FILE
	sleep 30	
done
