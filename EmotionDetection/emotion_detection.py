import requests
import json

def process_response(response):
    json_response = json.loads(response.text)

    output_dict = {
        'anger': json_response['emotionPredictions'][0]['emotion']['anger'],
        'disgust': json_response['emotionPredictions'][0]['emotion']['disgust'],
        'fear': json_response['emotionPredictions'][0]['emotion']['fear'],
        'joy': json_response['emotionPredictions'][0]['emotion']['joy'],
        'sadness': json_response['emotionPredictions'][0]['emotion']['sadness'],
    }

    max_score = 0
    dominant_emotion = None
    for key, value in output_dict.items():
        if value > max_score:
            max_score = value
            dominant_emotion = key

    output_dict.update({ 'dominant_emotion': dominant_emotion})

    return output_dict

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    if response.status_code == 400:
        output =  {        
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
        }
    else:
        output = process_response(response)

    return output