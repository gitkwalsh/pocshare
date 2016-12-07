import os, sys
buf ="use csadata;\ndelete from picklist where ptype='flavor';\n"
f= open("/home/cloudadmin/csadata/flavor.dat",'r')
for l in f:
     ar = l.split(',')
     buf = buf + 'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","flavor","");\n'  % (ar[1].replace("\n",""),ar[0],ar[0].replace("\n",""))
print buf

