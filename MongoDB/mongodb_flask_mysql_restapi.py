import pymongo
from flask import Flask, jsonify, request
import json
from bson.json_util import dumps

app = Flask(__name__)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]        # database name
mycol = mydb["customers"]            # collection name

@app.route('/all_api/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def new_va():
    if (request.method == 'GET'):
        if not request.args.get('name'):
            result = [x for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1})]
            return jsonify({"News": result})
        else:
            num = request.args.get('name')
            mydoc = mycol.find({"name": num}, {"_id": 0, "name": 1, "address": 1})
            result = [x for x in mydoc]
            return jsonify({"News": result})
    if (request.method == 'POST'):
        name_val = request.form.get('name')
        add_val = request.form.get('address')
        mydict = {"name": name_val, "address": add_val}
        mycol.insert_one(mydict)
        return jsonify({"News": "Inserted Successfully"})
    if (request.method == 'PUT'):
        name_val = request.form.get('name')
        add_val = request.form.get('address')
        mydoc = mycol.find({"name": name_val}, {"_id": 0, "name": 1, "address": 1})
        result = [x for x in mydoc]
        myquery = {"name": result[0]['name'], "address": result[0]['address']}
        newvalues = {"$set": {"name": name_val, "address": add_val}}
        mycol.update_one(myquery, newvalues)
        return jsonify({"News": "Updated Successfully"})
    if (request.method == 'DELETE'):
        num = request.args.get('name')
        myquery = {"name": num}
        mycol.delete_one(myquery)
        return jsonify({"News": "Deleted Successfully"})

if _name_ == '__main__':
    app.run(debug=True)
