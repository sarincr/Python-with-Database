import pymongo

CLNT = pymongo.MongoClient('mongodb://localhost:27017/')
NewDB = CLNT['NewDatabse']
Tab = NewDB["customers"]

ABC_Dict = { "name": "John", "address": "Highway 37" }

x = Tab.insert_one(ABC_Dict)

print(x)
print(x.inserted_id)
