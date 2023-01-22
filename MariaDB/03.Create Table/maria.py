import mariadb
import sys

X = mariadb.connect(
    host="localhost",
  user="username",
  password="password"
    )

Y = X.cursor()
Y.execute(''' CREATE DATABASE Products;  ''')
 
Y.execute('''  USE Products;''')
 
Y.execute('''   CREATE TABLE Students(
    student_id INT NOT NULL AUTO_INCREMENT,
    student_name VARCHAR(100) NOT NULL,
    student_address VARCHAR(40) NOT NULL,
    admission_date DATE,
    PRIMARY KEY ( student_id ));''')
