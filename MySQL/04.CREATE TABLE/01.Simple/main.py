import mysql.connector
X = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password= 'password',
  database="ABC"
  
)


Y = X.cursor()

Y.execute("CREATE TABLE students (name VARCHAR(255), address VARCHAR(255))")

print(Y)
