#!/bin/bash
clear
curl -k https://192.168.136.64:8444/PV/api/v1/vm > $1
python readj.py $1 > $1.sql
if [ "$2" = "yes"  ] ; then
 echo Recreating db
 mysql -ucsauser -ppwcsauser < mktable.sql 
fi
mysql -ucsauser -ppwcsauser < $1.sql
