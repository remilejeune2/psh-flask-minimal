import traceback
import uuid
import sys

import flask
import flask.json
import gevent.pywsgi

from platformshconfig import Config

app = flask.Flask(__name__)
config = Config()


@app.route('/')
def root():
    return flask.json.jsonify({"hello": "world"})


if __name__ == "__main__":
    http_server = gevent.pywsgi.WSGIServer(('127.0.0.1', int(config.port)), app)
    http_server.serve_forever()
