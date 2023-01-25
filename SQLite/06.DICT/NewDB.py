 
import sqlite3
 
conn = sqlite3.connect('NewDB.db')

 
cursor = conn.cursor()

 
table ="""CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255), SECTION VARCHAR(255));"""
cursor.execute(table)

students = [('John', '8', 'A'),
   ('Adam', '8', 'B'),
   ('Ann', '10', 'A'),
]

cursor.executemany('INSERT INTO STUDENT VALUES (?,?,?)', students)

print("Data Inserted in the table: ")
data=cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
	print(row)


conn.commit()

conn.close()
