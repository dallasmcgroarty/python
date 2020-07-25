import sqlite3
conn = sqlite3.connect("SQL/my_friends.db")

c = conn.cursor()

people = [
	("Roald","Amundsen", 5),
	("Rosa", "Parks", 8),
	("Henry", "Hudson", 7),
	("Neil","Armstrong", 7),
	("Daniel", "Boone", 3)]


# c.executemany("INSERT INTO friends VALUES (?,?,?)", people)
average = 0 # example if you wanted to get average as well
for person in people:
    c.execute("INSERT INTO friends VALUES (?,?,?)", person)
    print("Inserting friend..")
    average += person[2]
conn.commit()
conn.close()