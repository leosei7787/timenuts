"""
user object
"""
from google.appengine.ext import db

class user(db.Model):
  ForeName = db.StringProperty()
  SureName = db.StringProperty()
  Email = db.EmailProperty(required = True)
  ImageURL = db.LinkProperty()
  Headline = db.StringProperty()
  TimeCredit = db.IntegerProperty(required = True)
  Involvment = db.IntegerProperty(required = True)
  Awards = db.ListProperty(db.key)    # To the award model
  
  def get_awards(self):
    from models.award import award
    #Awards = []
    for AwardId in self.Awards:
      yield award.get_by_key_name(AwardId)
  
  #def get_skills(self):     # To the skill model
    
