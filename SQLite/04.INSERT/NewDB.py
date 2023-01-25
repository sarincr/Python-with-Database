import sqlite3

 
X = sqlite3.connect('NeDB.db')
 
Y = X.cursor()

 
Y.execute('''CREATE TABLE Employee(date text, First_Name text, Last_Name text, Age real)''')

 
Y.execute("INSERT INTO Employee VALUES ('2020-01-01','John','Adam',32)")
 
X.commit()

Y.close()
