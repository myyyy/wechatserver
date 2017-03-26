# -*- coding:utf-8 -*-
import tornado.web
from wechatpy.parser import parse_message
from wechatpy import WeChatClient
from event import get_localizer
TOKEN = '123456'
APPID = 'wxecb5391ec8a58227'
SECRET = 'fa32576b9daa6fd020c0104e6092196a'
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class BaseHandler(tornado.web.RequestHandler):

    _USER_ID = '_USER_ID'
    _ADMIN_ID = '_ADMIN_ID'
    client = property(lambda self: self.get_client())
    reply = property(lambda self: self.get_reply())

    def get_client(self):
        client = WeChatClient(APPID, SECRET)
        return client

    def get_reply(self):
        xml = self.request.body
        msg = parse_message(xml)
        if msg.type == 'text':
            reply = get_localizer(msg.type).reply(msg)
        if msg.type == 'event':
            reply = get_localizer(msg.event).reply(msg)
        return reply
