#!/opt/opsware/agent/bin/python
#Written by Ken Walsh kenneth.walsh@hp.com 1-2010
# -*- mode: Python; tab-width: 4; indent-tabs-mode: nil; -*-
# ex: set tabstop=4 :
# Please do not change the two lines above. See PEP 8, PEP 263.
#
"""
(c) Copyright 2011 Hewlett-Packard Development Company, L.P.
"""
import sys, os, traceback, time, string

sys.path.insert(0, "/opt/opsware/pylibs2")
sys.path.append("/opsw/apx/runtime/script/osprov.run_os_build_plan_papx")

from pytwist import *
from pytwist.com.opsware.server import ServerRef
from pytwist.com.opsware.osprov import AutomaticProvisioningRule
from pytwist.com.opsware.common import NotFoundException
import librunplan

ts = twistserver.TwistServer()
serverservice = ts.server.ServerService
osseqservice = ts.osprov.OSSequenceService

def unset_prov_rule(svrid):
        # get the server's MAC address and facility
        svrref = ServerRef(svrid)
        try:
                svrvo = serverservice.getServerVO(svrref)
        except NotFoundException:
                raise librunplan.ShowErrorMessage("Cound not find server record with ID %s" % svrid, EC_EXCEPTION)

        # get the server's facility (if the prov job is happening in a sat that defines
        # its own facility, the server's facility will not be the same as the buildmgr's)
        facilityref = svrvo.facility
        hwvo = serverservice.getServerHardwareVO(svrref)

        # to be safe, we'll clear the prov rule for all interfaces on the server
        # (it's too hard to tell which one it actually PXE boots off of)
        for interface in hwvo.interfaces:
                mac = interface.hardwareAddress
                unset_prov_rule_for_mac(mac, facilityref)

def unset_prov_rule_for_mac(mac, facilityref):
        # remove the auto prov rule (which will remove the symlink in /opt/opsware/boot/tftpboot/pxelinux.cfg/)
        autoprovrule = AutomaticProvisioningRule()
        autoprovrule.macAddress = mac
        try:
                osseqservice.clearAutomaticProvisioningRule(autoprovrule, facilityref)
        except:
                tb = apply(traceback.format_exception, sys.exc_info())
                tb_message = string.join(tb , "\n")
                if string.find(tb_message, "No such file or directory") == -1:
                        raise librunplan.ShowErrorMessage(tb_message, EC_EXCEPTION)
                else:
                        # that's fine, it didn't exist in the first place
                        pass

mid = librunplan.getMID()
print mid
#unset_prov_rule(mid)
