b=/hpmedia/linux/backup/dbbackupl_`date +%s.sql`
echo backing up last sql to [$b]
cp /var/hpsa/csadata/hpsa.sql $b
echo getting HP-SA content
/opt/opsware/agent/bin/python /var/hpsa/csadata/hpsa.py
echo doing db import
mysqldump --add-drop-table -u csauser -ppwcsauser csadata  > $b
mysql -ucsauser -ppwcsauser < /var/hpsa/csadata/hpsa.sql
mysql -ucsauser -ppwcsauser < /var/hpsa/csadata/aws_cf.sql

/var/hpsa/csadata/osget2.sh
