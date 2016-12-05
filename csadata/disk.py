import os, sys
buf ="use csadata;\ndelete from picklist where ptype='diskk';\n"
for y in range  (10,60,10):
  abuf =   "%d" % (y*1024)
  buf = buf + 'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","diskk","avail");\n'  % (abuf,abuf,abuf)
print buf

