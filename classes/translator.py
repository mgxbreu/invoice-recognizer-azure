from consts import service_headers, ENDPOINT
import requests

def detect_language(text):
    path = '/detect?api-version=3.0'
    constructed_url = ENDPOINT + path

    body = [{
        'text': text
    },]
    request = requests.post(constructed_url, headers=service_headers, json=body)
    response = request.json()
    response = response[0]
    language = response['language']
    return language

def translate(text, language):
    path = '/translate?api-version=3.0'
    params = f'&from={language}&to=es'
    constructed_url = ENDPOINT + path + params

    # You can pass more than one object in body.
    body = [{
        'text' : text
    }]
    request = requests.post(constructed_url, headers=service_headers, json=body)
    response = request.json()
    response = response[0]
    response = response['translations']
    response = response[0]
    response = response['text']
    return response

# print(json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': ')))