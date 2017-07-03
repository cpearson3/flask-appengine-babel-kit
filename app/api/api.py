# Define your API routes here

#  Import supporting libs
from flask import Flask, render_template, url_for, request, Response, jsonify
from wtforms import Form, StringField, TextAreaField, validators

import json
import logging

from .. import config

# import services and models
from .. import services
from .. import models

# Flask app app instance
app = Flask(__name__)
app.debug = True

# Set up CORS 
# Uncomment line below to enable CORS headers
# @app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', '*')
	return response

# Test Route
@app.route('/_api/hello/')
def helloWorld():

	# TODO: Better logging
	logging.warning('API Call to Hello World')

	return Response(json.dumps({
		'hello': 'world'
	}), mimetype="text/json")
