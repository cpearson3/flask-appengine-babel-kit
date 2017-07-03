import logging
from config import *

#  Import supporting libs
from flask import Flask, render_template, redirect, request

from google.appengine.api import users

# Flask app app instance
app = Flask(__name__)

# URL Routes
@app.route('/', defaults={'path': ''})
def IndexController(path):
	# Return index
	return render_template('index.html')

# Logout handler
@app.route('/logout')
@app.route('/logout/')
def LogoutController():
	return redirect(users.create_logout_url('/'))

# 404 handler	
@app.errorhandler(404)
def page_not_found(e):

	return render_template('404.html'), 404
	
# 500 handler	
@app.errorhandler(500)
def server_error(e):
	return render_template('500.html'), 500