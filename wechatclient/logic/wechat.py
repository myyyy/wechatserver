# -*- coding:utf-8 -*-
import tornado.web
from wechatpy import WeChatClient
TOKEN = '123456'
APPID = 'wxecb5391ec8a58227'
SECRET = 'fa32576b9daa6fd020c0104e6092196a'


class BaseHandler(tornado.web.RequestHandler):

    def __init__(self, application, request, **kwargs):
        self.client = self.get_client()

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
