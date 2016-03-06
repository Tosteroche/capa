import sqlite3


comm = sqlite3.connect('db.sqlite3')
cur = comm.cursor()
#cur.execute('drop table if exist users')

cur.execute('''create table users (
        id      integer primary key,
        phone   int,
        mac     text,
        date    date,
        key     text
)''')
