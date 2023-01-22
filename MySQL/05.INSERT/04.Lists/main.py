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
  ('Batista', 'Adam', 'Delhi', 'a1@efg.com', '1234' ),
  ('John', 'Cartet', 'Bombay', 'q2@efg.com', '1235' ),
  ('Joseph', 'Antonio', 'Gandhinagar', 'a3@efg.com', '1236' ),
  ('Scrooj', 'Donald', 'Chennai', 'a4@efg.com', '1237' ),
  ('Kevin', 'KA', 'Kochi', 'a5@efg.com', '1238' ),
  ('Robin', 'Pete', 'Culcutta', 'a6@efg.com', '1239' )
]

Y.executemany(sql, val)

X.commit()

print(Y.rowcount, "was inserted.") 

