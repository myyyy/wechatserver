# -*- coding:utf-8 -*-
from time import sleep

import tornado.web
from wechatpy.parser import parse_message
from wechatpy import WeChatClient

from datetime import datetime, timedelta

TOKEN = '123456'
APPID = 'wxecb5391ec8a58227'
SECRET = 'fa32576b9daa6fd020c0104e6092196a'
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import time


class TimeTask(object):

    def doFunc(self):
        client = WeChatClient(APPID, SECRET)
        # {"total":3,"count":3,"data":{"openid":["oWYtjwSmIQQVZ5ec3t2zC0nqDND4","oWYtjwfjyniCidxvlw5zZr5rQ0wk","oWYtjwcb6JiGduPVF-Hx0VFW8mp8"]},"next_openid":"oWYtjwcb6JiGduPVF-Hx0VFW8mp8"}
        followers = client.user.get_followers()
        openids = followers.get("data", {}).get("openid", {})
        for oid in openids:
            send_articles(oid, '测试，抱歉了！')

    def doFirst(self):
        SECONDS_PER_DAY = 24 * 60 * 60
        curTime = datetime.now()
        desTime = curTime.replace(hour=10, minute=0, second=0, microsecond=0)
        delta = curTime - desTime
        skipSeconds = SECONDS_PER_DAY - delta.total_seconds()
        print "Must sleep %d h" % (int(skipSeconds) / (60 * 60))
        sleep(skipSeconds)
        doFunc()
if __name__ == '__main__':
    tt = TimeTask()
    tt.doFirst()
