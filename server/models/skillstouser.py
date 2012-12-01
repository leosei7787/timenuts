"""
skill to user mapping object
"""
from server.models.user import user
from server.models.skill import skill
from google.appengine.ext import db

class skillstouser(db.Model):
  Skill = db.ReferenceProperty(skill,
                               required = True,
                               collection_name = 'users_mapping')
  User = db.ReferenceProperty(user,
                              required = True,
                              collection_name = 'skills_mapping')
