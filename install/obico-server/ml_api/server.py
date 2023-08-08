#!/usr/bin/env python

import flask
from flask import request, jsonify
from os import path, environ
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
import cv2
import numpy as np
import requests

from auth import token_required
from lib.detection_model import load_net, detect

THRESH = 0.08  # The threshold for a box to be considered a positive detection
SESSION_TTL_SECONDS = 60*2

# Sentry
if environ.get('SENTRY_DSN'):
    sentry_sdk.init(
        dsn=environ.get('SENTRY_DSN'),
        integrations=[FlaskIntegration(), ],
    )

app = flask.Flask(__name__)

# SECURITY WARNING: don't run with debug turned on in production!
app.config['DEBUG'] = environ.get('DEBUG') == 'True'

model_dir = path.join(path.dirname(path.realpath(__file__)), 'model')
net_main, meta_main = load_net(path.join(model_dir, 'model.cfg'), path.join(model_dir, 'model.weights'), path.join(model_dir, 'model.meta'))

@app.route('/p/', methods=['GET'])
@token_required
def get_p():
    if 'img' in request.args:
        try:
            resp = requests.get(request.args['img'], stream=True, timeout=(0.1, 5))
            resp.raise_for_status()
            img_array = np.array(bytearray(resp.content), dtype=np.uint8)
            img = cv2.imdecode(img_array, -1)
            detections = detect(net_main, meta_main, img, thresh=THRESH)
            return jsonify({'detections': detections})
        except:
            sentry_sdk.capture_exception()
    else:
        app.logger.warn("Invalid request params: {}".format(request.args))

    return jsonify({'detections': []})

@app.route('/hc/', methods=['GET'])
def health_check():
    return 'ok'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3333, threaded=False)
