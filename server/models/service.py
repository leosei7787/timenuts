"""
service object
"""
from server.models.user import user
from server.models.skill import skill
from google.appengine.ext import db
import logging

# Data Model
class service(db.Model):
  """All the data we store for a service"""
  Title = db.StringProperty()
  Description = db.StringProperty()
  Requester =  db.ReferenceProperty(user, collection_name="requested_services")
  TimeNeeded = db.IntegerProperty()
  Skill = db.ReferenceProperty(skill, collection_name="linked_services")
  Geoloc = db.BooleanProperty()
  StartDate = db.DateTimeProperty(auto_now_add=True)
  EndDate = db.DateTimeProperty(auto_now_add=True)
  Grade = db.RatingProperty()
  Feedback  = db.StringProperty()
  Responder = db.ReferenceProperty(user, collection_name="applied_services")
  Attachments = db.StringListProperty()
  Comments = db.ListProperty(db.Key)

  #@property
  #Category = 

  def get_category(self):
    from server.models.skill import skill
    return self.Skill.Category.get()

  def to_dict(self):
      tempdict1 = {
        'Id' : self.key(),
        'Title' : getattr(self,Title),
        'Description' : getattr(self,Description),
        'Requester' : getattr(self,Requester)
      }
      return tempdict1

