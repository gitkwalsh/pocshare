import os, sys
buf ="use csadata;\ndelete from picklist where ptype='SIZE';\n"
for x in range (1,5,1):
	for y in range  (12,80,10):
          abuf =   "%d-%d-%d" % (x,x,y)
          buf = buf + 'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","SIZE","Win");\n'  % (abuf,abuf,abuf)
print buf

