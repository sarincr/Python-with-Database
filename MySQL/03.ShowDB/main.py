import mysql.connector
X = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password= 'password'
)


Y = X.cursor()

Y.execute("CREATE DATABASE ABC")

print(Y)
