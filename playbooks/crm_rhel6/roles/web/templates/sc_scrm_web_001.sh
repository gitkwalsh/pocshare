#!/bin/bash 
iptables -F
cd /
tar -xvf ssc.tar
sleep 5
sed -i 's/variables_ rder = "GPCS"/variables_order = "EGPCS"/' /etc/php.ini
sed -i "s/192.168.136.85/{{dbip}}/g" /var/www/html/scrm/config.php
sed -i "s/192.168.136.81/{{webip}}/g" /var/www/html/scrm/config.php
wget {{logo}}   -O  /var/www/html/scrm/custom/themes/default/images/company_logo.png

chown apache:apache  /var/www/html/scrm/ -R 
chkconfig iptables off
service iptables stop 
chkconfig httpd on
service httpd restart
sleep 2
