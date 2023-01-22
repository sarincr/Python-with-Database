import mysql.connector
import pandas as pd



X = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password= "PassWord@123",
  database="ABC"
)


 

Y = X.cursor()


sql = "SELECT * FROM tblEmployee"

Y.execute(sql)



Z = Y.fetchall()



for x in Z:
  print(x)
  
df = pd.DataFrame(Z)
print(df.describe())
df.to_csv("Data.csv")
