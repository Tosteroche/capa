import sqlite3
from config import dbname
import datetime


def addToBase(mac, phone, passkode):
    db = sqlite3.connect(dbname)
    cur = db.cursor()

    now = datetime.datetime.now()

    f = cur.execute('select phone,mac from users where mac="%s"' % mac)
    f = f.fetchall()
    if not f:
        try:
            cur.execute('''
                insert into users (mac, phone, dreg, daccess, acode, passkode)
                values (?, ?, ?, ?, ?, ?)
            ''', (mac, phone, now, now, 1, passkode))
        except:
            pass    # не придумал
        db.commit()
    else:
        pass    # не пидумал
