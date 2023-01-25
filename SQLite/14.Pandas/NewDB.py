import pandas as pd
import sqlite3
 
conn = sqlite3.connect('NewDB.db')




cursor = conn.cursor()

 
table ="""CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255), SECTION VARCHAR(255));"""
cursor.execute(table)


cursor.execute('''INSERT INTO STUDENT VALUES ('John', '8', 'A')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Adam', '8', 'B')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Ann', '10', 'A')''')




print(cursor.fetchall())
  
conn.commit()


df = pd.read_sql("SELECT * FROM STUDENT", con=conn)
print(df)
df.to_csv("Index.csv")

conn.close()

