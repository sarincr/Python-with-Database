import mysql.connector
X = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password= 'password'
)


Y = X.cursor()

Y.execute("SHOW DATABASES")

for x in Y:
    print(x) 
