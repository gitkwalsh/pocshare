import sys,os

def csa_updte():
  hcmd1 = "curl   -k -u admin:cloud 'https://csa420a.myhome2k.org:8445/PAS/services/http/execute/Library/sub_flows/csa/csa_prop_m?CSA_CONTEXT_ID="
  cf = open('/root/AWSscripts/data/instances.dat','r')
  db_address='-na-'
  for l in cf:
   if l.find('requested') > -1:
     la = l.split(',')
     sub = la[0]
     db_identifer = la[1]
     fs = open('/root/AWSscripts/data/status_all.dat','r')
     for ls in fs:
       if ls.find(la[1]) > -1:
        lsa = ls.split(',')
        db_status = lsa[1]
        if db_status.find('available') > -1:
          db_address = lsa[2]
        oo_pass = "%s&pnameval_list=instance_status,%s!Address,%s" % (sub,db_status,db_address)
        my_cmd = hcmd1 + "%s'" % oo_pass
        print my_cmd
        os.system(my_cmd)
     fs.close()
  cf.close()

def csa_mk_status():
    os.system("aws rds  describe-db-instances > /root/AWSscripts/data/dball.dat")
    f = open('/root/AWSscripts/data/dball.dat','r')
    buf =''
    db_address='-na-'
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
    ff = open('/root/AWSscripts/data/status_all.dat','w')
    ff.write(buf)
    ff.close()
    print 'done csa_mk_status'


csa_mk_status()
csa_updte()
