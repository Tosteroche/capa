import sqlite3
import datetime


timeformat = '%d-%m-%Y %H:%M:%S'
dbase = 'base.db'

def checkUser(phone, mac):
    db = sqlite3.connect(dbase)
    cur = db.cursor()
    f = cur.execute("select mac,phone from users where mac == %s" % mac)
    f = f.fetchall()
    if not f:               # All gut
        return 0
    elif f[0][1] == phone:  # Already geting passkode
        return 1
    elif f[0][1] != phone:  # Geting passkode, but have no access, and go back whith enother phone
        return 2
    else:
        return 3
    db.close()


def addUser(phone, mac, passkode, acode=0):
    db = sqlite3.connect(dbase)
    cur = db.cursor()
    now = datetime.datetime.now().strftime(timeformat)
    try:
        cur.execute(
        """
            insert into users
            (mac, phone, dreg, dlaccess, passkode, acode)
            values (?,?,?,?,?,?)
        """,
        (mac, phone, now, now, passkode, acode))
        db.commit()
        db.close()
    except:
        print('error')


def getPassOfPhone(phone):
    db = sqlite3.connect(dbase)
    cur = db.cursor()
    f = cur.execute("select passkode from users where phone=%s" % phone)
    f = f.fetchall()
    if len(f) == 1:
        return f[0][0]
    else:
        pass
