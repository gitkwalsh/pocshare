import os, sys
buf ="use csadata;\ndelete from picklist where ptype='TPLATE';\n"
f= open("templ.dat",'r')
for l in f:
     ar = l.split(',')
     buf = buf + 'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","TPLATE","%s");\n'  % (ar[0],ar[1],ar[2].replace("\n",""),ar[3].replace("\n",""))
print buf

