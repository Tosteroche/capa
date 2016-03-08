#!/usr/bin/env python3
import random
import cgi

import getmac
import dbwork
import fwwork

import config

form = cgi.FieldStorage()

ipadd = getmac.getIP()
mac = getmac.getMac()
phone = form.getfirst('phone', None)

random.seed(phone)
passkode = random.randint(1000, 9999)

dbwork.addToBase(mac, phone, passkode)
fwwork.addToRule(mac)

print('Content-type: text/html')
print()
print('Hello')
print('''
<html>
    <head>
        <meta charset="utf-8">
        <title>Обработка данных</title>
    </head>
    <body>
        ip: %s<br>
        mac: %s<br>
        phone: %s<br>
        pass: %s<br>
    </body>
</html>
''' % (ipadd, mac, phone, passkode))
