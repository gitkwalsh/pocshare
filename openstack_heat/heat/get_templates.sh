wget http://192.168.136.7/heat/
clear;cat     index.html |grep template |cut -d '=' -f5|cut -d '"' -f2 |awk '{print "wget http://hptools.myhome2k.org/heat/"$1}'

