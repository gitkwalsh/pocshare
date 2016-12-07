import os, sys
buf ="use csadata;\ndelete from picklist where ptype='myimg';\n"
f= open("/home/cloudadmin/csadata/image.dat",'r')
for l in f:
     ar = l.split(',')
     buf = buf + 'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","myimg","");\n'  % (ar[1].replace("\n",""),ar[0].replace("\n",""),ar[1].replace("\n",""))
f.close()
print buf
