#!/opt/opsware/agent/bin/python
#Written by Ken Walsh kenneth.walsh@hp.com 1-2010
import traceback
import sys
import os


def get_swsp(sid):
    
    s1 =  open("/var/hpsa/sa_swsp.dat")
    buf="NONE|NONE"
    for line in s1:
        if line.find(sid) > -1:
           if line.find(sid) > -1:
            os_swsp = line.split('|')
            buf    = line.replace('\n','')
    s1.close()
    print "%s" %buf.replace("\n","")
    
if __name__ == '__main__':
    #----------------
    get_swsp(sys.argv[1])


