import duckdb
cursor = duckdb.connect()
print(cursor.execute('SELECT 42').fetchall())

