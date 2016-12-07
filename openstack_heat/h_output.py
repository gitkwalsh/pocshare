import os,sys
fname = '/home/cloudadmin/csadata/data/%s.output' % sys.argv[1]
f = open(fname,'r')
val=''
key=''
ret=''
for l in f:
  l = l.replace('\n','')
  l = l.replace(',','')
  l = l.replace('"','')
  if l.find('output_value') > -1:
   la = l.split(':')
   val = la[1]
  if l.find('output_key') > -1:
   lk = l.split(':')
   key = lk[1]
   ret = ret + '%s,%s!' %(key,val)
print '%sstackid,%s' %(ret.replace(' ',''),sys.argv[1])
f.close()
