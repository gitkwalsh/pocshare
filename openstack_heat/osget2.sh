clear
source demo.sh
rm -rf osdata2.sql
rm -rf index.html
rm -rf logo.html
wget http://ken-pc2/hp/heat/
cat index.html |grep template |awk '{print $6}'|cut -d '"' -f2|awk '{print $1",http://192.168.136.2/hp/heat/"$1}' > heat.dat
wget -O logo.html http://ken-pc2/logo/
cat logo.html  |grep href |awk '{print $5}'|cut -d '"' -f2|grep "\."|awk '{print $1",http://192.168.136.2/logo/"$1}'  > logo.dat
python pp.py OS-heat  heat.dat >>  osdata2.sql
python pp.py  logo logo.dat   >> osdata2.sql
mysql -ucsauser -ppwcsauser -hhptools < osdata2.sql
cat osdata2.sql

