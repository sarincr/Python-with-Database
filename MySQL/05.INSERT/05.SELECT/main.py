import mysql.connector
X = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password= 'password',
  database="ABC"
  
)


Y = X.cursor()

Y.execute("SELECT * FROM tblEmployee")

myresult = Y.fetchall()

for x in myresult:
  print(x)
