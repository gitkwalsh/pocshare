#!/opt/opsware/agent/bin/python
#Written by Ken Walsh kenneth.walsh@hp.com 1-2010
import traceback
import sys
import os


def get_config(sid):
    
    s1 =  open("/var/hpsa/sa_info.dat")
    for line in s1:
        #print line
        #os_seq|1540001|HP-rhel53|RHEL5U3_x64|CPU-1 MEM-2 GB Disk-12 GB |Guestos-rhel5_64Guest|10.11|.5
        if line.find('os_seq') > -1:
           if line.find(sid) > -1:
            os_seq_ar = line.split('|')
            seq_id    = os_seq_ar[1]
            seq_name  = os_seq_ar[2]
            seq_desc  = os_seq_ar[3].replace("\n","")
            seq_guestos  = os_seq_ar[5].replace("Guestos-","")
            s_cost  = os_seq_ar[6].replace("\n","")
            h_cost  = os_seq_ar[7].replace("\n","")
            pxeImg  = os_seq_ar[8].replace("\n","")
            print "seq_id=%s" % seq_id
            print "seq_name=%s" % seq_name
            print "seq_desc=%s" % seq_desc
            print "seq_guestos=%s" % seq_guestos
            print "s_cost=%s" % s_cost
            print "h_cost=%s" % h_cost
            print "pxeImg=%s" % pxeImg
    s1.close()
def get_ds_config(vmHost):
    
    s1 =  open("/var/hpsa/ds/hpds.dat")
    for line in s1:
         if line.find(vmHost) > -1:
            os_seq_ar = line.split('|')
            dataStore=os_seq_ar[1]
            print "dataStore=%s" % dataStore
    s1.close()  
    
if __name__ == '__main__':
    #----------------
    get_config(sys.argv[1])
    get_ds_config(sys.argv[2])
  

