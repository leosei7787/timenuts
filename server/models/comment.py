"""
comment object
"""
from server.models.service import service
from server.models.user import user
from google.appengine.ext import db
import logging

# Data Model
class comment(db.Model):
  """All the data we store for a service"""
  Comment = db.StringProperty()
  Owner =  db.ReferenceProperty(user)
  Date = db.DateTimeProperty(auto_now_add=True)
 
	def to_dict(self):
		tempdict1 = {
        "Id": self.key().id(),
        "Comment": self.Comment,
        "Owner": {
        	"Type":"Small",
        	"User" : self.Owner.to_small_dict()
        },
        "Date" : self.Date.strftime("%Y-%m-%d %H:%M:%S")