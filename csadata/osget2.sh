clear
rm -rf /var/hpsa/csadata/osdata2.sql
rm -rf  /var/hpsa/csadata/index.html
rm -rf  /var/hpsa/csadata/logo.html

wget -O /var/hpsa/csadata/index.html  http://hptools.myhome2k.org/heat/
cat     /var/hpsa/csadata/index.html |grep template |cut -d '=' -f5|cut -d '"' -f2 |awk '{print $1",http://hptools.myhome2k.org/heat/"$1}' >  /var/hpsa/csadata/heat.dat

wget -O  /var/hpsa/csadata/logo.html  http://hptools.myhome2k.org/logo/
cat      /var/hpsa/csadata/logo.html  |grep href |awk '{print $5}'|cut -d '"' -f2|grep "\."|awk '{print $1",http://192.168.136.7/logo/"$1}'  >  /var/hpsa/csadata/logo.dat

python  /var/hpsa/csadata/pp.py OS-heat   /var/hpsa/csadata/heat.dat >   /var/hpsa/csadata/osdata2.sql
python  /var/hpsa/csadata/pp.py  logo  /var/hpsa/csadata/logo.dat   >>  /var/hpsa/csadata/osdata2.sql
mysql -ucsauser -ppwcsauser  <  /var/hpsa/csadata/osdata2.sql
cat  /var/hpsa/csadata/osdata2.sql

