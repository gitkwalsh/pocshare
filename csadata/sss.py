import os, sys
buf ="use csadata;\ndelete from picklist where ptype='OS-rimages';\n"
for x in range (2,20,2):
          buf = buf + 'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","OS-rimages","");\n'  % (x,x,x)
print buf

