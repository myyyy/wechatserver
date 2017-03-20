# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import os
import json
import tornado
import tornado.web
import tornado.ioloop
from tornado import gen
from tornado.gen import coroutine
from wechatpy import WeChatClient
from wechatpy.parser import parse_message
import json
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
TOKEN = '123456'
APPID = 'wxecb5391ec8a58227'
SECRET = 'fa32576b9daa6fd020c0104e6092196a'
# OPENID = 'ozJS1syaqn5ztglMsr8ceH8o2zCQ'


class IndexHandler(tornado.web.RequestHandler):


    def get(self):
        signature = self.get_argument('signature','')
        timestamp = self.get_argument('timestamp','')
        nonce = self.get_argument('nonce','')
        client = WeChatClient(APPID, SECRET)
        print (client)
        try:
            check_signature(TOKEN, signature, timestamp, nonce)
        except InvalidSignatureException as e:
            self.write(str(e))
    def post(self):
        body = self.request.body
        print (body)
        msg = parse_message(xml)
        print (msg.content)


if __name__ == '__main__':
    app = tornado.web.Application(
        handlers=[
            (r'/wechat/', IndexHandler),
        ],
        debug=True,
    )
    app.listen(1121)
    print('server start on 127.0.0.1:1121')
    tornado.ioloop.IOLoop.instance().start()
