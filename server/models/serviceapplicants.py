"""
service to applicant object
"""
from models.service import service
from models.user import user
from google.appengine.ext import db

class serviceapplicants(db.Model):
    service = db.ReferenceProperty(service,
                                   required=True,
                                   collection_name='user')
    applicant = db.ReferenceProperty(user,
                                   required=True,
                                   collection_name='service')
    Date = db.DateTimeProperty()