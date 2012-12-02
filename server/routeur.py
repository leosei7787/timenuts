from google.appengine.ext import webapp
from google.appengine.api import users
from server.models.user import user
from server.models.skill import skill
from server.models.skillstouser import skillstouser
from server.models.service import service
from server.models.category import category
from google.appengine.ext.webapp.util import run_wsgi_app
import datetime
import random
import os
import logging
import json
from google.appengine.ext import db
import config

# Wrappers and utilities

def login_required(fn):
    """Decorator so that fn (which is a class function like get) is sent to a create login page if user is not logged"""
    def wrapped(obj):
        Login = users.get_current_user()
        if Login:
            return fn(obj)
        else:
            obj.redirect(users.create_login_url(obj.request.uri))
    return wrapped

def get_db_user(login):
    """Gets the user as in the db model from the user from request usermail (when user logged in)."""
    return user.gql("WHERE Email='%s'" % login.email()).run(limit=1).next()

# Views

class services(webapp.RequestHandler):
  def get(self):
    if self.request.get("debug") == "True":
      # get current user
      Login = users.get_current_user()
      if Login:
        # get all skills of that user
        #Email = Login.email()
        Email = self.request.get("usermail") 
        User = user.gql('WHERE Email=\''+Email+'\'').run(limit=1).next()
        Skills = User.get_skills()
        Services = []
        for s in Skills:
          LindedServices = s.linked_services.run()
          for Service in LindedServices:
            Services.append(Service)

        self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
        self.response.out.write( json.dumps([p.to_dict() for p in Services]) )
      else:
        self.redirect(users.create_login_url(self.request.uri))
    else:
      path = os.path.join(os.path.split(__file__)[0], 'json/service.json')
      self.response.out.write(open(path, 'r').read())

class userview(webapp.RequestHandler):
    """View rendering the user jsons"""
    @login_required
    def get(self):
        Login = users.get_current_user()
        u = get_db_user(Login)
        # GET parameter
        t = self.request.get('Type')
        if t == "small":
            self.response.out.write(json.dumps(u.to_small_dict()))
        elif t == "full":
            self.response.out.write(json.dumps(u.to_big_dict()))
        else:
            self.response.out.write("Error: Type GET parameter is taking values in ['small', 'full']")
        
class login(webapp.RequestHandler):
    def get(self):
        Login = users.get_current_user()
        if Login:
          q = user.gql('WHERE Email=\''+Login.email()+'\'')
          if q.count() == 0:
              u= user(ForeName = "",
                  SureName = "",
                  Email = Login.email(),
                  ImageURL = 'http://nfs-tr.com/images/avatars/003.png',
                  Headline = 'Awesomness',
                  TimeCredit = random.randint(0,10),
                  Involvement = random.randint(0,1000),
                  Awards = []
                  )
              u.put()
            
            
          self.response.headers['Content-Type'] = 'text/plain'
          self.response.out.write('Hello, ' + Login.email())
        else:
            self.redirect(users.create_login_url(self.request.uri))
            
class logout(webapp.RequestHandler):
    def get(self):
        Login = users.get_current_user()
        self.redirect(users.create_logout_url(self.request.uri))

class filltable (webapp.RequestHandler):
    def get(self):
        query = user.all(keys_only=True)
        entries =query.fetch(1000)
        db.delete(entries)
        query = category.all(keys_only=True)
        entries =query.fetch(1000)
        db.delete(entries)
        query = service.all(keys_only=True)
        entries =query.fetch(1000)
        db.delete(entries)
        query = skill.all(keys_only=True)
        entries =query.fetch(1000)
        db.delete(entries)        
        query = skillstouser.all(keys_only=True)
        entries =query.fetch(1000)
        db.delete(entries)

        # Store category
        for Category in Categories:
          c = category(Name=Category)
          c.put()
            for Skill in Category[c]:
              s = skill(Name=Skills,Category=c)

        # Define profiles
        for User in Profils:
          u= user(FirstName = User.FirstName,
            LastName = User.LastName,
            Email = User.Email,
            Image = User.Image,
            Headline = User.Headline,
            TimeCredit = User.TimeCredit,
            Involvement = User.Involvement,
            Address = User.Address,
            Awards = []
          )
          u.put()       

          for Skill in User[u]["Skills"]:
            s = skill.gql("Where Name="+Skill).run().next() 
            skillstouser(Skill=s,User=u).put()  


        
        #Service
        for x in range(10):
            service(
                Title =  "Service request, fake Title"+str(x),
                Description = "This is the comment of my Request "+ str(x),
                Requester =  u,
                TimeNeeded = x,
                Skill = s,
                Geoloc = True,
                StartDate = datetime.datetime.now(),
                EndDate = datetime.datetime.now()
                ).put()

        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.write("Done")

class index (webapp.RequestHandler):
    def get(self):  
        path = os.path.join(os.path.split(__file__)[0], '..','static/index.html')
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.out.write(open(path, 'r').read()) 


