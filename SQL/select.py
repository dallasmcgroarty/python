import sqlite3
conn = sqlite3.connect("SQL/my_friends.db")
# create cursor object
c = conn.cursor()
# c.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")
c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")

# iterate over the cursor
# for result in c:
#     print(result)

# returns the query in a list
#print(c.fetchall())

# fetch a single result i.e. the first one
# print(c.fetchone())

conn.commit()
conn.close()
