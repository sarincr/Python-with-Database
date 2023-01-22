from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd

import mysql.connector
 



X = mysql.connector.connect(
  host="localhost",
  user="newuser",
  password= "PassWord@123",
  database="ABC"
)

app = Flask(__name__)

df = pd.read_sql("SELECT * FROM tblEmployee", con=X)

 

@app.route('/', methods=("POST", "GET"))
def html_table():

    return render_template('index.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)



if __name__ == '__main__':
    app.run(host='0.0.0.0')
