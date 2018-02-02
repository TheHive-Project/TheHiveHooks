import json
from thehive_hooks import app
from thehive_hooks import ee

def make_handler_func(event_name):
    @ee.on(event_name)
    def _handler(event):
        app.logger.info('Handle {}: Event={}'.format(event_name, json.dumps(event, indent=4, sort_keys=True)))

    return _handler

events = [
    'AlertCreation',
    'AlertUpdate',
    'CaseArtifactCreation',
    'CaseArtifactJobCreation',
    'CaseArtifactJobUpdate',
    'CaseArtifactJobUpdate',
    'CaseArtifactUpdate',
    'CaseCreation',
    'CaseTaskCreation',
    'CaseTaskLogCreation',
    'CaseTaskUpdate',
    'CaseUpdate'
]

for e in events:
    make_handler_func(e)

# Sample handler for case closing
@ee.on('CaseUpdate')
def caseClosed(event):
    if 'status' in event['details'] and event['details']['status'] == 'Resolved':
        app.logger.info('Case {} has been marked as resolved'.format(event['rootId']))
