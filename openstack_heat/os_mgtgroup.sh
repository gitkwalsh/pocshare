source /home/cloudadmin/csadata/demo.sh
if [ "$1" = "a" ]
then
  nova  secgroup-create $2 \""$3"\" | grep $2 |awk '{print $2'}
fi

if [ "$1" = "d" ]
then
  nova  secgroup-delete  $2 
fi

 
