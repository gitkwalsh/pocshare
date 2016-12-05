import os, sys
buf ="use csadata;\ndelete from picklist where ptype='MEM';\n"
for x in range (2,20,2):
          buf = buf + 'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","MEM","");\n'  % (x,x,x)
print buf

buf ="use csadata;\ndelete from picklist where ptype='DISK';\n"
for x in range (8,100,4):
          buf = buf + 'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","DISK","");\n'  % (x,x,x)
print buf

buf ="use csadata;\ndelete from picklist where ptype='CPU';\n"
for x in range (1,7,1):
          buf = buf + 'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","CPU","");\n'  % (x,x,x)
print buf

