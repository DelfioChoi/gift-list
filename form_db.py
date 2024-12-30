import sqlite3 as sql

con = sql.connect('form_db.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS users')

sql = '''CREATE TABLE "users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "email" VARCHAR UNIQUE NOT NULL,
    "phone" INT NOT NULL
)'''

cur.execute(sql)
con.commit()
con.close()