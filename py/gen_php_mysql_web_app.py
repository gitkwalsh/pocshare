import sys,os

fa = sys.argv[1].split('.')
dbhost = sys.argv[2]
dbcon = open('dbcon.php','r')
fsho = open('sho.php','r')
ftop = open('t_op.php','r')
fbot = open('b_ot.php','r')
sspace='#==========================================================\n'

ttop = ftop.read()
bbot = fbot.read()
ssot = fsho.read()
ddbcon = dbcon.read()

dbcon.close()
ftop.close()
fbot.close()
fsho.close()

header = "<?php\n<title>%s</title></head><body><table border=1> <form action=%s.php target=body>><input type=hidden name=act value=_insert>\n" % (sys.argv[1],fa[0])
def g_input():
 f = open(sys.argv[1],'r')
 fa = sys.argv[1].split('.')
 buf =  "function tb_input ()\n{\n\n\tprint '<table border=1> <form action=%s.php target=body><input type=hidden name=act value=insert>';\n" % fa[0] 
 for l in f:
   la = l.split('|')
   if la[0].find('id') == 0:
     h=99
   else :
    if la[1].find('tinytext') == 0:
    #if la[1].find('varchar') == 0:
      buf =buf + "\tprint '<tr><td>%s</td><td><textarea rows=4 cols=50 name=%s></textarea></td></tr>';\n" % (la[0],la[0])
    else:
      buf =buf + "\tprint '<tr><td>%s</td><td><input type=text name=%s></td></tr>';\n" % (la[0],la[0])
 f.close()
 buf =buf + "\tprint '<tr><td></td><td><input type=submit value=insert></td></tr>';\n\n}" + sspace
 return buf


def g_edit():
 f = open(sys.argv[1],'r')
 fa = sys.argv[1].split('.')
 buf = "function tb_edit($id)\n{\n\n\t$v_query = \"select * from %s where id =$id\";\n" % (fa[0])
 buf = buf + ddbcon
 buf = buf +"\n\t#print \"$v_query\";\n" 
 buf = buf +"\n\tprint '<table border=1>';\t\n" 
 buf = buf +  "\n\tprint \"<form action=%s.php method=post target=body><input type=hidden name=act value=update ><input type=hidden name=id value=$id>\";\n" % (fa[0])
 sr=0
 for l in f:
   la = l.split('|')
   if la[0].find('id') == 0:
     h=99
     sr=sr+1
   else:
    if la[1].find('tinytext') == 0:
      buf =buf + '\tprint "<tr><td>%s</td><td><textarea rows=4 cols=50 name=%s>$srow[%s]</textarea></td></tr>";\n' % (la[0],la[0],sr)
    else:
      buf =buf + '\tprint "<tr><td>%s</td><td><input type=text name=%s value=$srow[%s]></td></tr>";\n' % (la[0],la[0],sr)
      sr =  sr +1
 f.close()
 buf = buf +  "\n\tprint '<tr><td><input type=radio name=killme value=up checked>update <input type=radio name=killme value=del>Delete</td><td><input type=submit value=update></td></tr>';" 
 buf =buf + "}"
 ret = buf 
 ret = ret.replace(",)",")")
 return ret

def g_insert():
 f = open(sys.argv[1],'r')
 fa = sys.argv[1].split('.')
 buf = "\t$v_query = \"insert into %s (" % (fa[0])
 vbuf = "values (" 
 nbuf = "function tb_insert()\n{\n\n"
 for l in f:
   la = l.split('|')
   if la[0].find('id') == 0:
     h=99
   else:
     buf = buf + "%s," % (la[0])
     vbuf = vbuf + "'$%s'," % (la[0])
     nbuf = nbuf + "\t$%s = $_REQUEST['%s'];\n" % (la[0],la[0])
 f.close()
 buf =buf + ")"
 vbuf =vbuf + ");\";\n"
 ret = "%s \n%s %s\n\n\t  f_sqlex($v_query);\ntb_display();\n}%s" % (nbuf,buf,vbuf,sspace)
 ret = ret.replace(",)",")")
 return ret

#bg
def g_update():
 f = open(sys.argv[1],'r')
 fa = sys.argv[1].split('.')
 buf1=''
 buf = "\t$v_query = \"update  %s set " % (fa[0])
 nbuf = "function tb_update($id)\n{\n\n"
 for l in f:
   la = l.split('|')
   if la[0].find('id') == 0:
      #buf1 = buf1 +   "\t$%s = $_REQUEST['%s'];\n" % (la[0],la[0])
      trump = 'looser'
   else:
      buf1 = buf1 +   "\t$%s = $_REQUEST['%s'];\n" % (la[0],la[0])
      buf = buf + " %s ='$%s', "% (la[0],la[0])
 f.close()
 buf =buf + "where id = $id\";\n "
 buf =buf + "\tprint $_REQUEST['killme'];\n "
 buf =buf + "\tif ( $_REQUEST['killme'] == 'del')\n\t {\n\t\t$v_query=\"delete from %s where id =$id \";\n\t}\n " % fa[0]
 buf = buf.replace(', where',' where')
 buf =buf + " \tprint $v_query;\n"
 buf =buf + " \tprint f_sqlex($v_query);;\n"
 buf =buf + " \tprint tb_display();\n"
 ret = "%s\n%s %s\n}%s" % (nbuf,buf1,buf,sspace)
 ret = ret.replace(",)",")")
 return ret

def g_display():
 f = open(sys.argv[1],'r')
 fa = sys.argv[1].split('.')
 buf = "function tb_display()\n{\n\n\t$v_query = \"select * from %s \";\n" % (fa[0])
 pbuf = "\n\t\tprint \"<tr>" 
 sr=0
 for l in f:
   la = l.split('|')
   if sr == 0:
     pbuf = pbuf + "<td><a href=%s.php?id=$srow[%s]&act=edit target=input>$srow[%s]</a></td>" % (fa[0],sr,sr)
   else:
    pbuf = pbuf + "<td>$srow[%s]</td>" % sr
   sr =  sr +1
 f.close()
 pbuf =  pbuf + "</tr>\";\n" 
 buf =  buf +  ssot
 buf =  buf.replace('mampi',pbuf)
 ret = "%s  \n}\n%s" % (buf,sspace)
 ret = ret.replace(",)",")")
 return ret


#bg

#bg



print ttop 
#print g_update()
print g_input()
print g_insert()
print g_display()
print g_edit()
print g_update()
bbot = bbot.replace('_pname',fa[0])
print bbot.replace('_dbhost',dbhost)

