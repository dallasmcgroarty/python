import sqlite3
conn = sqlite3.connect("SQL/users.db")

c = conn.cursor()
# query
u = input("please enter your username...")
p = input("please enter your password...")
query = f"SELECT * FROM users WHERE username=? AND password=?"

c.execute(query, (u,p))

result = c.fetchone()
if result:
    print('Welcome back!')
else:
    print('Failed Login!')
conn.commit()
conn.close()