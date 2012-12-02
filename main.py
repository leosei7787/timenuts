from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from server.routeur import *



app = webapp.WSGIApplication([
                               ('/', index), 
                               ('/data/services', services), 
                               ('/data/skills', skills),
                               ('/data/me', myuserview),
                               ('/data/user', userview),
                               ('/login', login),
                               ('/logout', logout),
                               ('/filltable',filltable)
                               ], debug=True)

 
def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()
