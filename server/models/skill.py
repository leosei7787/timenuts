"""
skill object
"""
from google.appengine.ext import db
from server.models.category import category

class skill(db.Model):
  Name = db.StringProperty()
  Category = db.ReferenceProperty(category,
                                  required = True)
