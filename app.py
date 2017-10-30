import time
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.ioloop import IOLoop
from handlers.users import MainHandler, TestHandler
import tornado.options
from tornado.options import options, define


# define('env', default='dev', help='env', type=str)


print("main")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/(.*)", MainHandler),
            (r"/test", TestHandler),
        ]

        # settings = dict(
        #     debug=True,
        # )

        super(Application, self).__init__(handlers)
        # self.db = db


def make_app():
    tornado.options.parse_command_line()
    print(options.DB_NAME)
    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8888)
    server.start(4)
    # app.listen(8888)
    IOLoop.current().start()

if __name__ == "__main__":
    make_app()
