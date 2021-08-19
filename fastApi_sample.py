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