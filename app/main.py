#!/usr/bin/env python3
"""Example bot that returns a synchronous response."""

from flask import Flask, request, json
from modules import help, ssh
from os import getenv

HOST_REGEXP = getenv('HOST_REGEXP') #regexp against which all hosts for the ssh module are checked
PROJECT_NUMBER = getenv('PROJECT_NUMBER')


modules = [help.Handler(), ssh.Handler(HOST_REGEXP)]


#Values needed to verify where the request is coming from and if it's really Google
CHAT_ISSUER = 'chat@system.gserviceaccount.com'
PUBLIC_CERT_URL_PREFIX = 'https://www.googleapis.com/service_accounts/v1/metadata/x509/'
AUDIENCE = "" #This needs to be set to the project number of the bot


app = Flask(__name__)


@app.route('/', methods=['POST'])
def on_event():
    """Handles an event from Google Chat."""
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
