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
