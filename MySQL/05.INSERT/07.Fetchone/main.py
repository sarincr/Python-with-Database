import mysql.connector
X = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password= 'password',
  database="ABC"
  
)


Y = X.cursor()

Y.execute("SELECT Employee_id, Employee_first_name, Employee_last_name FROM tblEmployee")

myresult = Y.fetchone()

for x in myresult:
  print(x)
