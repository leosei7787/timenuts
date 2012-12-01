"""
comment object
"""
from models.service import service
from models.user import user
from google.appengine.ext import db
import logging

# Data Model
class comment(db.Model):
  """All the data we store for a service"""
  Comment = db.StringProperty()
  Owner =  db.ReferenceProperty(user)
  Date = db.DateTimeProperty()
 