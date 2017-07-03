#  Import supporting libs
from flask import Flask, render_template, url_for, request, jsonify

# import upload services
from .. import services

import logging

# Flask app app instance
app = Flask(__name__)

# admin controller
@app.route('/admin/')
def IndexController():

	return render_template('home.html')
