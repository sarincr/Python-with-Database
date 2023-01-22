import mysql.connector
db_obj = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password"
)
print(db_obj)
