import duckdb
con = duckdb.connect(database=':memory:', read_only=False)
 
con.execute("CREATE TABLE items(item VARCHAR, value DECIMAL(10,2), count INTEGER)")
 
con.execute("SELECT * FROM items")
print(con.fetchall())
