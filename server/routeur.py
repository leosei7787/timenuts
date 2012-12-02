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

def get_db_user(request, login):
    """Gets the user as in the db model from the user from request usermail (when user logged in)."""
    e = login.email()
    return user.gql("WHERE Email='%s'" % e).run(limit=1).next()

def render_static_user_jsons(handler, t):
    if t == "small": j = 'smalluser.json'
    elif t == "full": j = 'fulluser.json'
    path = os.path.join(os.path.split(__file__)[0], 'json/'+j)
    handler.response.out.write(open(path, 'r').read())

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

class myuserview(webapp.RequestHandler):
    """View rendering the user jsons"""
    def get(self):
        t = self.request.get('Type')
        if t not in ['small', 'full']:
            self.response.out.write("Error: Type GET parameter is taking values in ['small', 'full']")
            return
        if self.request.get("debug") != "True":
            Login = users.get_current_user()
            if Login:
                u = get_db_user(self.request, Login)
                # GET parameter
                if t == "small":
                    self.response.out.write(json.dumps(u.to_small_dict()))
                elif t == "full":
                    self.response.out.write(json.dumps(u.to_big_dict()))
            else:
                self.redirect(users.create_login_url(self.request.uri))
        else: # Things are working
            render_static_user_jsons(self, t)

class userview(webapp.RequestHandler):
    """View rendering some user jsons"""
    def get(self):
        t = self.request.get('Type')
        if t not in ['small', 'full']:
            self.response.out.write("Error: Type GET parameter is taking values in ['small', 'full']")
            return
        try:
            Id = int(self.request.get('Id'))
        except ValueError:  # If int() not working
            self.response.out.write("Error: GET parameter Id must be an integer")
            return
        if self.request.get("debug") == "True":
            u = user.get_by_id(Id)
            if t == "small":
                d = u.to_small_dict()
            else:
                d = u.to_big_dict()
            self.resposne.out.write(d)
        else:
            render_static_user_jsons(self, t)
        
class login(webapp.RequestHandler):
    def get(self):
        Login = users.get_current_user()
        if Login:
          q = user.gql('WHERE Email=\''+Login.email()+'\'')
          if q.count() == 0:
              u= user(FirstName = "",
                  LastName = "",
                  Email = Login.email(),
                  Image = 'http://nfs-tr.com/images/avatars/003.png',
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


