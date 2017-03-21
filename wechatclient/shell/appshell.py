# -*- coding:utf-8 -*-
import os
import time


def app_timer():
	path = "/home/pi/code/wechatserver/wechatclient/"
   	os.chdir(path)
	while True:
		time.sleep(10)
		try:
			os.system("python clinet.py")
		except Exception as e:
		        pass


if __name__ == '__main__':
	app_timer()
