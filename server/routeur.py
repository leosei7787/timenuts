from google.appengine.ext import webapp
from google.appengine.api import users
from models.user import user
from google.appengine.ext.webapp.util import run_wsgi_app
import random

class services(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')
        
        
class newuser(webapp.RequestHandler):
    def get(self):
        Names = ['Pierre','Paul','Thomas','Francois','Steve','Vincent','Etienne','Larry']
        SurNames = ['A','B','C','D','E','F','G']
        Name = Names[ random.randint(0,len(Names)) ]
        SurName = SurNames[ random.randint(0,len(SurNames)) ]
        Email = Name+'.'+SurName+'@gmail.com'
        q = user.gql('WHERE Email=\''+Email+'\'')
        if q.count() == 0:
            u= user(ForeName = Name,
                    SureName = SurName,
                    Email = Email,
                    ImageURL = 'http://google.fr',
                    Headline = 'Awesomness',
                    TimeCredit = random.randint(0,10),
                    Involvment = random.randint(0,1000),
                    Awards = []
                    )
            u.put()
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.out.write('added!' + Email)
        else:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.out.write('Already exists!' + Email)