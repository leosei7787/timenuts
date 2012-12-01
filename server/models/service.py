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
  Category = db.StringListProperty()
  Geoloc = db.BooleanProperty()
  StartDate = db.DateTimeProperty()
  EndDate = db.DateTimeProperty()
  Grade = db.RatingProperty()
  Feedback  = db.StringProperty()
  Responder = db.ReferenceProperty(user)
  Attachments = db.StringListProperty()

  def get_players(self):
      Players =[]
      for playerId in self.players:
          p = PlayerManager.pull(playerId)
          Players.append( p )
      return Players
