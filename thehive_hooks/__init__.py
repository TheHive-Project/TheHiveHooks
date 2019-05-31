from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
from pyee import EventEmitter

# Declare the logger
app_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
pathLog = app_dir + '/thehive-hooks.log'
handler = RotatingFileHandler(pathLog, maxBytes=10000000, backupCount=1)
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
))


# Initialize the app
app = Flask(__name__)
app.logger.addHandler(handler)
app.url_map.strict_slashes = False

## Declare the event emitter
ee = EventEmitter()

import thehive_hooks.controllers
import thehive_hooks.handlers
