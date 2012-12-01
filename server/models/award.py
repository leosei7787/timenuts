"""
award object
"""
from google.appengine.ext import db

class award(db.Model):
  Name = db.StringProperty()
  
  def get_image_URL(self):
    return '/static/img/awards/%s.png' % self.Name
