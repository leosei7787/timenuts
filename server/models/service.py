"""
service object
"""
from models.user import user
from google.appengine.ext import db
import logging

# Data Model
class service(db.Model):
  """All the data we store for a service"""
  Title = db.StringProperty()
  Description = db.StringProperty()
  Requester =  db.ReferenceProperty(user)
  TimeNeeded = db.IntegerProperty()
  Category = db.ListProperty(db.key)    # List of skills
  Geoloc = db.BooleanProperty()
  StartDate = db.DateTimeProperty()
  EndDate = db.DateTimeProperty()
  Grade = db.RatingProperty()
  Feedback  = db.StringProperty()
  Responder = db.ReferenceProperty(user)
  Attachments = db.StringListProperty()
  Comments = db.ListProperty(db.key)

  def get_categories(self):
    from models.skill import skill
    for skillId in self.Category:
        yield skill.get_by_key_name(skillId)
