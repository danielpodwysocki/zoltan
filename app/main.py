#!/usr/bin/env python3
"""Example bot that returns a synchronous response."""

from flask import Flask, request, json
from modules import help

modules = [help]

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
                argument_text = event['message']['argumentText']

            command_id = event['message']['slashCommand']['commandId']
            
            text = 'You used a slash command %s' %command_id
            for m in modules:
                if str(m.Handler.id) == command_id:
                    text = m.Handler.command(argument_text) 

        else: 
            text = 'Hello, I am Zoltan, your chatbot helper. To learn about what I can do, type /help'
    else:
        return
    return json.jsonify({'text': text})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
