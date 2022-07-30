Important Topics



1 person viewed
FastApi  Topics (New)

5 Advance Features of FastAPI You Should Try 

All My Articles Under One Hood! 

 

Mysql python all type

Python Select from MySQL Table 

Python 

how to loop folder of files:

How to iterate over files in directory using Python? - GeeksforGeeks 


path_of_the_directory= 'tamil'
for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory,filename)
    if os.path.isfile(f):
    print(f)
python Any audio file to wav or etc

Convert MP3 to WAV - Python Tutorial 


from pydub import AudioSegment
import os

path_of_the_directory= 'tamil'a = 1for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory,filename)
    if os.path.isfile(f):
        sound = AudioSegment.from_file(f)
        a += 1        sound.export(out_f="output/new{}.wav".format(a) ,format="wav", bitrate="128k")
      
      
      

GIT comments
***************
git branch -a
git checkout remotes/origin/Chat_Bot 
git status
git commit -m “nnn”
git push origin HEAD:Chat_Bot 
git pull
	

Object Shape 
**************

https://www.google.com/search?q=opencv+shape+detection+python&ei=epgCYvflJ4G_8QOc6IKIBg&oq=opencv+shape+python&gs_lcp=Cgdnd3Mtd2l6EAMYADIGCAAQBxAeMgYIABAHEB4yBQgAEIAEMggIABAIEAcQHjIICAAQCBAHEB4yCAgAEAgQBxAeMgYIABAIEB4yBggAEAgQHjIGCAAQCBAeMgYIABAIEB46BwgAEEcQsAM6BwgAELADEEM6BwgAELEDEEM6BAgAEEM6BAgAEA1KBAhBGABKBAhGGABQ5wNY-RFg7ypoAXACeACAAWqIAbYEkgEDNS4xmAEAoAEByAEKwAEB&sclient=gws-wiz



Killer Python Automation Scripts for Daily Problems
********************************************************

https://python.plainenglish.io/10-python-automation-scripts-for-your-daily-problems-aefb502969e2

https://python.plainenglish.io/9-killer-python-automation-scripts-for-daily-problems-c1715ed42ed5


Python BEST website 

https://data-flair.training/blogs/top-python-interview-questions-answer

Python Json

https://medium.com/@alains/python-tutorial-7-advanced-features-of-the-json-library-4b5c485c75bf

Kill Comments  
***************

sudo lsof -i -P -n | grep LISTEN
sudo kill -9 738695


NOHUP
********

sudo nohup python Chat_bot_Api.py &
               
                      (OR)                

nohup python Chat_bot_Api.py & disown 
