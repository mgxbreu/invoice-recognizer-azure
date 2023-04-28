import json
from classes.recognize_invoice import RecognizeInvoice


def get_credentials(service):
    credentials = json.load(open('credentials.json'))
    credentials_in_service = credentials[service]
    KEY = credentials_in_service['apiKey']
    ENDPOINT = credentials_in_service['endpoint']

    return [KEY, ENDPOINT]

def process_file(path):
    sample = RecognizeInvoice(path)
    sample.recognize_invoice()
    info = sample.get_info()
    print(info)
    for key in info:
        if type(info[key] ) == str:
            language = detect_language(info[key])
            info[key] = translate(info[key], language)

    data.append(info)