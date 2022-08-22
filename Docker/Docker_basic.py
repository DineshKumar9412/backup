docker used for ready made package

docker install step:

reference link :-

https://phoenixnap.com/kb/install-docker-on-ubuntu-20-04 

steps:

sudo apt update

sudo apt-get install apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu  $(lsb_release -cs)  stable"

sudo apt update

sudo apt-get install docker-ce

docker --version

sudo systemctl start docker

sudo systemctl status docker



create a Dockerfile

FROM python:3.9 #your version
ADD voice_doc.py . #your python file 
ADD requirements.txt .#your installed packeges
RUN pip install -r requirements.txt # run all libraries
CMD  [ "python", "./voice_doc.py" ] 

RUN apt-get update ##[edited]


with WORKDIR

FROM python:3.9 #your version
WORKDIR /voice  #inside of all files

RUN pip install -r requirements.txt # run all libraries
CMD  [ "python", "./voice_doc.py" ] 

RUN apt-get update ##[edited]




Create docker image

docker build -t “imagename “ ..(dot is important)

ex:-

docker build -t voice .

run your docker images

docker run voice

Docker hub Register

go to docker hub official page https://hub.docker.com/  register Now

ex:

id : oasys2022

email : oasys@gmail.com

password: oasys@123

Create repository name

ex:oasys2022/voice_to_text

Then tag your image to docker hub 

docker tag imagename oasys2022/voice_to_text:first   ==>first is a tag name 

Then push your image in docker hub

docker push  oasys2022/voice_to_text:first

pull your docker and run

docker pull  oasys2022/voice_to_text:first

docker run -p 8000:8000 be80889572bc(image id)



Reduce_size docker image:

referense link:

https://blog.devgenius.io/building-smaller-docker-images-the-right-way-1b6c12c112e1 



first your create new file in pycharm.

file name is  Dockerfile.alpine-multi-stage



FROM python:3-alpine as builder 

ENV PATH="/opt/venv/bin:${PATH}"
COPY req.txt  /u01/req.txt
RUN \
  apk add build-base && \
  python -m venv /opt/venv && \
  pip install -r /u01/req.txt

FROM python:3-alpine
COPY .  /u01
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}"
EXPOSE 8080
WORKDIR /u01
ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:8080", "wsgi:app" ]



create new python file  

file name is wsgi .py 

also  requirements.txt

from flask import Flask

app = Flask(__name__)
@app.route('/')
def basic_route():
  return 'welcome to docker';

if __name__ == '__main__':
  app.run()

Build the docker image:

sudo docker build -t ddirect:alpine-multi-stage -f Dockerfile.alpine.multi-stage  . --no-cache

Run the docker image :

sudo docker run -p 8080:8080 76db01515bbf # image id


Tag the image into dockerhub :

sudo docker tag imagename oasys2022/voice_to_text:Reduce

push the image in docker hub:

docker push  oasys2022/voice_to_text:reduce

Pull the image into local:

docker pull  oasys2022/voice_to_text:reduc

Run the docker image:

sudo docker run -p 8080:8080 24947ae8bbfc

Delete the all docker images

sudo docker system prune -a







***Alpine is not supported in more packages So i move to docker slim its working fine***

referense link :-https://towardsdatascience.com/how-to-build-slim-docker-images-fast-ecc246d7f4a7

step 1:

createa folder app or any name inside of your environment

step 2:

create a python  file inside of app folder like ,hims_voice.py

import uvicorn
import speech_recognition as sr
from fastapi import FastAPI, File, UploadFile

r = sr.Recognizer()
app = FastAPI()

@app.post("/voice")
async def analyze_route(file : UploadFile = File(...)):
    try:
        a = file.file
        with sr.AudioFile(a) as source:
            audio_text = r.listen(source)
            text = r.recognize_google(audio_text)

            return {"result":text}
    except Exception as e:
        return {"Success": "false", "Result":str(e) }


if __name__ == '__main__':
    uvicorn.run('hims_voice:app', port=8009, host='0.0.0.0',reload=True,debug=True)
# https://github.com/docker-library/python/issues/546

step 3

create a requirements.txt (Every needed packages)

anyio==3.5.0
asgiref==3.5.0
click==8.0.3
fastapi==0.73.0
h11==0.13.0
idna==3.3
pydantic==1.9.0
python-multipart==0.0.5
six==1.16.0
sniffio==1.2.0
SpeechRecognition==3.8.1
starlette==0.17.1
typing_extensions==4.1.1
uvicorn==0.17.5

step 4

create a Dockerfile 

FROM python:3.8.0-slim
COPY . /app
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean
WORKDIR app
RUN pip install --user -r requirements.txt
CMD [ "python", "hims_voice.py" ]



step 5

sudo docker build -t hims_voice:user_wav .

step 6 

sudo docker images

step 7

sudo docker run -p 8009:8009 ca686323b288(image id)

step 8

sudo docker  tag  f291877c9bdd moorthy1417/slim_hims:final_hims

step 9

sudo docker push   moorthy1417/slim_hims:final_hims

step 10

sudo docker pull moorthy1417/slim_hims:final_hims

Final

sudo docker run -p 8009:8009 ca686323b288(image id)
