"""
service to applicant object
"""
from server.models.service import service
from server.models.user import user
from google.appengine.ext import db

class serviceapplicants(db.Model):
    Service = db.ReferenceProperty(service,
                                   required=True,
                                   collection_name='user')
    Applicant = db.ReferenceProperty(user,
                                   required=True,
                                   collection_name='service')
    Date = db.DateTimeProperty()
