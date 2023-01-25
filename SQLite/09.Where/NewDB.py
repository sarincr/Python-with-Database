 
import sqlite3
 
conn = sqlite3.connect('NewDB.db')

 
cursor = conn.cursor()

 
table ="""CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255), SECTION VARCHAR(255));"""
cursor.execute(table)


cursor.execute('''INSERT INTO STUDENT VALUES ('John', '8', 'A')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Adam', '8', 'B')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Ann', '10', 'A')''')


cursor.execute("SELECT * FROM STUDENT WHERE CLASS = '10'")

print(cursor.fetchall())
  
conn.commit()
conn.close()


conn.close()
