import os
import json

def get_credentials():
    credentials_dict = {}
    exists = os.path.isfile('credentials.json')
    if exists:
        with open('credentials.json') as credentials:
            credentials_dict = json.load(credentials)
    else:
        credentials_dict['username'] = input('Please enter your username: ')
        credentials_dict['client_id'] = input('Please enter your client ID: ')
        credentials_dict['client_secret'] = input('Please enter your client secret: ')
        credentials_dict['redirect_url'] = input('Please enter your redirect url: ')
        with open('credentials.json', mode='w') as f:
            f.write(json.dumps(credentials_dict))
    return credentials_dict

