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
    svr_filter = Filter()
    #svr_filter.expression =  "(ServerVO.hostName = %s)  " % svr_name   
    svr_filter.expression =  "(ServerVO.name = %s)  " % svr_name   
    svr_refs = 	server_service.findServerRefs(svr_filter)
    if len(svr_refs) ==0:
        print "Error|server %s not found" % svr_name
        sys.exit(1)
    
  
    if len(sp_pols) ==0:
        print "Error|software police %s not found" % sp_name
        sys.exit(1)
    #print "found server[%s] and sp [%s]" % (svr_name,sp_name)
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
    hpsa_user='hpsa_admin'
    hpsa_passwd='T@pT3ch1'
    ts.authenticate(hpsa_user,hpsa_passwd)
    job_service = ts.job.JobService
    server_service = ts.server.ServerService
    os_seq_service = ts.osprov.OSSequenceService
    sp_service     = ts.swmgmt.SoftwarePolicyService
    
    vir = ts.virtualization.VirtualServerService
    vst = ts.virtualization
    hyp = ts.virtualization.HypervisorService
    
    dep_swpol(svr_name,sp_name)
