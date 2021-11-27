import mariadb
import sys

conn = mariadb.connect(
    host="localhost",
  user="username",
  password="password"
    )


print(conn)
