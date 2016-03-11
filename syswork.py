import os
import cgi
import random
import datetime
import dbwork


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
    key = random.randint(1000, 9999)
    return key


def userStart(mac, phone):
    passkode = getAccCode(phone)
    dbwork.addUser(phone, mac, passkode)
    return passkode


def userCheck(mac, phone):
    return dbwork.checkUser(phone, mac)


def passCheck(phone, passkode):
    if passkode == dbwork.getPassOfPhone(phone):
        return True
    else:
        return False
