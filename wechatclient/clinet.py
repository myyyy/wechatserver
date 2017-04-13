# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import os
import json
import tornado
import tornado.web
import tornado.ioloop
from logic.wechat import BaseHandler

from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from logic import timetask as tt


class IndexHandler(BaseHandler):

    def get(self):
        signature = self.get_argument('signature', '')
        timestamp = self.get_argument('timestamp', '')
        nonce = self.get_argument('nonce', '')
        client = self.client
        try:
            check_signature(TOKEN, signature, timestamp, nonce)
        except InvalidSignatureException as e:
            self.write(str(e))

    def post(self):
        reply = self.reply
        self.write(reply)


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
