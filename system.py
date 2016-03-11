import os
import sys
import cgi
import random


def getIp():
    return os.environ['REMOTE_ADDR']


def getMac(ip=False):
    cmd = ''
    if not ip:
        ip = getIp()
        cmd = 'sudo arp -n %s' % ip
    else:
        cmd = 'sudo arp -n %s' % ip
    mac = os.popen(cmd).read().split()[8]
    return mac


def getAccCode(phone):
    random.seed(phone)
    random.randint(1000, 9999)
