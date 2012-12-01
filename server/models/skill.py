"""
skill object
"""
from google.appengine.ext import db

class skill(db.Model):
  Name = db.StringProperty()

  def get_image_URL(self):
    return '/static/img/skills/%s.png' % self.Name
