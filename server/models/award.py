"""
award object
"""
from google.appengine.ext import db

class award(db.Model):
  Name = db.StringProperty()
  
  def get_URL(self):
    return '/static/images/awards/%s.png' % self.Name
