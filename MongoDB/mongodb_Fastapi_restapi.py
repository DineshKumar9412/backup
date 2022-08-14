import pymongo
import uvicorn
from typing import List
from fastapi import FastAPI, Form
import pandas as pd
import json

app = FastAPI()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]        # database name
mycol = mydb["customers"]            # collection name

@app.get("/get_method/{num}")
async def get_met(num: str):
    mydoc = mycol.find({"name": num}, {"_id": 0, "name": 1, "address": 1})
    result = [x for x in mydoc]
    return {"News": result}

@app.get("/get_method/")
async def get_met():
    result = [x for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1})]
    return {"News": result}

@app.post("/post_form/")
async def post_method(name_val: str = Form(), add_val: str = Form()):
    mydict = {"name": name_val, "address": add_val}
    mycol.insert_one(mydict)
    return {"News": "Inserted Successfully"}

@app.put("/put_method/{id_val}")
async def update_item(id_val: str, add_val: str = Form()):
    mydoc = mycol.find({"name": id_val}, {"_id": 0, "name": 1, "address": 1})
    result = [x for x in mydoc]
    myquery = {"name": result[0]['name'], "address": result[0]['address']}
    newvalues = {"$set": {"name": id_val, "address": add_val}}
    mycol.update_one(myquery, newvalues)
    return {'data': "updated successfully!"}

@app.delete("/del_method/{id_val}")
async def delete_item(id_val: str):
    myquery = {"name": id_val}
    mycol.delete_one(myquery)
    return {"News": "Deleted Successfully"}

if _name_ == '__main__':
    uvicorn.run('Fastapi_mongodb:app', debug=True, reload=True)
