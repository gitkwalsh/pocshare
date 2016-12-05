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
#______________________________________
if __name__ == '__main__':
    # Take arg of an OS Sequence name
    if len(sys.argv) < 2 :
            print "Usage: <esx> <vmname>" % sys.argv[0]
            sys.exit(1)
    key = sys.argv[2]
    in_vm_name = sys.argv[2]
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
    hyps= hyp.findHypervisorRefs(None)
    for v_hyp in  hyps:
        v_hyp_s = "%s" % v_hyp
        if v_hyp_s.find(svr_name)> -1:
            print "hypervisor found[%s]" % v_hyp_s
            pr_hyp(v_hyp)
#---------------------------


def pr_hyp(h_ref):
    p=1
    h=1
    m=1
    bk_mac_look = 0
    bk_hyp_scan= 0
    while (bk_hyp_scan == 0):
        print 'scanning hypeviosor %s pass num %d' % (svr_name,h)
        h =h+1
        hyp.scanHypervisor(v_hyp)
        vv_svrs = vir.getVirtualServersByHypervisor(v_hyp)
        for vv_svr in vv_svrs:
            vv_svr_s = "%s" %vv_svr
            vv_vm_name = vv_svr_s[0:vv_svr_s.find('(')]
            print "\tlooking for %s pass num %d" % (in_vm_name, p)
            p=p+1
            if vv_vm_name.find(in_vm_name) > -1:
                vmVod=vst.VirtualServerService.getVirtualServerDetailsVO(vv_svr)
                vmnic=vmVod.virtualNICs[0]
                bk_hyp_scan = 1
                vv_vm_svr_id=vv_svr_s[vv_svr_s.find(':')+1:vv_svr_s.find(')')]
                print "\t\tFound %s [%s-%s-%s" % (in_vm_name,vv_vm_name.rstrip(),vv_vm_svr_id,vmnic.mac)
                server_service = ts.server.ServerService
                filter = Filter()
                filter.expression = "device_interface_mac = %s" % vmnic.mac
                while (bk_mac_look == 0):
                    print "\t\tlooking for %s ....pass num %d" % (filter.expression,m)
                    m=m+1
                    ca_svr_refs = server_service.findServerRefs(filter)
                    if len(ca_svr_refs) > 0:
                        ca_svr      = ca_svr_refs[0]
                        print "\t\t\tFound setting CA computername to %s" % fvalue
                        server_service.setCustAttr(ca_svr, 'computername',fvalue)
                        server_service.setCustAttr(ca_svr, 'ComputerName',fvalue)
                        bk_mac_look =1
                    else:
                        time.sleep(15)                    
                            

