#!/opt/opsware/agent/bin/python
#Written by Ken Walsh kenneth.walsh@hp.com 12-2010


import traceback
import sys
import string
# for pytwist support
sys.path.append("/opt/opsware/agent/pylibs")
from pytwist import *
from pytwist.com.opsware.osprov import *
from pytwist.com.opsware.server import *
from pytwist.com.opsware.job import *
from pytwist.com.opsware.search import *
from pytwist.com.opsware.common import *
from pytwist.com.opsware.server import ServerRef
#______________________________________

def getplat(p):
  ret=""
  if p.find("Win") > -1 :
    ret = "Win"
  else:
    ret = "Linux"
  return ret


def listsvr1():
    filter = Filter()
    buf = "use csadata;\ndelete from picklist where ptype='PATCHSVR';\n"
    svr_refs = svr_svc.findServerRefs(filter)
    for svr in svr_refs:
        s_svo = svr_svc.getServerVO(svr)
        s_plat = s_svo.getPlatform()
        buf = buf + 'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","PATCHSVR","%s");\n'  % (svr.id,svr.name,svr.name,getplat(s_plat.name))
    return buf

def listsvr():
    filter = Filter()
    buf = "use csadata;\ndelete from picklist where ptype='SVR';\n"
    svr_refs = svr_svc.findServerRefs(filter)
    for svr in svr_refs:
        s_svo = svr_svc.getServerVO(svr)
        s_plat = s_svo.getPlatform()
        buf = buf + 'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s-%s","%s","SVR","%s");\n'  % (svr.name,svr.name,getplat(s_plat.name),svr.name,getplat(s_plat.name))
    return buf

def listsw(flname):
    filter = Filter()
    filter.expression = "(software_policy_folder_id = \"%s\")  " % flname
    sw_ref = sw_pol_service.findSoftwarePolicyRefs(filter)
    buf = "use csadata;\ndelete from picklist where ptype='SW';\n"
    buf = buf + 'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("-none-","None","None","SW","Win");\n' 
    buf = buf + 'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("-none-","None","None","SW","Linux");\n' 
    bf2=''
    for seq in sw_ref:
       sw_vo = sw_pol_service.getSoftwarePolicyVO(seq)
       pl = sw_vo.getPlatforms()
       #:for pl in platforms:
       if pl[0].name.find('Win') > -1:
              bf2 = bf2 + '%s,%s-Win\n' % (seq.name,seq.name)
              #print "winpe64!winLonghorn64Guest!%s" % (seq.name)
              buf = buf + 'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","SW","Win");\n'  % (seq.name,seq.name,seq.name)
       else:
         
             bf2 = bf2 + '%s,%s-Linux\n' % (seq.name,seq.name)
             buf=   buf +  'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","SW","Linux");\n'  % (seq.name,seq.name,seq.name)
    ff=open("/var/www/html/di_swpol.dat",'w')
    ff.write(bf2)
    ff.close()
    return buf

def listfl(flname):
    filter = Filter()
    filter.expression = "(os_sequence_folder_id = \"%s\")  " % flname
    seq_refs = 	os_seq_service.findOSSequenceRefs(filter)
    buf ="use csadata;\ndelete from picklist where ptype ='OS';\n"
    for seq in seq_refs:
       osseq_vo = os_seq_service.getOSSequenceVO(seq)
       pl = osseq_vo.getPlatforms()
       if pl[0].name.find('Win') > -1:
         if pl[0].name.find('2008') > -1:
          if pl[0].name.find('64') > -1:
           pval= "winpe64!winLonghorn64Guest!%s" % (seq.name)
           buf=   buf +  'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","OS","win");\n'  % (pval,seq.name,seq.name)
         else:
          pval= "winpe!winLonghornGuest!%s" % (seq.name)
          buf=   buf +  'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","OS","win");\n'  % (pval,seq.name,seq.name)
       else:
         if pl[0].name.find('Cent') > -1:
          if pl[0].name.find('64') > -1:
             pval= "linux6!centos64Guest!%s" % (seq.name)
             buf=   buf +  'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","OS","linux");\n'  % (pval,seq.name,seq.name)
       if pl[0].name.find('Red') > -1:
          if pl[0].name.find('64') > -1:
           if pl[0].name.find('ver 5') > -1:
             pval= "linux5!rhel5_64Guest!%s" % (seq.name)
             buf=   buf +  'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","OS","linux");\n'  % (pval,seq.name,seq.name)
           if pl[0].name.find('ver 6') > -1:
             pval= "linux6!rhel6_64Guest!%s" % (seq.name)
             buf=   buf +  'insert into picklist (pvalue,pdisplay,pdesc,ptype,ptype1) values ("%s","%s","%s","OS","linux");\n'  % (pval,seq.name,seq.name)
    return buf      
if __name__ == '__main__':
    flname = "2410001";
    ts = twistserver.TwistServer()
    hpsa_user='webuser'
    hpsa_passwd='webuser'
    ts.authenticate(hpsa_user,hpsa_passwd)
    os_seq_service = ts.osprov.OSSequenceService
    sw_pol_service = ts.swmgmt.SoftwarePolicyService 
    fl = ts.osprov.FolderService
    svr_svc = ts.server.ServerService
    #
    f = open('/var/hpsa/csadata/hpsa.sql','w')
    os_buf =  listfl(flname)
    sw_buf =  listsw(flname)
    svr_buf =  listsvr()
    svr1_buf =  listsvr1()
    f.write(os_buf)
    f.write(sw_buf)
    f.write(svr_buf)
    f.write(svr1_buf)
    f.close()
    print "done"

