import sys,os
def c_lean(x):
     x= x.replace(',','')
     x= x.replace('\n','')
     x= x.replace('"','')
     return x
f = open(sys.argv[1],'r')
m=''
for l in f:
  if l.find('StackId":') > -1 :
    lstackid = l.split('":')
    la       = lstackid[1]
    la = la.replace(' ','') 
    la = c_lean(la)
    m = m + "%s!" % la 


  if l.find('StackStatus":') > -1 :
    lstatus  = l.split(':')
    m = m + "%s!" % c_lean(lstatus[1].replace(' ','')) 


  if l.find('StackName":') > -1 :
    lstatus  = l.split(': ')
    m = m + "%s!" % c_lean(lstatus[1]) 


  if l.find('OutputKey":') > -1 :
    lstatus  = l.split(':')
    m = m + "%s" % c_lean(lstatus[1]) 

  if l.find('OutputValue":') > -1 :
    lstatus  = l.split(': ')
    m = m + ",%s!" % c_lean(lstatus[1]) 


f.close()
print m
