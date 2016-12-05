#!/usr/bin/python

# ps.py
# Kenneth Walsh <kenneth.walsh@hp.com>
# Feb 25, 2009

import sys
sys.path.append("/opt/opsware/pylibs2")
sys.path.append("/opt/opsware/agent/pylibs")
from pytwist import *
from pytwist.com.opsware.server import *
from pytwist.com.opsware.search import *
from pytwist.com.opsware.virtualization import *
from pytwist.com.opsware.common import ObjRef
import string



if __name__ == '__main__':
        svr_name = sys.argv[1]
        ts = twistserver.TwistServer()
        ts.authenticate('webuser','webuser')
        vir = ts.virtualization.VirtualServerService
        vst = ts.virtualization
        ds_service = ts.virtualization.DataStoreService
        svr_svc = ts.server.ServerService
        hyp = ts.virtualization.HypervisorService
        v_netsvc = ts.virtualization.VirtualNetworkService
        v_svr_svc = ts.virtualization.VirtualServerService
        v_prtgrp = ts.virtualization.PortGroupService
        hyp = ts.virtualization.HypervisorService
        hyps= hyp.findHypervisorRefs(None)
        
        
        filter = Filter()
        filter.expression = "(ServerVO.name = %s)  " % svr_name
        v_hyp = svr_svc.findServerRefs(filter)
        if len(v_hyp) > 0:
            #print "Found matching name= %s %s" % (v_hyp[0].getName(),svr_name)
            sshvo = svr_svc.getServerHardwareVO(v_hyp[0])
            ssvo = svr_svc.getServerVO(v_hyp[0])
            netint= sshvo.getInterfaces()
            print "HOSTNAME=%s" % ssvo.getName() 
            print "IP=%s" % netint[0].getIpAddress() 
			