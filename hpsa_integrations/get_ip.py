#!/opt/opsware/agent/bin/python
#Written by Ken Walsh kenneth.walsh@hp.com 1-2010
import traceback
import sys
import re
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



def getsvrip():
    vmName= sys.argv[1]
    filter = Filter()
    filter.expression = "(ServerVO.name = %s)  " % vmName
    v_hyp = svr_svc.findServerRefs(filter)
    if len(v_hyp) > 0:
        sshvo = svr_svc.getServerHardwareVO(v_hyp[0])
        svrvo = svr_svc.getServerVO(v_hyp[0])
        netint= sshvo.getInterfaces()
        #print "HOSTNAME=%s" % svrvo.getName() 
        for mnic in netint:
         sip = mnic.getIpAddress()
         ssip = str(sip)
         if ssip <> 'None' :
           print "IP=%s" % ssip
if __name__ == '__main__':
    ts = twistserver.TwistServer()
    hpsa_user='webuser'
    hpsa_passwd='webuser'
    ts.authenticate(hpsa_user,hpsa_passwd)
    job_service = ts.job.JobService
    svr_svc = ts.server.ServerService
    os_seq_service = ts.osprov.OSSequenceService
    #----------------
    ret = getsvrip()
