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
    from server.models.award import award
    return award.get_by_id(self.Awards)
  
  def get_skills(self):     # To the skill model
    """Generator to get the skills associated with the user"""
    from server.models.skillstouser import skillstouser
    stu = skillstouser.gql("WHERE User = :1", self).run()
    return [x.Skill for x in stu]
