import duckdb
con = duckdb.connect(database='NewDB', read_only=False)


con.execute('''CREATE TABLE Employee(id INTEGER, name VARCHAR, AGE INTEGER, SALARY INTEGER, Address VARCHAR);''')

con.execute('''INSERT INTO Employee VALUES (1, 'Adam', 33, 25000, 'Texas'), (2, 'John', 20, 36000, 'Newyork');''')
 
con.execute("SELECT * FROM Employee")
print(con.fetchall())
