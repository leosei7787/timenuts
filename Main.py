import webapp2
import os
from server import Routeur

app = webapp2.WSGIApplication([
                               ('/', Routeur)
                               ], debug=True)
