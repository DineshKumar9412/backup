import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# # mongodb didn't create database and collection in empty rows. so we need to insert a single row
mydb = myclient["mydatabase"]        # database name
mycol = mydb["customers"]            # collection name

# # insert single row
mydict = {"name": "John", "address": "Highway 37"}
ins_one = mycol.insert_one(mydict)

# # insert Multiple rows
mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]
ins_man = mycol.insert_many(mylist)

# # Find Method  or filter

# # single filter
x = mycol.find_one()

# # Show All
for x in mycol.find():
  print(x)

# # Find all using 0 and 1   0 for not show 1 for show
for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):  # ===>> Column Name
  print(x)
for x in mycol.find({}, {"address": 0, "_id": 0}):
  print(x)
# didn't work  for x in mycol.find({},{ "name": 1, "address": 0 }):
# Filter Query
myquery = {"address": "Park Lane 38"}
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)

myquery = {"address": {"$gt": "S"}}        # ===> S or higher (alphabetically) only display
myquery = {"address": {"$regex": "^S"}}      # ===> S start alphabetically only display
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x)

# # Sort And ascending and descending
mydoc = mycol.find().sort("name")          # ===> alphabetically order
mydoc = mycol.find().sort("name", -1)      # ===> descending order
mydoc = mycol.find().sort("name", 1)         # ===> descending order
for x in mydoc:
  print(x)

# # Delete Method

myquery = {"address": "Mountain 21"}
mycol.delete_one(myquery)

myquery = { "address": {"$regex": "^S"}}  # ===> start with s all delete
x = mycol.delete_many({})

# # collection drop
mycol.drop()
# # Update
myquery = {"address": "Valley 345"}
newvalues = {"$set": {"address": "Canyon 123"}}

#second 
myquery = { "address": { "$regex": "^S" } }         # ===> start with s change all
newvalues = { "$set": { "name": "Minnie" } }
x = mycol.update_many(myquery, newvalues)
mycol.update_one(myquery, newvalues)
#print "customers" after the update:
for x in mycol.find():
  print(x)

#  # limit
myresult = mycol.find().limit(5)
#print the result:
for x in myresult:
  print(x)
