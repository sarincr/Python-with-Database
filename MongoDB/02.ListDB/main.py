import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

 
mydb = myclient["mydatabase"]

 
 
 
for db in myclient.list_databases():
    print(db)
