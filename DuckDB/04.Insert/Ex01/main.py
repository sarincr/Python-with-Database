import duckdb
con = duckdb.connect(database='NewDB', read_only=False)


con.execute('''CREATE TABLE Employee(id INTEGER, name VARCHAR);''')

con.execute('''INSERT INTO Employee VALUES (1, 'Adam'), (2, 'John');''')
 
con.execute("SELECT * FROM Employee")
print(con.fetchall())
