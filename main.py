import webapp2, jinja2, os, re
from google.appengine.ext import db


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class StudentDB(db.Model):
    """ create student database
    """
    first_name = db.StringProperty(required=True)
    last_name = db.StringProperty(required=True)
    phone = db.StringProperty(required=True)
    email = db.StringProperty()
    address = db.StringProperty()
    academic_year = db.IntegerProperty()
    area_study = db.StringProperty()
    focus_area = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
     def get(self):
        self.render("index.html")

class StudentDetails(Handler):
    def get(self):
        self.render("profile.html")

class StudentUpdate(Handler):
    def get(self):
        self.render("update.html")

class NewStudent(Handler):
    def get(self):
        self.render("create.html")

class EngageTeam(Handler):
    def get(self):
        self.render("engagementteam.html")



app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/student', StudentDetails),
    webapp2.Route('/student/update', StudentUpdate),

    # webapp2.Route('/student/update/<id:\d+>', StudentUpdate),

    ('/student/create', NewStudent),
    ('/student/engageteam', EngageTeam)
], debug=True)
