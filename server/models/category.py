"""
category object, larger that skills
"""
from google.appengine.ext import db

class category(db.Model):
  Name = db.StringProperty()

