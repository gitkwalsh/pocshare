#!/opt/opsware/agent/bin/python
#Written by Ken Walsh kenneth.walsh@hp.com 12-2010

#OK|11950001L|server.swpolicy.remediate|1|Remediate Policies

#import traceback
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


def chk_forruninjob(svr_name,de_bug):
    svr_filter = Filter()
    svr_filter.expression =  "(ServerVO.hostName = %s)  " % svr_name
    svr_refs =  server_service.findServerRefs(svr_filter)
    if len(svr_refs) ==0:
        print "Error|server %s not found" % svr_name
        sys.exit(1)
    svr_id =  "=%s" % svr_refs[0].getId()
    filter = Filter()
    jobType    = "server.swpolicy.remediate"
    jobStatus  = "ACTIVE"
    filter.expression = "((job_type = %s) & (job_status = %s ) & (job_device_id = %s ))" % (jobType,jobStatus,svr_id)
    #print "[%s]" % filter.expression
    jobs = job_service.findJobRefs(filter)
    ret="OK|jobsFound|%s" %  len(jobs)
    if de_bug == "1":
      for thisJob in jobs:
        jobvo= job_service.getJobInfoVO(thisJob)
        ret=ret + "\nRunningJobs|%s|%s|%s|%s|%s" % (thisJob.getId(),jobvo.getType(),jobvo.getStatus(),jobvo.getDescription(),jobvo.getUserName())
    return ret 

if __name__ == '__main__':
    # Take arg of an OS Sequence name
    if len(sys.argv) < 1 :
            print "Usage: >" % sys.argv[0]
            sys.exit(1)
    svr_name = sys.argv[1]
    de_bug = sys.argv[2]
    ts = twistserver.TwistServer()
    hpsa_user="webuser"
    hpsa_passwd="webuser"
    ts.authenticate(hpsa_user,hpsa_passwd)
    job_service = ts.job.JobService
    server_service = ts.server.ServerService
    
    print chk_forruninjob(svr_name,de_bug)
