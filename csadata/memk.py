import os, sys
buf ="use csadata;\ndelete from picklist where ptype='memk';\n"
for y in range  (2,10,2):
  abuf =   "%d" % (y*1024)
  buf = buf + 'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","memk","avail");\n'  % (abuf,abuf,abuf)
print buf

