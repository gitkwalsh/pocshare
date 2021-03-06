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


def dep_swpol(svr_name,sp_name):
    #SoftwarePolicyVO.name
    filter = Filter()
    filter.expression = "(SoftwarePolicyVO.name = \"%s\")  " % sp_name
    sp_pols = 	sp_service.findSoftwarePolicyRefs(filter)
    #
    mac= sys.argv[1]
    filter = Filter()
    filter.expression = "device_interface_mac = %s" % mac
    svr_refs = server_service.findServerRefs(filter)
    if len(svr_refs) > 0:
        print "OK,%s" % (svr_refs[0].id)
    else:
      print "Error %s not found" % mac
      sys.exit(1)

    if len(sp_pols) ==0:
        print "Error|software police %s not found" % sp_name
        sys.exit(1)
    sp_service.attachToPolicies(sp_pols,svr_refs)
    jobRef=sp_service.startRemediateNow(sp_pols,svr_refs[0])
    jobvo= job_service.getJobInfoVO(jobRef)
    out="OK|%s|%s|%s|%s" % (jobRef.getId(),jobvo.getType(),jobvo.getStatus(),jobvo.getDescription())
    print "%s" % out

if __name__ == '__main__':
    # Take arg of an OS Sequence name
    if len(sys.argv) < 2 :
            print "Usage: <esx> <vmname>" % sys.argv[0]
            sys.exit(1)
    sp_name  = sys.argv[2]
    svr_name = sys.argv[1]
    ts = twistserver.TwistServer()
    hpsa_user='webuser'
    hpsa_passwd='webuser'
    ts.authenticate(hpsa_user,hpsa_passwd)
    job_service = ts.job.JobService
    server_service = ts.server.ServerService
    os_seq_service = ts.osprov.OSSequenceService
    sp_service     = ts.swmgmt.SoftwarePolicyService
    
    vir = ts.virtualization.VirtualServerService
    vst = ts.virtualization
    hyp = ts.virtualization.HypervisorService
    
    dep_swpol(svr_name,sp_name)
