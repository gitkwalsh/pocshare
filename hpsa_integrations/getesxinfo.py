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
from pytwist.com.opsware.virtualization import *
from pytwist.com.opsware.common import ObjRef
from pytwist.com.opsware.server import ServerRef
 

def  g_vnet(v_hyp):
     v_prtgrps =  v_prtgrp.getPortGroupsByHypervisor(v_hyp)
     print v_prtgrps
     r=''
     for prtgrp in v_prtgrps:
        prgg_vo=  v_prtgrp.getPortGroupVO(prtgrp)
        r=r+  "%s<br>" % (prgg_vo.getName())
     return r


def g_cpu(v_hyp):
        svr_vo = svr_svc.getServerHardwareVO(v_hyp)
        c_pus = svr_vo.getCpus()
        h_mems = svr_vo.getMemories()
        m_tot=0
        for h_mem in h_mems:
           if (h_mem.getType() == 'RAM'):
                m_tot = m_tot + int(h_mem.getQuantity())
        r= '<li>%s-%s <li> MEM %d GB' % (len(c_pus),c_pus[0].getModel(),m_tot/1000000)
        return r

def g_datastor(r_scan):
    hyps= hyp.findHypervisorRefs(None)
    ret='<table border=1>'
    ret= ret +"<tr><th>Hypervisor</th><th>Storage/Total/Free</th></tr>"
    for v_hyp in  hyps:
        if r_scan == 1:
            hyp.scanHypervisor(v_hyp)
        my_ds_refs = ds_service.getDataStoresByHypervisor(v_hyp)
        ret=ret + '<tr><td valign=top><b>%s</b></td><td><table border=1>' % v_hyp.getName()
        v_div = 1073741824.0
        for my_ds_ref in my_ds_refs:
           my_ds_vo= ds_service.getDataStoreVO(my_ds_ref)
           ret= ret +"<tr><td>%s</td><td>%s GB</td><td>%d GB</td></tr>" % (my_ds_vo.getName(),my_ds_vo.getCapacity()/v_div,my_ds_vo.getFreeCapacity()/v_div)
        r="<tr><td>Network</td><td>%s</td></tr>" % g_vnet(v_hyp)
        ret = ret + "%s</table>" %r
    ret=ret +' </table>'
    return ret

def g_getvm(r_scan):
        hyps= hyp.findHypervisorRefs(None)
        v = "<table border=1><tr><th>Hypervisor</th><th>Virtual Server</th></tr>"
        for v_hyp in  hyps:
            if r_scan == '1':
               hyp.scanHypervisor(v_hyp)
            h_ypvo = hyp.getHypervisorVO(v_hyp)
            h_vms  = h_ypvo.getVirtualServers()
            s_cpu = g_cpu(v_hyp)
            v =  v +"<tr><td valign=top><b>%s</b><br>%s</td><td><table border=0>" % (v_hyp.getName(),s_cpu)
            if len(h_vms) == 0:
                v = v + '<tr><td>none<td></tr>'
            for h_vm in h_vms:
                v_svr_vo = v_svr_svc.getVirtualServerVO(h_vm)
                v = v + '<tr><td>%s <br>%s<td></tr>' % (h_vm.getName(),g_cpu(v_svr_vo.getServer()))
            v=v + "</table>"
        v= v + '</table>'
        return v




if __name__ == '__main__':
        re_scan = sys.argv[1]
        ts = twistserver.TwistServer()
        ts.authenticate('webuser','webuser')
        
        vir = ts.virtualization.VirtualServerService
        vst = ts.virtualization
        ds_service = ts.virtualization.DataStoreService
        svr_svc = ts.server.ServerService
        hyp = ts.virtualization.HypervisorService
        hyps= hyp.findHypervisorRefs(None)
        r=''
        #r=r + g_datastor(re_scan)
        r=r+ g_getvm(re_scan)
        print "%s" % (r)
 