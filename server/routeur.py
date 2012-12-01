from google.appengine.ext import webapp
from google.appengine.api import users
from server.models.user import user
from server.models.skill import skill
from server.models.skillstouser import skillstouser
from google.appengine.ext.webapp.util import run_wsgi_app
import random
import os

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
                for s in Skills:
                    self.response.out.write(s.Name)
                
                self.response.out.write( "hello "+str(User.key().id()) )
            else:
                self.redirect(users.create_login_url(self.request.uri))
        else:
            path = os.path.join(os.path.split(__file__)[0], 'json/service.json')
            self.response.out.write(open(path, 'r').read())
        
class login(webapp.RequestHandler):
    def get(self):
        Login = users.get_current_user()
        if Login:
            q = user.gql('WHERE Email=\''+login.email()+'\'')
            if q.count() == 0:
                u= user(ForeName = "",
                    SureName = "",
                    Email = login.email(),
                    ImageURL = 'http://nfs-tr.com/images/avatars/003.png',
                    Headline = 'Awesomness',
                    TimeCredit = random.randint(0,10),
                    Involvment = random.randint(0,1000),
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
        # User
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
        #skill
        s=skill(Name="Javascript")
        s.put()
        # skillstouser
        stu = skillstouser(User=u.key(), Skill=s.key())
        stu.put()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write("Done")
