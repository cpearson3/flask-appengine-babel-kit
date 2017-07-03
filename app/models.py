# Place Data Models

# models.py
import logging
from google.appengine.ext import ndb

# Parent model class with datatime stamp
class DateStampModel(ndb.Model):
	datetime = ndb.DateTimeProperty(auto_now_add=True)

class MyModal(DateStampModel):
	testField = ndb.StringProperty()