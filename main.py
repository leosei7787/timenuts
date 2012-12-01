from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from server.routeur import services

app = webapp.WSGIApplication([
                               ('/services', services)
                               ], debug=True)

 
def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()