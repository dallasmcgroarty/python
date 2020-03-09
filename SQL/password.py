import sqlite3
conn = sqlite3.connect("users.db")

# query

c = conn.cursor()

conn.commit()
conn.close()