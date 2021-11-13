import psycopg2

X = psycopg2.connect(database = "postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
print("Opened database successfully")

Y = X.cursor()
Y.execute('''CREATE TABLE COMPANY
      (ID INT PRIMARY KEY     NOT NULL,
      First_NAME           TEXT    NOT NULL,
      Second_NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      EXP         REAL);''')
print("Table created successfully")

X.commit()
X.close()
