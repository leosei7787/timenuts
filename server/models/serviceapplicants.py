"""
service to applicant object
"""
from server.models.service import service
from server.models.user import user
from google.appengine.ext import db

class serviceapplicants(db.Model):
    Service = db.ReferenceProperty(service,
                                   required=True,
                                   collection_name='users_mapping')
    Applicant = db.ReferenceProperty(user,
                                   required=True,
                                   collection_name='services_mapping')
    Date = db.DateTimeProperty()
