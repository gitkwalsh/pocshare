import sys,os
#curl   -k -u admin:cloud "https://csa420a.myhome2k.org:8445/PAS/services/http/execute/Library/sub_flows/csa/csa_prop_m?CSA_CONTEXT_ID=ff8081814d78a58b014d9845bea03386&pnameval_list=Update,1020pm!instance_status,Availdude!instance_identifier,mydb170"

def csa_updte();
  cf = open('/root/AWSscripts/data/instances.dat','r')
  for l in cf:
   if l.find('requested') > -1:
     la = l.split(',')
     sub = la[0]
     db_identifer = la[1]
     db_status = la[2]
     oo_pass = "%s&pnameval_list=instance_status%s" % (sub,db_status)


f = open('/root/AWSscripts/data/dball.dat','r')
buf =''
for l in f :
  if l.find('"Engine"') > -1 :
    db_engine= l[l.find(':')+3:l.find('",')]
  if l.find('"DBInstanceStatus"') > -1 :
    db_status= l[l.find(':')+3:l.find('",')]
  if l.find('Address') > -1 :
    db_address= l[l.find(':')+3:l.find('.com"')+4]
  if l.find('"AvailabilityZone"') > -1 :
    db_az= l[l.find(':')+3:l.find('",')-1]
  if l.find('"DBInstanceIdentifier"') > -1 :
    db_identifier= l[l.find(':')+3:l.find('",')-1]
    buf =buf + "%s,%s,%s,%s,%s\n" % (db_identifier,db_status,db_address,db_az,db_engine)
f.close()
ff = open('/root/AWSscripts/data/statall.dat','w')
ff.write(buf)
