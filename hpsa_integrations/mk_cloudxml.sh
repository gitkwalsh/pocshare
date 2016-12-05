#!/bin/bash
while true
do
my_rnd=$(date +v%H%M%S)
cp /etc/viewpoint/cloud.xml /var/hpsa/backup/cloud-$my_rnd.xml
python /var/hpsa/vp_buildv1.py 
sleep 140
done
