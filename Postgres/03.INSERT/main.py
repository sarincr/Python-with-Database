import psycopg2

X = psycopg2.connect(database = "postgres", user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432")
print("Opened database successfully")

Y = X.cursor()


Y.execute('''CREATE TABLE COMPANY
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      EXP         REAL);''')

Y.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS, EXP) \
      VALUES (1, 'Adam', 32, 'Delhi', 20 )");


X.commit()
X.close()
