from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app

class services(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')
        
        
class newuser(webapp.RequestHandler):
    def get(self):
        
        #Email = users.get_current_user().nickname()
        #user.gql("SELECT * FROM user where Email= :Email",Email=Email)
        
        user= user(  ForeName = "Leo",
                    SureName = "Sei",
                    Email = "sei7787@gmail.com",
                    ImageURL = "http://google.fr",
                    Headline = "Awesomness",
                    TimeCredit = 1000,
                    Involvment = 1000
                    )
        user.put()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('added!')