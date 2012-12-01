"""
award object
"""
from google.appengine.ext import db

class award(db.Model):
  name = db.StringProperty()
  
  def get_URL(self):
    return '/static/images/awards/%s.png' % self.name
