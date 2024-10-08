'''
This module defines the function emotion_detector
to extract the sentiment in a given text
'''
import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    keys = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']

    response = requests.post(url, json = myobj, headers = headers)
    formatted_response = json.loads(response.text)

    if response.status_code == 400:
        result = {}
        for key in keys:
            result[key] = None
    else:
        result = formatted_response["emotionPredictions"][0]["emotion"]
        result['dominant_emotion'] = max(result, key=result.get)

    return result
