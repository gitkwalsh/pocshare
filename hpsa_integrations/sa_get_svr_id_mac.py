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


def get_svr_mac():
    mac= sys.argv[1]
    filter = Filter()
    filter.expression = "device_interface_mac = %s" % mac
    svr_refs = svr_svc.findServerRefs(filter)
    if len(svr_refs) > 0:
        print "OK,%s" % (svr_refs[0].id)
    else:
      print "Error %s not found" % mac

if __name__ == '__main__':
    ts = twistserver.TwistServer()
    hpsa_user='webuser'
    hpsa_passwd='webuser'
    ts.authenticate(hpsa_user,hpsa_passwd)
    job_service = ts.job.JobService
    svr_svc = ts.server.ServerService
    os_seq_service = ts.osprov.OSSequenceService
    #----------------
    ret = get_svr_mac()
