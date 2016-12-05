#!/opt/opsware/agent/bin/python
#Written by Ken Walsh kenneth.walsh@hp.com 12-2010
#gets info about a vm
#usage python get_vminfo.py esx4-bay4 vm922
#output
##NAME=vm922
##MAC=00:0c:29:b7:68:90
##HOSTNAME=testrhel
##IP=135.28.86.119

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

def re_name(v_hyp):
   v_found=0
   v_tries=0
   hyp.scanHypervisor(v_hyp)
   while (v_tries < 15):
    h_ypvo = hyp.getHypervisorVO(v_hyp) 
    h_vms  = h_ypvo.getVirtualServers()
    
    for h_vm in h_vms:
        if  h_vm.getName() == vm_name:
            #print "vertual server id [%s] %s" % (h_vm.getId(),h_vm)
           
            vmVod=vst.VirtualServerService.getVirtualServerDetailsVO(h_vm)
            vmnic=vmVod.virtualNICs[0]
           
            #vv_vm_svr_id=vv_svr_s[vv_svr_s.find(':')+1:vv_svr_s.find(')')]
            print "NAME=%s\nMAC=%s" % (h_vm.getName(),vmnic.mac)
            #print "IP=%s" % vmnic.ip 
            
            filter = Filter()
            filter.expression = "device_interface_mac = %s" % vmnic.mac
            ca_svr_refs = server_service.findServerRefs(filter)
            if len(ca_svr_refs) > 0:
                    #print "server ref[%s]" % ca_svr_refs[0]
                    sshvo = server_service.getServerHardwareVO(ca_svr_refs[0])
                    ssvo = server_service.getServerVO(ca_svr_refs[0])
                    netint= sshvo.getInterfaces()
                    print "HOSTNAME=%s" % ssvo.getName() 
                    print "IP=%s" % netint[0].getIpAddress() 
                    ca_svr      = ca_svr_refs[0]
                    #print "\t\t\tFound setting CA computername to %s" % fvalue
                    server_service.setCustAttr(ca_svr, 'ComputerName',fvalue)
                    v_tries=16
           
    v_tries =  v_tries +1 
    if (v_tries > 15) :
      sys.exit(0)
    

if __name__ == '__main__':
    # Take arg of an OS Sequence name
    if len(sys.argv) < 2 :
            print "Usage: <esx> <vmname>" % sys.argv[0]
            sys.exit(1)
    key = sys.argv[2]
    vm_name = sys.argv[2]
    fvalue = sys.argv[2]
    svr_name = sys.argv[1]
    ts = twistserver.TwistServer()
    ts.authenticate('webuser','webuser')
    job_service = ts.job.JobService
    server_service = ts.server.ServerService
    os_seq_service = ts.osprov.OSSequenceService

    vir = ts.virtualization.VirtualServerService
    vst = ts.virtualization
    hyp = ts.virtualization.HypervisorService
    
    # Find the server(s) by MAC
    filter = Filter()
    filter.expression = "(ServerVO.hostName = %s)  " % svr_name
    v_hyp = hyp.findHypervisorRefs(filter)
    if len(v_hyp) == 0:
            print "No Hypervisor found matching name= %s" % svr_name
            sys.exit(1)
    
    re_name(v_hyp[0])