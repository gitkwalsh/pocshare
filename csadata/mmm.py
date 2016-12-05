import os, sys
f = open(sys.argv[2],'r')
buf ="use csadata;\ndelete from picklist where ptype='%s';\n" % (sys.argv[1])
for x in f:
          x = x.replace('\n','')
          buf = buf + 'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","%s","avail");\n'  % (x,x,x,sys.argv[1])
print buf
f.close()
