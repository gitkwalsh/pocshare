import os, sys
buf ="use csadata;\ndelete from picklist where ptype='%s';\n" % sys.argv[1]
f= open(sys.argv[2],'r')
for l in f:
     ar = l.split(',')
     buf = buf + 'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","%s","");\n'  % (ar[1].replace("\n",""),ar[0],ar[0].replace("\n",""),sys.argv[1])
f.close()
print buf
