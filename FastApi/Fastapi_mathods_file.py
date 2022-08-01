Basic Code 


from fastapi import FastAPI, File, UploadFile
import uvicorn
app = FastAPI()

@app.post("/chatbot_text")
async def analyze_route(input:str):
    try:
          res = input
          return {"result":res}
    except Exception as e:
        return {"Success": "false", "Result":str(e) }
if __name__ == '__main__':
    uvicorn.run('fast_face:app', port=8001, host='0.0.0.0',reload=True,debug=True)
 

GET Single File command


from fastapi import FastAPI, File, UploadFile
import uvicorn
app = FastAPI()

@app.post("/chatbot_text")
async def analyze_route(file : UploadFile = File(...)):
      try:
          res = file
          contents = await res.read()
          nparr = np.fromstring(contents, np.uint8)
          img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
 

GET Multiple File Or List of File


from fastapi import FastAPI, File, UploadFile
import uvicorn
app = FastAPI()

@app.post("/chatbot_text")
async def analyze_route(files: List[UploadFile] = File(...)):
      try:
          res = files
          contents = await res.read()
          nparr = np.fromstring(contents, np.uint8)
          img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
 

GET Video File  or Wav File 


from fastapi import FastAPI, File, UploadFile
import uvicorn
app = FastAPI()

@app.post("/chatbot_text")
async def analyze_route(file : UploadFile = File(...)):
      try:
          res = files.file
 

Web Security (Did not display the value in our api hit) log


#https://fastapi.tiangolo.com/tutorial/body/

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    
app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    df = item.name
 

Web Security Token     **************


#https://fastapi.tiangolo.com/tutorial/security/first-steps/

from fastapi import FastAPI
from pydantic import BaseModel

 

Web Security Token JWT(JSON Web Tokens)

In our env first we create a .env file 

how to create a secret key 


import secrets
df = secrets.token_hex(16)# how many you want ex: secrets.token_hex(25) its create a key
print(df)
in that .env file we add two values   ex:


secret = ca88f10711ec297152dce765b2e8404b
algorithm = HS256
First we need to create a jwt token so

pip install python-decouple

pip install PyJWT


import time
from typing import Dict
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

payload = {
        "user_id": "Hmis_Voice_to_text", 
        "password":"HMIS!@h6m4",    }
token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

print(token)
Now we created The Token.   

we need to compare or check is it correct so 


import time
from typing import Dict
import jwt
from decouple import config

token = eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiSG1pc19Wb2ljZV90b190ZXh0IiwicGFzc3dvcmQiOiJITUlTIUBoNm00In0.cjd1uF8AtErIBQVnma3-gFlv68trCxckBIdZyHo9a5Q
# this is my token

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")
decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
print(decoded_token)
FastApi. Document Details 

Basic code

 


from fastapi import FastAPI, File, UploadFile
import uvicorn
app = FastAPI()

@app.post("/chatbot_text")
async def analyze_route(input:str):
    try:
          a = input
          return {"result":a}
    except Exception as e:
        return {"Success": "false", "Result":str(e) }
if __name__ == '__main__':
    uvicorn.run('fast_face:app', port=8001, host='0.0.0.0',reload=True,debug=True)
 

Uvicon.Run “File_Name”(your python file) ex fast_face:app (fast_face is my file name)

 

String value (single)

 async def analyze_route(input:str):

async def analyze_route(input:str, fgg:float): 

 

String value (Multiple )

Query Parameters and String Validations - FastAPI 
https://fastapi.tiangolo.com/tutorial/query-params-str-validations/

async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50)):

 

Single File Reading

async def analyze_route(file : UploadFile = File(...)):

contents = await file.read()

print(contents)

Multiple File Reading

async def analyze_route(files: List[UploadFile] = File(...)):

for img in files:
contents = await img.read()
nparr = np.fromstring(contents, np.uint8)
img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

 

How to Read Image file 
async def analyze_route(file : UploadFile = File(...)):

contents = await file.read()
nparr = np.fromstring(contents, np.uint8)
img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

 

How to Read wav File  (Or) Video File
async def analyze_route(intte : UploadFile = File(...)):

filenae = intte.file

print(filenae)

BaseModel

How to upload both file and JSON data using FastAPI? 
https://stackoverflow.com/questions/70535711/error-in-multipart-form-data-request-using-pydantic-basemodel-in-fastapi

What are the advantages of using Depends in FastAPI over just calling a dependent function/class? 
https://stackoverflow.com/questions/61871147/what-are-the-advantages-of-using-depends-in-fastapi-over-just-calling-a-dependen

How to add both file and JSON body in a FastAPI POST request? 
https://stackoverflow.com/questions/65504438/how-to-add-both-file-and-json-body-in-a-fastapi-post-request/70640522#70640522

Api Security In FastApi:

how not to show critical information in api logs


from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    my_value: str


@app.post("/text")
async def analyze_route(input:Item):
    try:
        res = input.my_value
        return {"result":res}
    except Exception as e:
        return {"Success": "false", "Result":str(e) }

if __name__ == '__main__':
    uvicorn.run('chat_bot_api:app', port=9005, host='0.0.0.0',reload=True,debug=True)
    
  
 

Api Token In FastApi using JWT (Securing FastAPI with JWT Token-based Authentication )
https://testdriven.io/blog/fastapi-jwt-auth/

step1:

first we need to create a .env file in ower env 

into the file we give


secret_key = hdbkjsdmjskbjhdjhjdhjdhfjdgjd
algorithm = HS256
how to create secret key in python using


import os
import binascii
key = binascii.hexlify(os.urandom(24))
print(key)
                                                                         (OR)      (2 is best)


import secrets
df = secrets.token_hex(16)
print(df)
 

pip install PyJWT==1.7.1 python-decouple==3.3

Code


import time
from typing import Dict
import jwt
from decouple import config


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

payload = {
        "user_id": "Hmis_Voice_to_text","password":"HMIS!@h6m4"}
token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])

print(decoded_token)
