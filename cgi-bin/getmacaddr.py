#!/usr/bin/env python3
import os
import cgi


ipaddr = cgi.escape(os.environ['REMOTE_ADDR'])
mac = os.popen('arp -n %s' % ipaddr).read().split()[8]
print('Content-type: text/html')
print()
print(mac)
