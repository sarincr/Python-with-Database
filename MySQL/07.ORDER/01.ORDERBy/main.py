import mysql.connector
X = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password= "PassWord@123",
  database="ABC"
)


 

Y = X.cursor()


sql = "SELECT * FROM tblEmployee ORDER BY Employee_first_name"

Y.execute(sql)

myresult = Y.fetchall()

for x in myresult:
  print(x)
 
