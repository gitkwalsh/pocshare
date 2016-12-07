import os, sys
buf ="use csadata;\ndelete from picklist where ptype='osimages';\n"
f= open("/home/cloudadmin/csadata/image.dat",'r')
for l in f:
     ar = l.split(',')
     buf = buf + 'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","osimages","");\n'  % (ar[0].replace("\n",""),ar[0].replace("\n",""),ar[0].replace("\n",""))
f.close()
print buf
