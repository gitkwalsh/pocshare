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


def get_os_seq_name(seq_name):
    filter = Filter()
    filter.expression = "(OSSequenceVO.name = \"%s\")  " % seq_name
    seq_ref = 	os_seq_service.findOSSequenceRefs(filter)
    if len(seq_ref) ==0:
      ret= 'Error'
    else:
      ret= seq_ref[0].id 
    print ret

if __name__ == '__main__':
    seq_name = sys.argv[1]
    ts = twistserver.TwistServer()
    hpsa_user='webuser'
    hpsa_passwd='webuser'
    ts.authenticate(hpsa_user,hpsa_passwd)
    os_seq_service = ts.osprov.OSSequenceService
    get_os_seq_name(seq_name)
