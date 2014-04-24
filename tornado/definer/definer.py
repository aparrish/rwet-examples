import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import random
from textblob import Word

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
tornado.options.parse_command_line()

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html')

class DefinitionHandler(tornado.web.RequestHandler):
	def post(self):
		word_str = self.get_argument('word')
		word_obj = Word(word_str)
		if len(word_obj.definitions) > 0:
			definition_str = random.choice(word_obj.definitions)
		else:
			definition_str = "undefinable"
		self.render('definition.html', word=word_str, definition=definition_str)

static_path = os.path.join(os.path.dirname(__file__), "static")
template_path = os.path.join(os.path.dirname(__file__), "templates")
application = tornado.web.Application(
		handlers=[(r"/", IndexHandler), (r"/definition", DefinitionHandler)],
		static_path=static_path,
		template_path=template_path)

http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(options.port)
tornado.ioloop.IOLoop.instance().start()

