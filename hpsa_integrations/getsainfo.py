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


def mk_pagesec():
    seq_refs = os_seq_service.findOSSequenceRefs(None)
    buf =""
    
    for seq_ref in seq_refs:
        seq = os_seq_service.getOSSequenceVO(seq_ref)
        f = seq.getFolder()
        fol_name= f.name
        if string.lower(fol_name) == 'portal':
            seq_id = "%s" % seq_ref.getId()
            seq_id=seq_id[0:len(seq_id)-1]
            seq_name = seq.name
            seq_desc= seq.description
            buf= buf +"os_seq|%s|%s|%s\n" % (seq_id,seq_name,seq_desc)

    if buf > "" :
        f1 = open("/var/hpsa/sa_info.dat","w")
        f1.write(buf)
        f1.close()
    return buf

if __name__ == '__main__':
    ts = twistserver.TwistServer()
    ts.authenticate('webuser','webuser')
    job_service = ts.job.JobService
    server_service = ts.server.ServerService
    os_seq_service = ts.osprov.OSSequenceService
    #----------------
    ret = mk_pagesec()
  

