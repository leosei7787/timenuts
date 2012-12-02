from google.appengine.ext import webapp
from google.appengine.api import users
from server.models.user import user
from server.models.skill import skill
from server.models.skillstouser import skillstouser
from server.models.service import service
from server.models.category import category
from server.models.comment import comment
from server.models.serviceapplicants import serviceapplicants
from google.appengine.ext.webapp.util import run_wsgi_app
from datetime import *
import random
import os
import logging
import json
from google.appengine.ext import db
from server.config import *

# Wrappers and utilities

def login_required(fn):
    def wrapper(obj):
        Login = users.get_current_user()
        if Login:
            fn(obj)
        else:
            obj.redirect(users.create_login_url(obj.request.uri))
    return wrapper


def get_db_user(request, login):
    """Gets the user as in the db model from the user from request usermail (when user logged in)."""
    e = login.email()
    return user.gql("WHERE Email='%s'" % e).run(limit=1).next()

#def render_static_user_jsons(handler, t):
#    if t == "small": j = 'smalluser.json'
#    elif t == "full": j = 'fulluser.json'
#    path = os.path.join(os.path.split(__file__)[0], 'json/'+j)
#    handler.response.out.write(open(path, 'r').read())

# Views

class services(webapp.RequestHandler):
  def get(self):
    if self.request.get("debug") != "True":
      # get current user
      Login = users.get_current_user()
      if Login:
        # get all skills of that user
        Email = Login.email()
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


class serviceelement(webapp.RequestHandler):
  def get(self):
    Path = self.request.path.split("/")
    Id = Path[ (len(Path)-1) ]
    Service = service.get_by_id( int(Id) )
    self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
    self.response.out.write( json.dumps( Service.to_dict() ) )

  def post(self):
    User = get_db_user(self.request,users.get_current_user())
    Skill = skill.gql("WHERE Name='"+self.request.get('Skill')+"'").run().next()
    Service = service(
            Title =  self.request.get('Title'),
            Description = self.request.get('Description'),
            Requester = User ,
            TimeNeeded = int(self.request.get('TimeNeeded')),
            Skill = Skill,
            Geoloc = bool(self.request.get('Geoloc')),
            StartDate = datetime.strptime(self.request.get('StartDate'),'%Y-%M-%d'),
            EndDate = datetime.strptime(self.request.get('EndDate'),'%Y-%M-%d')
            )
    Service.put()
    self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
    self.response.out.write( json.dumps( Service.to_dict() ))




class myuserview(webapp.RequestHandler):
    """View rendering the user jsons"""
    @login_required
    def get(self):
        t = self.request.get('Type')
        if t not in ['small', 'full']:
            self.response.out.write("Error: Type GET parameter is taking values in ['small', 'full']")
            return
        self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
        Login = users.get_current_user()
        u = get_db_user(self.request, Login)
        # GET parameter
        if t == "small":
            self.response.out.write(json.dumps(u.to_small_dict()))
        elif t == "full":
            self.response.out.write(json.dumps(u.to_big_dict()))

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
        self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
        u = user.get_by_id(Id)
        if t == "small":
            d = u.to_small_dict()
        else:
            d = u.to_big_dict()
        Login = users.get_current_user()
        LoginUser = get_db_user(self.request, Login)
        if u.key() in LoginUser.Friends:
            d['AreFriends'] = "True"
        else:
            d['AreFriends'] = "False"
        self.response.out.write(json.dumps(d))

class myapplying(webapp.RequestHandler):
  @login_required
  def get(self):
      # get current user
      Login = users.get_current_user()
      self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
      u = get_db_user(self.request, Login)
      servapps = serviceapplicants.gql("WHERE Applicant=:1", u)
      ApplyingDict = [servapp.Service.to_dict() for servapp in servapps]
      self.response.out.write(json.dumps(ApplyingDict))

class mydoneservices(webapp.RequestHandler):
    @login_required
    def get(self):
        Login = users.get_current_user()
        self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
        u = get_db_user(self.request, Login)
        self.response.out.write(
            json.dumps([s.to_dict() for s in service.gql("WHERE Responder=:1", u)]))
        
class myrequests(webapp.RequestHandler):
    @login_required
    def get(self):
        Login = users.get_current_user()
        self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
        u = get_db_user(self.request, Login)
        self.response.out.write(
            json.dumps([s.to_dict() for s in service.gql("WHERE Requester=:1", u)]))

class skills(webapp.RequestHandler):
  def get(self):
    Skills = skill.all().run()
    Cat = {}
    for Skill in Skills:
      if Skill.Category.Name not in Cat:
        Cat[Skill.Category.Name] = []

      Cat[Skill.Category.Name].append(Skill.Name)

    self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
    self.response.out.write( json.dumps(Cat) )

