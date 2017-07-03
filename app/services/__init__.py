# Example Data Store Service Module
# Services are namespaces for Data Store getters and setters

from google.appengine.ext import ndb
from .. import models

import json
import logging

class DataStoreService:
    # Gets all data store objects from given class
    def GetAll(self, ndbClass):
    	results = None
    	
    	try:
    		# build result list
    		result = []
    		# get all, order by datetime
    		query = ndbClass.query().order(-ndbClass.datetime)
    		for i in query.iter():
    			obj = {
    				'key': i.key.urlsafe(),
    				'data': i.data,
    				'formID': i.formID,
    				'datetime': i.datetime
    			}
    			result.append(obj)
    
    		return result
    
    	except Exception as e:
    		# handle error on get
    		logging.warning('FormService.GetAll error: ' + str(e))
    		return None
    
    # Delete Method
    def Delete(self, key):
    	try:
    		# get by key
    		i =  ndb.Key(urlsafe=key).get()
    		
    		i.key.delete()
    		
    		return True
    
    	except Exception as e:
    		# handle error on get
    		logging.warning('Delete Method error: ' + str(e))
    		return None
    		
    # get by key
    def Get(self, key):
    	return None
    
    # Save Method
    def Save(sef, data):
    	return None
