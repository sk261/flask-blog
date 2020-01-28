'''
DB manager in Python
sqlite3:
import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
'''
