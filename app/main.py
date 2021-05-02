#!/usr/bin/env python3
"""Example bot that returns a synchronous response."""

from flask import Flask, request, json
from modules import help, ssh
from os import getenv
from oauth2client import client

HOST_REGEXP = getenv('HOST_REGEXP') #regexp against which all hosts for the ssh module are checked
PROJECT_NUMBER = getenv('PROJECT_NUMBER')
PRIV_KEY = getenv('PRIV_KEY')

modules = [help.Handler(), ssh.Handler(HOST_REGEXP, PRIV_KEY)]


#Values needed to verify where the request is coming from and if it's really Google
CHAT_ISSUER = 'chat@system.gserviceaccount.com'
PUBLIC_CERT_URL_PREFIX = 'https://www.googleapis.com/service_accounts/v1/metadata/x509/'
AUDIENCE = PROJECT_NUMBER


app = Flask(__name__)


@app.route('/', methods=['POST'])
def on_event():
    """Handles an event from Google Chat."""

    auth_header = request.headers.get('Authorization')
    bearer = auth_header.split("Bearer ")[1]

    #Verify the OAuth2 token, to make sure the request is coming from Google
    try:
        token = client.verify_id_token(bearer, AUDIENCE, cert_uri=PUBLIC_CERT_URL_PREFIX + CHAT_ISSUER)
        if token['iss'] != CHAT_ISSUER:
            return json.jsonify({'message':'Failed'}), 401
    except Exception as e:
        print(e)
        return json.jsonify({'message':'Failed'}), 401

    event = request.get_json()
    if event['type'] == 'ADDED_TO_SPACE' and not event['space']['singleUserBotDm']:
        text = 'Thanks for adding me to "%s"!' % (event['space']['displayName'] if event['space']['displayName'] else 'this chat')
    elif event['type'] == 'MESSAGE':
        if 'slashCommand' in event['message']:
            argument_text = None
            if 'argumentText' in event['message']:
                argument_text = event['message']['argumentText'].strip()

            command_id = event['message']['slashCommand']['commandId']
            
            text = 'You used a slash command %s' %command_id
            for m in modules:
                if str(m.id) == command_id:
                    text = m.command(argument_text)

        else:
            text = 'Hello, I am Zoltan, your chatbot helper. To learn about what I can do, type `/help`'
    else:
        return
    return json.jsonify({'text': text})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
