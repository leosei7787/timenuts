from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class services(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')