import sqlite3

 
conn = sqlite3.connect('NeDB.db')
 
cursor = conn.cursor()


cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

X= '''CREATE TABLE IF NOT EXISTS projects (
	id integer PRIMARY KEY,
	name text NOT NULL,
	begin_date text,
	end_date text
); '''
conn.execute(X)
print("Table created")
 
conn.commit()

 
conn.close()
