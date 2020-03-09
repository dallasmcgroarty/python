import sqlite3
conn = sqlite3.connect("SQL/users.db")

c = conn.cursor()

people = [
	("Roald", "slnfi4nt4"),
	("Rosa", "08i70kjhf"),
	("Henry", "mypasshehe"),
	("Neil", "neil98theman!"),
	("Daniel", "dantheman34x1*"),
    ("Dallas", "password")]

c.execute("CREATE TABLE users (username TEXT, password TEXT);")
c.executemany("INSERT INTO users VALUES (?,?)", people)

conn.commit()
conn.close()
