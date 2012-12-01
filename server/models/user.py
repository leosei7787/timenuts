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
  Awards = db.ListProperty(db.Key)    # To the award model
  
  def get_awards(self):
    from models.award import award
    return award.get_by_id(self.Awards)
  
  def get_skills(self):     # To the skill model
    from models.skillstouser import skillstouser
    from models.skill import skill
    
