import pickle
import numpy as np
import json
import random
from tensorflow.keras.models import load_model
import nltk
from inltk.inltk import tokenize
from fastapi import FastAPI, File, UploadFile,APIRouter
from pydantic import BaseModel


class Item(BaseModel):
    my_value: str

# app = FastAPI()
nolroute = APIRouter()

model = load_model('Chatbot_Tamil.h5')

intents = json.loads(open('intents_tamil.json').read())
words = pickle.load(open('words_tamil.pkl', 'rb'))
classes = pickle.load(open('classes_tamil.pkl', 'rb'))

def clean_up_sentence(sentence):
    word = tokenize(sentence, "ta")
    sentence_words = []
    for w in word:
        sentence_words.append(w)
    return sentence_words

def bag_of_words(sentence, words, show_details=True):
    # tokenizing patterns
    sentence_words = clean_up_sentence(sentence)
    # bag of words - vocabulary matrix
    bag = [0]*len(words)
    for s in sentence_words:
        # print(s)
        for i,word in enumerate(words):
            if word == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % word)
    # print(np.array((bag)))
    return(np.array(bag))

def predict_class(sentence):
    # filter below  threshold predictions
    p = bag_of_words(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sorting strength probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    # print(return_list)
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result


# ints = predict_class("வணக்கம்")
# res = getResponse(ints, intents)
# print(res)
@nolroute.post("/Tamil_chatbot_text")
async def analyze_route(input:Item):
    try:
        res = input.my_value
        ints = predict_class(res)
        res = getResponse(ints, intents)

        return {"result":res}
    except Exception as e:
        return {"Success": "false", "Result":str(e) }

