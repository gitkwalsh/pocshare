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


def getjobstatus(jobID):
        jobID= sys.argv[1]
        filter = Filter()
        filter.expression = "(job_id = %s)" % jobID
        jobsRefs = job_service.findJobRefs(filter)
        if len(jobsRefs) == 0:
            print "no Job Found"
            sys.exit(0)
        for jobsRef in jobsRefs:
            jobvo= job_service.getJobInfoVO(jobsRef)
            out="%s|%s|%s|%s" % (jobsRef.getId(),jobvo.getType(),jobvo.getStatus(),jobvo.getDescription())
        return out


if __name__ == '__main__':
    ts = twistserver.TwistServer()
    hpsa_user="webuser"
    hpsa_passwd="webuser"
    ts.authenticate(hpsa_user,hpsa_passwd)
    job_service = ts.job.JobService
    svr_svc = ts.server.ServerService
    os_seq_service = ts.osprov.OSSequenceService
    #----------------
    ret = getjobstatus(sys.argv[1])
    print ret

