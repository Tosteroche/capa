import os
import cgi


def getIP():
    ipaddr = os.environ['REMOTE_ADDR']
    return cgi.escape(ipaddr)


def getMac():
    ipaddr = getIP()
    mac = os.popen('arp -n %s' % ipaddr)
    mac = mac.read()
    mac = mac.split()
    mac = mac[8]
    return mac
