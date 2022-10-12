import traceback
import uuid
import sys

import flask
import flask.json

app = flask.Flask(__name__)

@app.route('/')
def root():
    return flask.json.jsonify({"hello": "world"})