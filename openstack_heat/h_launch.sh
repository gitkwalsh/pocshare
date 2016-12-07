source /home/cloudadmin/csadata/demo.sh
echo heat stack-create $1  --template-file=$2 -P "$3" > /home/cloudadmin/csadata/data/$1_stack.run
chmod u+x  /home/cloudadmin/csadata/data/$1_stack.run
/home/cloudadmin/csadata/data/$1_stack.run > /home/cloudadmin/csadata/data/$1_stack_create.dat
id=`cat /home/cloudadmin/csadata/data/$1_stack_create.dat |grep $1|awk '{print $2}'`
sleep 45
heat output-show --all $id > /home/cloudadmin/csadata/data/$id.output
python /home/cloudadmin/csadata/h_output.py $id
 
