from models.models import User
from schemas import UserSchema
from tornado import escape
from tornado.concurrent import run_on_executor
from tornado.platform.asyncio import to_tornado_future
from concurrent.futures import ThreadPoolExecutor
from tornado.escape import json_encode, json_decode, utf8, unicode_type
import threading
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(5)

    # def prepare(self):
    #     print("con")
    #     self.application.db.connect()
    #     return super(MainHandler, self).prepare()
    #
    # def on_finish(self):
    #     print("close")
    #     if not self.application.db.is_closed():
    #         self.application.db.close()
    #     return super(MainHandler, self).on_finish()

    async def get(self, username):
        data = await to_tornado_future(self.get_data(username))
        self.write(json_decode(data.data))

    async def post(self, *args, **kwargs):
        data = await to_tornado_future(self.get_data())
        self.write(json_decode(data.data))

    @run_on_executor
    def get_data(self, username):
        if username:
            user = User.select().filter(User.username == username).first()
            data = UserSchema().dumps(user)
        else:
            user = User.select()
            data = UserSchema(many=True).dumps(user)
        return data

    def write(self, chunk):

        if self._finished:
            raise RuntimeError("Cannot write() after finish()")
        if not isinstance(chunk, (bytes, unicode_type, dict, list)):
            message = "write() only accepts bytes, unicode, list and dict objects"
            raise TypeError(message)
        if isinstance(chunk, (dict, list)):
            chunk = escape.json_encode(chunk)
            self.set_header("Content-Type", "application/json; charset=UTF-8")
        chunk = utf8(chunk)
        self._write_buffer.append(chunk)


class TestHandler(tornado.web.RequestHandler):

    async def get(self, *args, **kwargs):
        print(threading.current_thread().getName())
        self.write("ok111")