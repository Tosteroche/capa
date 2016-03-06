#!/usr/bin/env python3
import os
import cgi
import datetime
import sqlite3


db = 'db.sqlite3'

ipaddr = cgi.escape(os.environ['REMOTE_ADDR'])
mac = os.popen('arp -n %s' % ipaddr).read().split()[8]

form = cgi.FieldStorage()
phone = form.getfirst('phone', None)
if not phone:
    print('Content-type: text/html')
    print()
    print('нет телефона, нет интернета')
else:
    phone = cgi.escape(phone)
    now = datetime.datetime.now()
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('insert into users (phone, mac, date, key) values(?,?,?,?)', (phone, mac, now, 'hello'))
    conn.commit()
    print('Content-type: text/html')
    print()
    print('''
            <html>
                <head>
                    <meta charset="utf-8">
                    <title>Обработка данных</title>
                </head>
                <body>
                    IP Address: %s<br>
                    MAC Address: %s<br>
                    Phone: %s<br>
                </body>
            </html>
    ''' % (ipaddr, mac, phone))


# print('Content-type: text/html')
# print()
# print(mac)
