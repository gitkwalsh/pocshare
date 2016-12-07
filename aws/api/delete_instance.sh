# $1-instance name  $2 $3 $4 
#POP
aws rds delete-db-instance --db-instance-identifier $1 --skip-final-snapshot