class commentelement(webapp.RequestHandler):
  def post(self):
    Path = self.request.path.split("/")
    Id = Path[ (len(Path)-1) ]
    Login = users.get_current_user()
    User = get_db_user(self.request,Login)
    
    #Store comment
    c = comment(Comment = self.request.get("Comment"),
      Owner = User
      )
    c.put()

    #Append comment to Service
    Service = service.get_by_id(int(Id))
    Service.Comments.append(c)
    self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
    self.response.out.write( json.dumps(Service) )



class comments(webapp.RequestHandler):
  def get(self):
    Path = self.request.path.split("/")
    Id = Path[ (len(Path)-1) ]
    Service = service.get_by_id(int(Id))
    Comments = []
    CommentsId = Service.Comments
    for Comment in CommentsId:
      Comments.append( comment.get_by_id(Comment) )
      self.response.write(comment.get_by_id(Comment).Comment)
    self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
    self.response.out.write( json.dumps([c.to_dict() for c in Comments]) )

class applyrequest(webapp.RequestHandler):
    @login_required
    def post(self):
        try:
            ServiceId = int(self.request.get('ServiceId'))
        except ValueError:  # If int() not working
            self.response.out.write("Error: POST parameter ServiceId must be an integer")
        Login = users.get_current_user()
        User = get_db_user(users.get_current_user, Login)
        Service = service.get_by_id(ServiceId)
        # Test see if there is already the mapping in serviceapplicants
        ServiceApplicants = serviceapplicants(
            Service = Service,
            Applicant = User,
        )
        if serviceapplicants.gql("WHERE User=:1 AND Service=:2", User, Service).count() == 0:
            ServiceApplicants.put()
        self.response.out.write(json.dumps(ServiceApplicants.to_dict()))


class login(webapp.RequestHandler):
    @login_required
    def get(self):
        Login = users.get_current_user()
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
        query = comment.all(keys_only=True)
        entries =query.fetch(1000)
        db.delete(entries)

        # Store category & Skills
        for Category in ConfigCategories:
          c = category(Name=Category)
          c.put()
          for Skill in ConfigCategories[Category]:
            skill(Name=Skill,Category=c).put()

        # Define profiles + link to Skills
        for User in ConfigProfils:
          u =  user(FirstName = User['FirstName'],
            LastName = User['LastName'],
            Email = User['Email'],
            Image = User['Image'],
            Headline = User['Headline'],
            TimeCredit = User['TimeCredit'],
            Involvement = User['Involvement'],
            Address = User['Address'],
            Awards = []
            )
          u.put()       

          for Skill in User["Skills"]:
            s = skill.gql("WHERE Name='"+Skill+"'").run().next() 
            skillstouser(Skill=s,User=u).put()  

        # Friends
        for User in ConfigProfils:
          if User.has_key('Friends'):
              for FriendEmail in User['Friends']:
                FriendUser = user.gql("WHERE Email='%s'" % FriendEmail).run().next()
                u = user.gql("WHERE Email='%s'" % User['Email']).run().next()
                u.Friends.append(FriendUser.key())
              u.put() 

        #Service
        for Service in ConfigServices:
          ## all FK needed
          User = user.gql("WHERE Email='"+Service["Requester"]+"'").run().next()
          Skill = skill.gql("WHERE Name='"+Service["Skill"]+"'").run().next()

          ser = service(
            Title =  Service['Title'],
            Description = Service['Description'],
            Requester = User ,
            TimeNeeded = Service['TimeNeeded'],
            Skill = Skill,
            Geoloc = Service['Geoloc'],
            StartDate = datetime.strptime(Service['StartDate'],'%Y-%M-%d'),
            EndDate = datetime.strptime(Service['EndDate'],'%Y-%M-%d'),
            Comments = []
          )
          if Service.has_key("Responder"):
            Responder = user.gql("WHERE Email='"+Service["Responder"]+"'").run().next()
            ser.Responder = Responder
          if Service.has_key('Comments'):
            for C in Service["Comments"]:
              User = user.gql("WHERE Email='"+C["Owner"]+"'").run().next()
              c  = comment(
                Owner = User,
                Comment = C["Comment"]
              )
              c.put()
              ser.Comments.append(c.key().id())
          ser.put()

        # Service Applicants
        for SAppl in ServiceApplicants:
            # FK
            Service = service.gql("WHERE Title='%s'" % SAppl['Service']).run().next()
            Applicant = user.gql("WHERE Email='%s'" % SAppl['Applicant']).run().next()
            serviceapplicants(
                Date = datetime.strptime(SAppl['Date'], '%Y-%M-%d'),
                Service = Service,
                Applicant = Applicant
            ).put()

        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.write("Done")

class index (webapp.RequestHandler):
    def get(self):  
        # Path = os.path.split(__file__)[0].split("/")
        # Path = Path[0:(len(Path)-1)]
        File = os.path.join('static/index.html')
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.out.write(open(File, 'r').read()) 


