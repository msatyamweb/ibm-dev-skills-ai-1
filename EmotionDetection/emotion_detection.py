# Import libraries required

import requests
import json

# Function determines the emotion

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = input_json, headers = header)
    format_response = json.loads(response.text)
    emotions = format_response['emotionPredictions'][0]['emotion']
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    max_emotion = max(emotions, key= emotions.get)
    format_emotions = {
                        'anger' : anger,
                        'disgust' : disgust,
                        'fear' : fear,
                        'joy' : joy,
                        'sadness' : sadness,
                        'max_emotion' : max_emotion
                    }
    return format_emotions



   
    
