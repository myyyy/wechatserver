# -*- coding: utf-8 -*-
import requests

ROBOTURL  = u'http://www.tuling123.com/openapi/api'
ROBOTKEY="f4867f649f20418eb1e93f4b54149f7e"
class TuLingRobot(object):
    """docstring for TulingRobot"""
    def __init__(self, arg=None):
        self.arg = arg
        self.reply = self.get_message(arg).get('text','')

    def get_message(self,arg):
        data={'info':arg,'key':ROBOTKEY}
        response = requests.get(ROBOTURL, params=data)
        msg = response.json()
        return msg

if __name__ == '__main__':
    tu = TuLingRobot('你是谁')
    print tu.reply