import webapp2

# makes a page from home.html
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        f= open("home.html","r")
        with open('home.html') as f:
            self.response.write(f.read())
        f.closed

# makes a page from countries.html
class Countries(webapp2.RequestHandler):
    def post(self):
        self.response.headers["Content-Type"] = "text/html"
        f= open("countries.html","r")
        with open('countries.html') as f:
            self.response.write(f.read())
        f.closed

# makes a page from sports.html
class Sports(webapp2.RequestHandler):
    def post(self):
        self.response.headers["Content-Type"] = "text/html"
        f= open("sports.html","r")
        with open('sports.html') as f:
            self.response.write(f.read())
        f.closed

# makes a page from venues.html
class Venues(webapp2.RequestHandler):
    def post(self):
        self.response.headers["Content-Type"] = "text/html"
        f= open("venues.html","r")
        with open('venues.html') as f:
            self.response.write(f.read())
        f.closed

routes = [('/', MainPage), ('/countries', Countries), ('/sports', Sports) ('/venues', Venues)]

my_app = webapp2.WSGIApplication(routes, debug=True)