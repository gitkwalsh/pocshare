#!/bin/bash 
systemctl start mariadb
/bin/sleep 5
/usr/bin/mysqladmin -u root password 'go.HP.software'
/bin/sleep 5
/usr/bin/mysql -uroot -pgo.HP.software < /tmp/scr.sql
/bin/sleep 3 
/usr/bin/mysql -uroot -pgo.HP.software < /tmp/sugarcrmdb.sql
/usr/bin/mysql  -uscrm -ppwscrm < /tmp/sname.sql
