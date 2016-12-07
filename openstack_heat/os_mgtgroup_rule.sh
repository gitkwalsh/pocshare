#!/bin/bash
source /home/cloudadmin/csadata/demo.sh
if [ "$1" = "a" ]
then
  echo nova secgroup-add-rule $2 $3 $4 $5 "0.0.0.0/0"
  nova secgroup-add-rule $2 $3 $4 $5 "0.0.0.0/0"
fi

