## Overview

This tool is designed as an entrypoint to users willing to consume TheHive's audit events using webhooks. It's a Flask web application that exposes a REST API to be declared in your TheHive's `application.conf` configuration file, and will receive all the changes made on TheHive side.

Once configured, users/developers need to define their custom event handlers, by writing some Python love.

## Installation

First, start by closing the repository:

```
git clone git@github.com:TheHive-Project/TheHiveHooks.git
```

We recommend to use `virtualenv` for development:

- Start by installing `virtualenv` if you don't have it
```
pip install virtualenv
```

- Once installed access the project folder
```
cd TheHiveHooks
```

- Create a virtual environment
```
virtualenv venv
```

- Enable the virtual environment
```
source venv/bin/activate
```

- Install the python dependencies on the virtual environment
```
pip install -r requirements.txt
```

- Start the web application
```
./debug.sh
```

Once these steps are successfully done, the web application will start receiving the changes made on TheHive side, and you will see some default logs generated from the default handlers (just print the received events)

## Write you own event handlers

Following is the list of events that can listened to:

- AlertCreation
- AlertUpdate
- CaseArtifactCreation
- CaseArtifactJobCreation
- CaseArtifactJobUpdate
- CaseArtifactJobUpdate
- CaseArtifactUpdate
- CaseCreation
- CaseTaskCreation
- CaseTaskLogCreation
- CaseTaskUpdate
- CaseUpdate

To add a new event handler, developers have to add methods to the `thehive_hooks/handlers.py` file.

A handler method is as simple as the Following bit of code:

```python
@ee.on('CaseUpdate')
def caseClosed(event):
    if 'status' in event['details'] and event['details']['status'] == 'Resolved':
        app.logger.info('Case {} has been marked as resolved'.format(event['rootId']))
```

The sample above declare an event handler for `CaseUpdate` event. The code checks if the event is related to a case close action, and do some work (just logging a message in this case)

We can imaging an event handler that sends an email to some inbox once a case is closed.

Be creative, and enjoy.
