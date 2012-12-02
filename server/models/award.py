"""
award object
"""
from google.appengine.ext import db

class award(db.Model):
  Name = db.StringProperty()
