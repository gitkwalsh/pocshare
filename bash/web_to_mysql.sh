#!/bin/bash
wget -O  /tmp/logo.html  http://192.168.20.196/logo/
cat      /tmp/logo.html  |grep href |awk '{print $5}'|cut -d '"' -f2|grep "\."|awk '{print $1",http://192.168.20.196/logo/"$1}' > /tmp/logo.dat
python  /var/www/html/scripts/pp.py  logo  /tmp/logo.dat   >  /var/www/scripts/data/osdata2.sql
mysql -ucsauser -ppwcsauser  < /var/www/scripts/data/osdata2.sql
