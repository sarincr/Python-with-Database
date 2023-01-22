import mysql.connector
X = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password= 'password',
  database="ABC"
  
)


Y = X.cursor()

sql = "INSERT INTO Students (name, address) VALUES (%s, %s)"
val = ("S1", "State 1")
Y.execute(sql, val)

X.commit()

print(Y.rowcount, "Record inserted.")

for i in Y:
  print(i) 
