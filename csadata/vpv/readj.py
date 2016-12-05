import sys,os
def ssp(l):
  aret = l.split(':')
  ret = aret[1]
  ret = ret.replace('"','')
  ret = ret.replace(' ','')
  ret = ret.replace(',','')
  return ret
buf=''
sbuf='use csadata;\n truncate hpvm;\n'
f=open(sys.argv[1],'r')
for l in f:
 l =l.replace('\n','')
 if l.find('"ManagementIP"') > -1:
   svrip = ssp(l)

 if l.find('"SystemVirtType"') > -1:
   hyptype = ssp(l)

 if l.find('"ClusterName"') > -1:
   cluster = ssp(l)

 if l.find('"SystemName"') > -1:
   systemname = ssp(l)

 if l.find('"SystemHostHostName"') > -1:
   vmhostname = ssp(l)
 
 if l.find('"SystemID"') > -1:
   uuid = ssp(l)

 if l.find('"resourcepath"') > -1:
  buf = buf + "%s,%s,%s,%s,%s\n" % (uuid,systemname,cluster,vmhostname,hyptype)
  sbuf = sbuf + "insert into csadata.hpvm (vmid,vmname,cluster,vmhost,hyptype) values ('%s','%s','%s','%s','%s');\n" % (uuid,systemname,cluster,vmhostname,hyptype)


print sbuf


