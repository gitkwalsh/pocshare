import os, sys
buf ="use csadata;\ndelete from picklist where ptype='HPIMAGE';\n"
f= open("hpimg.dat",'r')
for l in f:
 ar = l.split(',')
 buf = buf + 'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","HPIMAGE","avail");\n'  % (ar[0],ar[1].replace("\n",""),ar[1].replace("\n",""))

print buf

