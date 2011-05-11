import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

from context_free import ContextFree
from context_free_reader import add_rules_from_file

define("port", default=8888, help="run on the given port", type=int)
define("grammar", default="definitions.grammar", help="grammar file to load",
	type=str)
define("axiom", default="Def", help="axiom to expand from grammar", type=str)

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/", IndexHandler),
			(r"/definition", DefinitionHandler)
		]
		settings = dict(
			template_path=os.path.join(os.path.dirname(__file__), "templates"),
			static_path=os.path.join(os.path.dirname(__file__), "static")
		)
		tornado.web.Application.__init__(self, handlers, **settings)

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html')

class DefinitionHandler(tornado.web.RequestHandler):
	def post(self):
		word = self.get_argument('word')
		cfree = ContextFree()
		add_rules_from_file(cfree, open(options.grammar))
		expansion = cfree.get_expansion(options.axiom)
		self.render('definition.html', word=word, definition=' '.join(expansion))

if __name__ == "__main__":
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
