import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os

import twython

from markov_by_char import CharacterMarkovGenerator

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
define("n", default=6, help="length of n-gram", type=int)
define("api_key", help="twitter api key")
define("api_secret", help="twitter api secret")
define("access_token", help="twitter access token")
define("token_secret", help="twitter token secret")

tornado.options.parse_command_line()

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html')

class MarkovHandler(tornado.web.RequestHandler):
	def get(self):
		twitter = twython.Twython(options.api_key, options.api_secret,
				options.access_token, options.token_secret)
		response = twitter.get_user_timeline(
				screen_name=self.get_argument('screen_name'),
				count=200)
		generator = CharacterMarkovGenerator(options.n, 140)
		for tweet in response:
			generator.feed(tweet['text'])
		self.write(generator.generate())

static_path = os.path.join(os.path.dirname(__file__), "static")
template_path = os.path.join(os.path.dirname(__file__), "templates")
application = tornado.web.Application(
		handlers=[(r"/", IndexHandler), (r"/markov", MarkovHandler)],
		static_path=static_path,
		template_path=template_path)

http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(options.port)
tornado.ioloop.IOLoop.instance().start()

