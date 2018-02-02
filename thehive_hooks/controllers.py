from flask import request
from flask import request
import json

from thehive_hooks import app
from thehive_hooks import ee

def capitalize(event_name):
    event_name = event_name.replace('_', ' ')
    return ''.join(x for x in event_name.title() if not x.isspace())

@app.route('/')
def index():
    return 'TheHiveHooks'

@app.route("/webhook", methods=['POST'])
def webhook():
    event = request.get_json()
    event_name = capitalize('{}_{}'.format(event['objectType'], event['operation']))
    app.logger.info('Emit {}: Root={}, Details={}'.format(event_name, event['rootId'], json.dumps(event['details'], sort_keys=True)))
    ee.emit(event_name, event)

    return json.dumps(event, indent=4, sort_keys=True)
