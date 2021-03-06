#!/opt/opsware/agent/bin/python
#Written by Ken Walsh kenneth.walsh@hp.com 1-2010
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


def showsvr():
    #mac= sys.argv[1]
    filter = Filter()
    filter.expression =  "(ServerVO.name = %s)  " % sys.argv[1]
    svr_refs = svr_svc.findServerRefs(filter)
    for ss in svr_refs:
        buf=''
        sshvo = svr_svc.getServerHardwareVO(ss)
        svrvo = svr_svc.getServerVO(ss)
        netint= sshvo.getInterfaces()
        sip = netint[0].getIpAddress()
        ssip = str(sip)
        print "%s\t%s\t%s" % (ss.name,ssip,svrvo.getManagementIP())
        svrvo.setManagementIP(ssip)
        print "%s\t%s\t%s---new" % (ss.name,ssip,svrvo.getManagementIP())



if __name__ == '__main__':
    ts = twistserver.TwistServer()
    hpsa_user='webuser'
    hpsa_passwd='webuser'
    ts.authenticate(hpsa_user,hpsa_passwd)
    job_service = ts.job.JobService
    svr_svc = ts.server.ServerService
    os_seq_service = ts.osprov.OSSequenceService
    #----------------
    showsvr()
