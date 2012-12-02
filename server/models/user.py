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
  Involvement = db.IntegerProperty(required = True)
  Awards = db.ListProperty(db.Key)    # To the award model
  Address = db.PostalAddress()
  
  def get_awards(self):
    """Get the list of proper awards objects"""
    from server.models.award import award
    return award.get_by_id(self.Awards)
  
  def get_skills(self):     # To the skill model
    """Generator to get the skills associated with the user"""
    from server.models.skillstouser import skillstouser
    stu = skillstouser.gql("WHERE User = :1", self).run()
    return [x.Skill for x in stu]

  def to_small_dict(self):
    """Returns a dict of minimum info about the user"""
    CHOICES = ('ForeName', 'SureName', 'ImageURL', 'TimeCredit', 'Involvement',)
    return dict(
      {'Id': self.key().id()},
      **dict(
        [(
          k,
          v.get_value_for_datastore(self)
          ) for (k, v) in self.properties().items() if k in CHOICES]
      )
    )

  def to_big_dict(self):
    """Returns a dict of all info about the user and related objects"""
    d = self.to_small_dict()
    d['Email'] = self.Email
    d['Headline'] = self.Headline
    d['Address'] = self.Address
    from server.models.award import award
    d['Awards'] = [award.get_by_id(x.id()).Name for x in self.Awards]
    return d
