import pymongo

CLNT = pymongo.MongoClient('mongodb://localhost:27017/')
NewDB = CLNT['NewDatabse']
Tab = NewDB["customers"]

ABC_Dict = { "name": "John", "address": "Highway 37" }

x = Tab.insert_one(ABC_Dict)

print(x)

print("List of collections\n--------------------")

for coll in NewDB.list_collection_names():
    print(coll)
print("Collections\n--------------------")
for n in Tab.find():
  print(n)
