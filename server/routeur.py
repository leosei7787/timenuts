from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app

class services(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')
        
        
class newuser(webapp.RequestHandler):
    def get(self):
        
        Email = users.get_current_user().email()
        #user.gql("SELECT * FROM user where Email= :Email",Email=Email)
        
        
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello '+Email+'!')