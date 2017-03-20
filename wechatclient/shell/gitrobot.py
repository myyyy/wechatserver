# -*- coding:utf-8 -*-
import os
import time
def dev_robot():
	path = "/home/pi/code/wechatserver/wechatclient/"
	os.chdir(path)
	val = os.system("git pull")
	os.system("python clinet.py")


if __name__ == '__main__':

	
	while True:
		time.sleep(10) 
		cas_val = dev_robot()
		print cas_val
	