# import secrets
# df = secrets.token_hex(16)
#
# print(df)
# import time
# from typing import Dict
# import jwt
# from decouple import config
#
#
# JWT_SECRET = config("secret")
# JWT_ALGORITHM = config("algorithm")
#
# payload = {
#         "user_id": "Hmis_Voice_to_text",
#         "password":"HMIS!@h6m4",
#     }
# token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
#
# print(token)
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiSG1pc19Wb2ljZV90b190ZXh0IiwicGFzc3dvcmQiOiJITUlTIUBoNm00In0.cjd1uF8AtErIBQVnma3-gFlv68trCxckBIdZyHo9a5Q



from fastapi import FastAPI, File, UploadFile,Form
import uvicorn
import jwt
from decouple import config
from pydantic import BaseModel
import speech_recognition as sr
r = sr.Recognizer()

class Item(BaseModel):
    my_value: str = None

class na_item(BaseModel):
    u_name:str
    pas_wo:str

app = FastAPI()


@app.post("/sing_up")
async def analyze_route(to_val:na_item):
    try:
          name = to_val.u_name
          pas = to_val.pas_wo
          payload = {
                      "user_id": name,
                      "password": pas,
                  }

          JWT_SECRET = config("secret")
          JWT_ALGORITHM = config("algorithm")
          Hmis_token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

          return {"result": Hmis_token}
    except Exception as e:
        return {"Success": "false", "Result":str(e) }


@app.post("/uploadfile/", status_code=201)
async def create_upload_file(my_value: str = Form(...), file: UploadFile = File(...)):

    try:
        token_va = Item(my_value= my_value)
        token = token_va.my_value
        JWT_SECRET = config("secret")
        JWT_ALGORITHM = config("algorithm")
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        if decoded_token :
            files = file.file
            with sr.AudioFile(files) as source:
                audio_text = r.listen(source)
                text = r.recognize_google(audio_text)
        return {"result": text}
    except Exception as e:
        return {"Success": "false", "Result":str(e) }
if __name__ == '__main__':
    uvicorn.run('Tocken_api:app', port=8006, host='0.0.0.0',reload=True,debug=True)
# # # decoded_token = jwt.decode(ds, JWT_SECRET, algorithms=[JWT_ALGORITHM])
# #
# # print(decoded_token)


# def token_response(token: str):
#     return {
#         "access_token": token
#     }
#
# def signJWT(user_id: str) -> Dict[str, str]:
#     payload = {
#         "user_id": user_id,
#         "expires": time.time() + 600
#     }
#     token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
#
#     return token_response(token)
#
# def decodeJWT(token: str) -> dict:
#     try:
#         decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
#         return decoded_token if decoded_token["expires"] >= time.time() else None
#     except:
#         return {}


#
# payload = {
#         "user_id": "Hmis_Voice_to_text",
#         "password":"HMIS!@h6m4",
#     }
# token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
#
# # print(token)
#
# decoded_token = jwt.decode(no, JWT_SECRET, algorithms=[JWT_ALGORITHM])
#
# print(decoded_token)
#
# # eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiSG1pc19Wb2ljZV90b190ZXh0IiwicGFzc3dvcmQiOiJITUlTIUBoNm00In0.cjd1uF8AtErIBQVnma3-gFlv68trCxckBIdZyH
# #"user_id": "Hmis_Voice_to_text",
#      #   "password":"HMIS!@h6m4",
#
# # def token_response(token: str):
# #     return {
# #         "access_token": token
# #     }
# #
# # def signJWT(user_id: str) -> Dict[str, str]:
# #     payload = {
# #         "user_id": user_id,
# #         "expires": time.time() + 600
# #     }
# #     token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
# #
# #     return token_response(token)
#
# # def decodeJWT(token: str) -> dict:
# #     try:
# #         decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
# #         return decoded_token if decoded_token["expires"] >= time.time() else None
# #     except:
# #         return {}
#
# from fastapi import FastAPI, File, UploadFile,Form
# from pydantic import BaseModel
# import uvicorn
#
# app = FastAPI()
#
#
# class Properties(BaseModel):
#     language: str = None
#     author: str = None
#
#
# @app.post("/uploadfile/", status_code=201)
# async def create_upload_file(language: str = Form(...),author: str = Form(...),file: UploadFile = File(...)):
#
#     return {"filename": file.filename, 'properties': Properties(language=language,author=author)}
#
#
# if __name__ == '__main__':
#     uvicorn.run('Tocken_api:app', port=8001, host='0.0.0.0',reload=True,debug=True)
