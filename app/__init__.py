# Application Entry Point

from main import *

# 301 Redirect *.appspot.com requests to custom domain if set
@app.before_request
def AppspotRedirect():

	if CUSTOM_DOMAIN == '':
		return
	
	domain = request.headers['Host'].split(':')[0]
	logging.warning('request host domain: ' + domain)
	
	if domain == APPENGINE_DOMAIN:
		
		redirect_url = CUSTOM_DOMAIN + request.script_root + request.path
		logging.warning('redirecting to: ' + redirect_url)

		return redirect(redirect_url, code=301)