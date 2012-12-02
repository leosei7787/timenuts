"""
service object
"""
from server.models.user import user
from server.models.skill import skill
from server.models.category import category
from google.appengine.ext import db
import logging
import datetime

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
  Applicants = db.ReferenceProperty(user, collection_name="applied_services")
  Responder = db.ReferenceProperty(user, collection_name="responded_service")
  Attachments = db.StringListProperty()
  Comments = db.ListProperty(db.Key)
  CreatedTime = db.DateTimeProperty(auto_now_add=True)
  ModifiedTime = db.DateTimeProperty(auto_now_add=True)

  #@property
  #Category = 

  def get_category(self):
    return self.Skill.Category.get()

  def to_dict(self):
      tempdict1 = {
        "Id": self.key().id(),
        "Title": self.Title,
        "Description": self.Description,
        "Category" : self.Skill.Category.Name,
        "Skill" : self.Skill.Name,
        "StartDate" : self.StartDate.strftime("%Y-%m-%d %H:%M:%S"),
        "EndDate" : self.EndDate.strftime("%Y-%m-%d %H:%M:%S"),
        "Requester": {
          "Type":"Small",
          "User":self.Requester.to_small_dict()
          },
        "Grade" : self.Grade,
        "TimeNeeded": self.TimeNeeded,
        "Done" : "false",
        "Feedback":self.Feedback,
        "CreatedTime":self.CreatedTime.strftime("%Y-%m-%d %H:%M:%S"),
        "ModifiedTime" :self.ModifiedTime.strftime("%Y-%m-%d %H:%M:%S"),
        "Address" : self.Requester.Address,
        "Icons":{
          "Geoloc": "True" if self.Requester.Address else "False" ,
          "Friends" :  "True",
          "Time": "True" if (self.EndDate - self.StartDate) < datetime.timedelta(days=7) else "False",
          "FriendsofFriends":"False"

        }
      }
      return tempdict1

