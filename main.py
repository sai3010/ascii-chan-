import webapp2
import os
import jinja2
from webapp2_extras import jinja2

from google.appengine.api import users
from jinja2 import Environment,PackageLoader
from jinja2 import Environment,FileSystemLoader


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = Environment(loader=FileSystemLoader(template_dir),
           autoescape=True)


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
        self.render("rot13.html")

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
