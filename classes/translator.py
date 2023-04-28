from utils.credentials import get_credentials
import os, requests, uuid, json

KEY, ENDPOINT = get_credentials("translator")
region = 'eastus'

def detect_language(text):
    path = '/detect?api-version=3.0'
    constructed_url = ENDPOINT + path

    headers = {
        'Ocp-Apim-Subscription-Key': KEY,
        'Ocp-Apim-Subscription-Region': region,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
    body = [{
        'text': text
    },]
    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()
    response = response[0]
    language = response['language']
    return language

def translate(text, language):
    path = '/translate?api-version=3.0'
    params = f'&from={language}&to=es'
    constructed_url = ENDPOINT + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': KEY,
        'Ocp-Apim-Subscription-Region': region,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text' : text
    }]
    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()
    response = response[0]
    response = response['translations']
    response = response[0]
    response = response['text']
    return response

# print(json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': ')))