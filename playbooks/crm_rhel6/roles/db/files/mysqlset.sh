#!/bin/bash 
yum -y install mysql mysql-server
/bin/sleep 5
/usr/bin/mysql_install_db
/bin/sleep 5
/usr/bin/mysqld_safe &
/bin/sleep 5
/usr/bin/mysqladmin -u root password 'go.HP.software'
chkconfig mysqld on
