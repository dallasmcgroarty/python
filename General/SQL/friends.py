import sqlite3
conn = sqlite3.connect("SQL/my_friends.db")
# create cursor object

c = conn.cursor()
# execute some sql

# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# query = '''INSERT INTO friends
#             VALUES ('Merriweather','Lewis', 7)'''

# BAD form for inserting data:
# name = "Dana"
# query = f"INSERT INTO friends (first_name) VALUES ('{name}')"
# c.execute(query)

#Better way!
# form_first = "Mary-Todd"
# query = f"INSERT INTO friends (first_name) VALUES (?)"
# c.execute(query, (form_first,))

#Another good way
data = ("Steve","Irwin", 9)
query = "INSERT INTO friends VALUES (?,?,?)"
c.execute(query, data)
# commit changes
conn.commit()
conn.close()