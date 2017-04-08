# -*- coding:utf-8 -*-
import tornado.web
from wechatpy.parser import parse_message
from wechatpy import WeChatClient
TOKEN = '123456'
APPID = 'wxecb5391ec8a58227'
SECRET = 'fa32576b9daa6fd020c0104e6092196a'
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class BaseHandler(object):
    def get_client(self):
        client = WeChatClient(APPID, SECRET)
        a = client.menu.create({
            "button": [
                {
                    "type": "click",
                    "name": "阅读",
                    "key": "TODAY_READ"
                },
                {
                    "type": "click",
                    "name": "音乐",
                    "key": "TODAY_MUSIC"
                },
                {
                    "name": "时光",
                    "sub_button": [
                        {
                            "type": "click",
                            "name": "状态",
                            "key": "TODAY_STATUS"
                        },
                        {
                            "type": "view",
                            "name": "故事",
                            "url": "http://wufazhuce.com/"
                        },
                        {
                            "type": "view",
                            "name": "再见",
                            "url": "http://byetimes.com/"
                        },
                        {
                            "type": "view",
                            "name": "关于我们",
                            "url": "http://suyafei.com/"
                        }
                    ]
                }
            ],
        })

        return a


if __name__ == '__main__':

    client = BaseHandler().get_client()
    print (client)
