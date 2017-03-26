# -*- coding:utf-8 -*-
import tornado.web
from wechatpy.parser import parse_message
from wechatpy import WeChatClient
TOKEN = '123456'
APPID = 'wxecb5391ec8a58227'
SECRET = 'fa32576b9daa6fd020c0104e6092196a'


class BaseHandler(tornado.web.RequestHandler):

    _USER_ID = '_USER_ID'
    _ADMIN_ID = '_ADMIN_ID'
    client = property(lambda self: self.get_client())
    msg = property(lambda self: self.get_msg())

    def get_client(self):
        client = WeChatClient(APPID, SECRET)
        client.menu.add_conditional({
            "button": [
                {
                                    "type": "click",
                                    "name": "阅读",
                                    "key": "V1001_TODAY_READ"
                                    },
                {
                    "type": "click",
                    "name": "音乐",
                    "key": "V1001_TODAY_MUSIC"
                },
                {
                    "name": "时光",
                    "sub_button": [
                        {
                            "type": "view",
                            "name": "故事",
                            "url": "http://www.soso.com/"
                        },
                        {
                            "type": "view",
                            "name": "流年",
                            "url": "http://v.qq.com/"
                        },
                        {
                            "type": "click",
                            "name": "关于我们",
                            "key": "ABOUT_US"
                        }
                    ]
                }
            ],
        })
        return client

    def get_msg(self):
        xml = self.request.body
        msg = parse_message(xml)
        try:
            if msg.event == 'subscribe':
                reply = create_reply('感谢关注', message=msg)
                self.write(_reply)
        except Exception as e:
            return msg
