clear
source /home/cloudadmin/csadata/demo.sh
rm -rf /home/cloudadmin/csadata/osdata.sql
nova image-list  |grep ACTIVE |awk '{print $4 ","$2}'  > /home/cloudadmin/csadata/image.dat
nova flavor-list |grep 'True' |awk '{print $4,$2,"MEM,"$6"!DISK,"$8"!CPU,"$13}' > /home/cloudadmin/csadata/hp.dat
nova keypair-list |grep ':' |awk '{print $2 ","$2}' > /home/cloudadmin/csadata/keypair.dat
#python /home/cloudadmin/csadata/image.py > /home/cloudadmin/csadata/osdata.sql
python /home/cloudadmin/csadata/pp.py osimage /home/cloudadmin/csadata/image.dat >> /home/cloudadmin/csadata/osdata.sql
python /home/cloudadmin/csadata/keypair.py >> /home/cloudadmin/csadata/osdata.sql
python  /home/cloudadmin/csadata/pt.py osflavor /home/cloudadmin/csadata/hp.dat >> /home/cloudadmin/csadata/osdata.sql
mysql -ucsauser -ppwcsauser -hhptools < /home/cloudadmin/csadata/osdata.sql
cat /home/cloudadmin/csadata/osdata.sql

