import mariadb
import sys

X = mariadb.connect(
    host="localhost",
  user="username",
  password="password"
    )

Y = X.cursor()
Y.execute(''' CREATE DATABASE Products;  ;''')

 
Y.execute("SHOW DATABASES")

for x in Y:
    print(x) 
