import mysql.connector
X = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password= 'password',
  database="ABC"
  
)

Y = X.cursor()

sql = "INSERT INTO tblEmployee (Employee_first_name, Employee_last_name, Employee_Address, Employee_emailID, Employee_department_ID) VALUES (%s, %s, %s, %s, %s) "
val = [
  ('John', 'Adam', 'India', 'abc@efg.com', '1234' )
]

Y.executemany(sql, val)

X.commit()

print(Y.rowcount, "Data Inserted") 
