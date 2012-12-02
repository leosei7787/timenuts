"""
service to applicant object
"""
from server.models.service import service
from server.models.user import user
from google.appengine.ext import db

class serviceapplicants(db.Model):
    Service = db.ReferenceProperty(service,
                                   required=True,
                                   collection_name='applicants_mapping')
    Applicant = db.ReferenceProperty(user,
                                   required=True,
                                   collection_name='services_mapping')
    Date = db.DateTimeProperty(auto_now_add = True)
    
    def to_dict(self):
        d = {
            'Id': self.key().id(),
            'Date': str(self.Date),
            'Applicant': self.Applicant.to_small_dict(),
            'Service': self.Service.to_dict()
        }
        return d
