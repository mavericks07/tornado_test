import tornado
from tornado.testing import AsyncHTTPTestCase, AsyncTestCase, AsyncHTTPClient
from tornado.escape import json_decode, json_encode
from tornado import gen
from models import User
from schemas import UserSchema


class MyTestCase(AsyncTestCase):
    @tornado.testing.gen_test
    def test_http_fetch(self):
        print(self.io_loop)
        client = AsyncHTTPClient(self.io_loop)
        response = yield client.fetch("http://127.0.0.1:8888")
        # Test contents of response
        self.assertIs(200, response.code)
