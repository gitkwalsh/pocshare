#!/bin/bash
/usr/bin/mysql -uroot -pgo.HP.software < /tmp/scr.sql 
/usr/bin/mysql -uscrm -ppwscrm < /tmp/sugarcrmdb.sql 
/usr/bin/mysql -uscrm -ppwscrm < /tmp/sname.sql 
