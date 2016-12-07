echo [csaoo] $1 $2 $3 > /root/AWSscripts/data/csa_config.dat
bkt=$3
aws s3 ls $3 | awk -v bkt=$3 '{print "https://s3.amazonaws.com/" bkt "/"$4 ","$4}' > /root/AWSscripts/data/s3bucket.dat
python /root/AWSscripts/insert_csa_picklistdb.py  > /root/AWSscripts/data/$3s3.sql
scp /root/AWSscripts/data/mycfs3.sql root@hptools.myhome2k.org:/var/hpsa/csadata/aws_cf.sql

