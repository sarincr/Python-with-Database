import mysql.connector
import pandas as pd



X = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password= "PassWord@123",
  database="ABC"
)


  
df = pd.read_sql("SELECT * FROM tblEmployee", con=X)

print(df.head())
df.to_csv("Data.csv")
