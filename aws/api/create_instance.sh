# $1-instance name  $2-master-username $3-master-password $4-engine type Valid values: MySQL | postgres |oracle-se1 | oracle-se | oracle-ee | sqlserver-ee | sqlserver-se | sqlserver-ex | sqlserver-web 
#POP
aws rds create-db-instance --db-instance-identifier $1 --allocated-storage $5 --db-instance-class $6  --engine $4 --master-username $2  --master-user-password $3


