# -*- coding:utf-8 -*-
from wechatpy.replies import TextReply
from wechatpy import create_reply
from storage.robot import TuLingRobot
from storage.machine import Machine


class SubscribeEvent(object):
    """用户关注事件"""

    def reply(self, msg):
        reply = create_reply('感谢您的关注', message=msg)
        return reply.render()


class UnsubscribeEvent(object):
    """用户取消关注事件"""
    # event = 'unsubscribe'

    def reply(self, msg):
        pass


class SubscribeScanEvent(object):
    """用户扫描二维码关注事件"""
    # _reply = 'subscribe_scan'

    def reply(self, msg):
        pass


class TextEvent(object):
    """图铃机器人"""

    def reply(self, msg):
        if msg.content in 'status':
            data = Machine().fast_data
            reply = TextReply(content=data, message=msg)
            reply = create_reply(data, message=msg)
        else:
            robot = TuLingRobot(msg.content)
            reply = create_reply(robot.reply, message=msg)
        return reply.render()


class ClickEvent(object):
    """点击菜单拉取消息事件"""

    def reply(self, msg):
        if msg.key == 'TODAY_STATUS':
            import pdb
            pdb.set_trace()
            data = Machine().fast_data
            reply = TextReply(content=data, message=msg)
            reply = create_reply(data, message=msg)
            return reply.render()


def get_localizer(event="subscribe", msg='msg'):
    """The factory method"""
    print (msg)
    import pdb
    pdb.set_trace()
    languages = dict(subscribe=SubscribeEvent, unsubscribe=UnsubscribeEvent,
                     subscribe_scan=SubscribeScanEvent, text=TextEvent, click=ClickEvent)
    return languages[event](msg)

if __name__ == '__main__':
    get_localizer().reply('msg')
