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



Chatbot
************

We have Two Method 


First Method


1.  https://www.youtube.com/watch?v=9KZwRBg4-P0    
2. https://github.com/Sourabhhsethii/Building-a-simple-chatbot-in-python


Second Method 

1.  https://realpython.com/python-speech-recognition/


Video link
***********

https://www.youtube.com/watch?v=SCk7onPrrwk

	MAP Document
*************************

https://towardsdatascience.com/make-beautiful-spatial-visualizations-with-plotly-and-mapbox-fd5a638d6b3c

https://towardsdatascience.com/meet-plotly-mapbox-best-choice-for-geographic-data-visualization-599b514bcd9a

Many traces on same plot in plotly express


https://stackoverflow.com/questions/60910962/is-there-any-way-to-draw-india-map-in-plotly


https://discuss.streamlit.io/t/ann-streamlit-folium-a-component-for-rendering-folium-maps/4367

MAP Document
*************************

https://towardsdatascience.com/make-beautiful-spatial-visualizations-with-plotly-and-mapbox-fd5a638d6b3c

https://towardsdatascience.com/meet-plotly-mapbox-best-choice-for-geographic-data-visualization-599b514bcd9a

Many traces on same plot in plotly express


https://stackoverflow.com/questions/60910962/is-there-any-way-to-draw-india-map-in-plotly


https://discuss.streamlit.io/t/ann-streamlit-folium-a-component-for-rendering-folium-maps/4367

	
Need to learn 
*********************


1. TensorFlow 
2. Keras
3. PyTroch
  4. Scikit-learn Python
  5. Python Pandas
  6 . NumPy Python

frame = frame[500:700, 500:1300]


Poly Line 
*********

https://stackoverflow.com/questions/57312028/problem-with-using-cv2-pointpolygontest-and-cv2-polylines


CNN MODEL  *************

IMAGE Classification 

https://www.youtube.com/watch?v=ejkRh9obVjk

https://www.youtube.com/watch?v=7MceDfpnP8k

Data Augmentation
*********************

https://machinelearningmastery.com/how-to-configure-image-data-augmentation-when-training-deep-learning-neural-networks


Method 

1. https://www.analyticsvidhya.com/blog/2021/08/image-classification-using-cnn-understanding-computer-vision/

2. https://www.analyticsvidhya.com/blog/2021/06/develop-your-first-image-classification-project-with-convolutional-neural-network/

3. https://www.analyticsvidhya.com/blog/2021/01/image-classification-using-convolutional-neural-networks-a-step-by-step-guide/



Pre-Training Model

https://www.analyticsvidhya.com/blog/2020/08/top-4-pre-trained-models-for-image-classification-with-python-code/



Data Science Step 
*******************

df = pd.read_csv('Iris.csv')

df.info()

df.isnull().sum()

df.shape()

df[‘ibm’] .describe()

df[‘ibm’].fillna(df[‘ibm’].mean())

            Or

df[‘ibm’].dropna(df[‘ibm’].mean())




Dlib_Model
******************


https://programmer.help/blogs/face-recognition-dlib-python-version.html

https://towardsdatascience.com/step-by-step-face-recognition-code-implementation-from-scratch-in-python-cc95fa041120

https://github.com/susantabiswas/FaceRecog

https://www.geeksforgeeks.org/python-multiple-face-recognition-using-dlib/

Face Detector HOG & CNN
*****************************

https://learnopencv.com/face-detection-opencv-dlib-and-deep-learning-c-python/

https://towardsdatascience.com/cnn-based-face-detector-from-dlib-c3696195e01c

https://livecodestream.dev/post/detecting-face-features-with-python/


Folder Looping
*****************



for directory in os.listdir('images'):
    for file in os.listdir(os.path.join('images', directory)):
        img_path = os.path.join('images', directory, file)
        img = cv2.imread(img_path)
GOOGLE COLAB  *****************



How to unzip file in colab 

1.  !unzip -q "/content/gdrive/My Drive/dataset.zip"

  2.  !tar -xf lfw.tgz

How to Delete folder or file in colab 

https://www.codegrepper.com/code-examples/python/delete+non+empty+directory+python

1. import os
2. import shutil
3. os.remove('/your/path/to/file.txt') #removes a file.
4. os.rmdir('/your/folder/path/') #removes an empty directory.
5. shutil.rmtree('/your/folder/path/') #deletes a directory and all its contents.



