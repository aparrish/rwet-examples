import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
tornado.options.parse_command_line()

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		greeting = self.get_argument('greeting', None)
		if greeting:
			self.write(greeting + ', friendly user!')
		else:
			self.write('you got me!')
	def post(self):
		username = self.get_argument('name', None)
		if username:
			self.write('Nice to meet you, ' + username)
		else:
			self.write('you posted to me!')

application = tornado.web.Application(handlers=[(r"/", IndexHandler)])

http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(options.port)
tornado.ioloop.IOLoop.instance().start()

