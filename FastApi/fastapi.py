from fastapi import FastAPI, File, UploadFile
import cv2
import uvicorn
app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):

   a =  cv2.imread(file.filename)

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')

    
    
PYTHON  API ALL

Wsgi vs Asgi  (https://www.youtube.com/watch?v=LtpJup6vcS4)

Flask  vs swagger vs fastapi

Flask 

Flask is a web framework that provides libraries to build lightweight web applications in python

It is based on WSGI toolkit and jinja2 template engine

Microframework

WSGI
The Web Server Gateway Interface (Web Server Gateway Interface, WSGI) has been used as a standard for Python web application development. WSGI is the specification of a common interface between web servers and web applications.
Werkzeug
Werkzeug is a WSGI toolkit that implements requests, response objects, and utility functions. This enables a web frame to be built on it. The Flask framework uses Werkzeg as one of its bases.
jinja2
jinja2 is a popular template engine for Python.A web template system combines a template with a specific data source to render a dynamic web page.

What is REST API (Application Programming Interface)
REST API stands for Restful API that allows integrating applications or interaction with RESTful web services. It is now growing as the most common method for connecting components in a microservice architecture. 
