# -*- coding: utf-8 -*-
from __future__ import unicode_literals
 
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
 
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage
import pinfo 
 
WECHAT_TOKEN = '123456'
AppID = 'wxecb5391ec8a58227'
AppSecret = 'fa32576b9daa6fd020c0104e6092196a'
# 实例化 WechatBasic
wechat_instance = WechatBasic(
    token=WECHAT_TOKEN,
    appid=AppID,
    appsecret=AppSecret
)
 
@csrf_exempt
def index(request):
    if request.method == 'GET':
        # 检验合法性
        # 从 request 中提取基本信息 (signature, timestamp, nonce, xml)
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
 
        if not wechat_instance.check_signature(
                signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponseBadRequest('Verify Failed')
 
        return HttpResponse(
            request.GET.get('echostr', ''), content_type="text/plain")
 

    if request.method == 'POST':
        # 解析本次请求的 XML 数据
        try:
            wechat_instance.parse_data(data=request.body)
        except ParseError:
            return HttpResponseBadRequest('Invalid XML Data')
     
        # 获取解析好的微信请求信息
        message = wechat_instance.get_message()
     
        # 关注事件以及不匹配时的默认回复
        response = wechat_instance.response_text(
            content = (
                '感谢您的关注!'
                ))
        if isinstance(message, TextMessage):
            # 当前会话内容
            content = message.content.strip()
            if content == '功能':
                reply_text = (
                        '目前支持的功能:'
                    )
            elif content.endswith('状态'):
                CPU_usage = pinfo.getCPUuse()
                CPU_temp = pinfo.getCPUtemperature()
                RAM_stats = pinfo.getRAMinfo()
                DISK_total,DISK_used,DISK_perc = pinfo.getDiskSpace()
                RAM_total = round(int(RAM_stats[0]) / 1000,1)
                RAM_used = round(int(RAM_stats[1]) / 1000,1)
                RAM_free = round(int(RAM_stats[2]) / 1000,1)
                reply_text = ('CPU Temperature = '+CPU_temp+'\n'
                                'CPU Use =' + CPU_usage + '\n'
                                'RAM Total = ' + str(RAM_total) +' MB\n'
                                'RAM Used = ' + str(RAM_used) + ' MB\n')
                                'RAM Free = ' + str(RAM_free) + ' MB\n')
                                'DISK Total Space = ' + str(DISK_total) + 'B\n'
                                'DISK Used Space = ' + str(DISK_used) + 'B\n'
                                'DISK Used Percentage = ' + str(DISK_perc)
                            )
     
            response = wechat_instance.response_text(content=reply_text)
     
        return HttpResponse(response, content_type="application/xml")
