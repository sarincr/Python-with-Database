import mysql.connector
X = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password= 'password',
  database="ABC"
  
)


Y = X.cursor()

Y.execute("CREATE TABLE Students (PersonID int,LastName varchar(255),FirstName varchar(255),Address varchar(255),City varchar(255));")

Y.execute("SHOW TABLES")

for i in Y:
  print(i) 
