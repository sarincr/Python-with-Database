import mysql.connector
X = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password= 'password',
  database="ABC"
  
)

Y = X.cursor()

InD = '''
 INSERT INTO tblEmployee (employee_first_name, employee_last_name) values ('John','Adam');
'''

Y.execute(InD)

X.commit()

print(Y.rowcount, "record inserted.")

