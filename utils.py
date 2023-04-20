import json

def get_credentials(service):
    credentials = json.load(open('credentials.json'))
    credentials_in_service = credentials[service]
    KEY = credentials_in_service['apiKey']
    ENDPOINT = credentials_in_service['endpoint']

    return [KEY, ENDPOINT]