from flask import Flask, jsonify, request
import mysql.connector
import pandas as pd
import streamlit as st
from time import time
import json, yaml

app = Flask(__name__)

# Database Connection Information
mydb = mysql.connector.connect(host="localhost", 
                               port="3306",            
                               user="root",            
                               password="root@123",            
                               database="face")
                               
# GET REQUEST 1 Method
@app.route('/get_method/', methods=['GET'])
def home():
    mydb.connect()
    if (request.method == 'GET'):
        if mydb.is_connected():
            mycursor = mydb.cursor(
            # query = "SELECT * FROM test;"            
            # df = pd.read_sql(query, mydb)            
            mycursor.execute("SELECT * FROM test;")
            df = pd.DataFrame(mycursor.fetchall())
            jsonfiles = json.loads(df.to_json(orient='records'))
            mycursor.close()
            mydb.close()
            return jsonify(jsonfiles)
        else:
            return jsonify({'data': "no"})

# GET REQUEST 2 Method
@app.route('/get_method/<int:num>', methods=['GET'])
def id_value(num):
    mydb.connect()
    if (request.method == 'GET'):
        if mydb.is_connected():
            mycursor = mydb.cursor()
            # query = f"select * from test where id='{num}';"            
            # df = pd.read_sql(query, mydb)            
            mycursor.execute(f"select * from test where id='{num}';")
            df = pd.DataFrame(mycursor.fetchall())
            jsonfiles = json.loads(df.to_json(orient='records'))
            mycursor.close()
            return jsonify(jsonfiles)
        else:
            return jsonify({'data': "no"})
# POST REQUEST Method
@app.route('/post_method/', methods=['POST'])
def mew_va():
    mydb.connect()
    if (request.method == 'POST'):
        if mydb.is_connected():
            mycursor = mydb.cursor()
            id_val = request.form.get('id_val')
            name_val = request.form.get('name_val')
            in_val = request.form.get('intime_val')
            out_val = request.form.get('outtime_val')
            sql = "INSERT INTO test (id, name, intime, outtime) VALUES (%s, %s, %s, %s)"            
            val = (id_val, name_val, in_val, out_val)
            mycursor.execute(sql, val)
            mydb.commit()
            mydb.close()
            return jsonify({'data': "sucessfully inserted"})
        else:
            return jsonify({'data': "no"})
# PUT REQUEST Method
@app.route('/put_method/', methods=['PUT'])
def put_va():
    mydb.connect()
    if (request.method == 'GET'):
        if mydb.is_connected():
            mycursor = mydb.cursor()
            id_val = request.form.get('id_val')
            name_val = request.form.get('name_val')
            in_val = request.form.get('intime_val')
            out_val = request.form.get('outtime_val')
            # sql = "INSERT INTO test (id, name, intime, outtime) VALUES (%s, %s, %s, %s)"            
            sql = "UPDATE test SET name=%s, intime=%s, outtime=%s WHERE id=%s"            
            val = (name_val, in_val, out_val, id_val)
            mycursor.execute(sql, val)
            mydb.commit()
            mydb.close()
            respone = jsonify({'data': "Employee updated successfully!"})
            respone.status_code = 200            return respone
        else:
            return jsonify({'data': "no"})
# DELETE REQUEST Method
@app.route('/del_method/<int:num>', methods=['DELETE'])
def del_value(num):
    mydb.connect()
    if (request.method == 'DELETE'):
        if mydb.is_connected():
            mycursor = mydb.cursor()
            mycursor.execute(f"DELETE FROM test WHERE id='{num}';")
            mydb.commit()
            mydb.close()
            respone = jsonify({'data': "Deleted successfully!"})
            respone.status_code = 200            return respone
        else:
            return jsonify({'data': "no"})

if _name_ == '__main__':
    app.run(debug=True)
        
              
              
# Flask Restful API

from flask import Flask, jsonify, request
import mysql.connector
import pandas as pd
import streamlit as st
from time import time
import json

app = Flask(__name__)

mydb = mysql.connector.connect(host="localhost",                               port="3306",                               user="root",                               password="root@123",                               database="face")
@app.route('/all_api/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def new_va():
    if (request.method == 'GET'):
        if not request.args.get('name'):
            mydb.connect()
            if mydb.is_connected():
                mycursor = mydb.cursor()
                mycursor.execute("SELECT * FROM test;")
                df = pd.DataFrame(mycursor.fetchall())
                jsonfiles = json.loads(df.to_json(orient='records'))
                mycursor.close()
                mydb.close()
                return jsonify(jsonfiles)
            else:
                return jsonify({'data': "no"})
        else:
            num = request.args.get('name')
            mydb.connect()
            if mydb.is_connected():
                mycursor = mydb.cursor()
                mycursor.execute(f"select * from test where id='{num}';")
                df = pd.DataFrame(mycursor.fetchall())
                jsonfiles = json.loads(df.to_json(orient='records'))
                mycursor.close()
                return jsonify(jsonfiles)
            else:
                return jsonify({'data': "no"})
    if (request.method == 'POST'):
        mydb.connect()
        if mydb.is_connected():
            mycursor = mydb.cursor()
            id_val = request.form.get('id_val')
            name_val = request.form.get('name_val')
            in_val = request.form.get('intime_val')
            out_val = request.form.get('outtime_val')
            sql = "INSERT INTO test (id, name, intime, outtime) VALUES (%s, %s, %s, %s)"            val = (id_val, name_val, in_val, out_val)
            mycursor.execute(sql, val)
            mydb.commit()
            mydb.close()
            return jsonify({'data': "sucessfully inserted"})
        else:
            return jsonify({'data': "no"})
    if (request.method == 'PUT'):
        mydb.connect()
        if mydb.is_connected():
            mycursor = mydb.cursor()
            id_val = request.form.get('id_val')
            name_val = request.form.get('name_val')
            in_val = request.form.get('intime_val')
            out_val = request.form.get('outtime_val')
            sql = "UPDATE test SET name=%s, intime=%s, outtime=%s WHERE id=%s"            val = (name_val, in_val, out_val, id_val)
            mycursor.execute(sql, val)
            mydb.commit()
            mydb.close()
            respone = jsonify({'data': "updated successfully!"})
            respone.status_code = 200            return respone
        else:
            return jsonify({'data': "no"})
    if (request.method == 'DELETE'):
        num = request.args.get('name')
        mydb.connect()
        if mydb.is_connected():
            mycursor = mydb.cursor()
            mycursor.execute(f"DELETE FROM test WHERE id='{num}';")
            mydb.commit()
            mydb.close()
            respone = jsonify({'data': "Deleted successfully!"})
            respone.status_code = 200            return respone
        else:
            return jsonify({'data': "no"})

if _name_ == '__main__':
    app.run(debug=True)
     
              
              
#  Method 2

# Flask Restful API Using from flask_restful import Resource, Api
# from flask import Flask, jsonify, request
# from flask_restful import Resource, Api

from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import mysql.connector
import pandas as pd
import streamlit as st
from time import time
import json

app = Flask(__name__)
api = Api(app)

mydb = mysql.connector.connect(
            host="localhost", port="3306",user="root",password="root@123",database="face")
# First Route
class Hello(Resource):
    def get(self):
        if not request.args.get('name'):
            mydb.connect()
            if mydb.is_connected():
                mycursor = mydb.cursor()
                mycursor.execute("SELECT * FROM test;")
                df = pd.DataFrame(mycursor.fetchall())
                jsonfiles = json.loads(df.to_json(orient='records'))
                mycursor.close()
                mydb.close()
                return jsonify(jsonfiles)
            else:
                return jsonify({'data': "no"})
        else:
            num = request.args.get('name')
            mydb.connect()
            if mydb.is_connected():
                mycursor = mydb.cursor()
                mycursor.execute(f"select * from test where id='{num}';")
                df = pd.DataFrame(mycursor.fetchall())
                jsonfiles = json.loads(df.to_json(orient='records'))
                mycursor.close()
                return jsonify(jsonfiles)
            else:
                return jsonify({'data': "no"})
    def post(self):
        mydb.connect()
        if mydb.is_connected():
            mycursor = mydb.cursor()
            id_val = request.form.get('id_val')
            name_val = request.form.get('name_val')
            in_val = request.form.get('intime_val')
            out_val = request.form.get('outtime_val')
            sql = "INSERT INTO test (id, name, intime, outtime) VALUES (%s, %s, %s, %s)"            
            val = (id_val, name_val, in_val, out_val)
            mycursor.execute(sql, val)
            mydb.commit()
            mydb.close()
            return jsonify({'data': "sucessfully inserted"})
        else:
            return jsonify({'data': "no"})
    def put(self):
        mydb.connect()
        if mydb.is_connected():
            mycursor = mydb.cursor()
            id_val = request.form.get('id_val')
            name_val = request.form.get('name_val')
            in_val = request.form.get('intime_val')
            out_val = request.form.get('outtime_val')
            sql = "UPDATE test SET name=%s, intime=%s, outtime=%s WHERE id=%s"            
            val = (name_val, in_val, out_val, id_val)
            mycursor.execute(sql, val)
            mydb.commit()
            mydb.close()
            respone = jsonify({'data': "updated successfully!"})
            respone.status_code = 200            return respone
        else:
            return jsonify({'data': "no"})
    def delete(self):
        num = request.args.get('name')
        mydb.connect()
        if mydb.is_connected():
            mycursor = mydb.cursor()
            mycursor.execute(f"DELETE FROM test WHERE id='{num}';")
            mydb.commit()
            mydb.close()
            respone = jsonify({'data': "Deleted successfully!"})
            respone.status_code = 200            return respone
        else:
            return jsonify({'data': "no"})
# Second Route
class Square(Resource):
    def get(self, num):
        return jsonify({'square': num ** 2})

api.add_resource(Hello, '/all_api/')
api.add_resource(Square, '/square/<int:num>')

if _name_ == '__main__':
    app.run(debug=True)
                
             
         
