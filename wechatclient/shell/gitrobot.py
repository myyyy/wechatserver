# -*- coding:utf-8 -*-
import os
import time
def dev_robot():
	path = "/home/pi/code/wechatserver/wechatclient/"
	os.chdir(path)
	os.system("git fetch  --all")
	os.system("git reset --hard tornado")
	val = os.system("git pull")
	os.system("python clinet.py")


if __name__ == '__main__':

	
	while True:
		print(1)
		time.sleep(100) 
		cas_val = dev_robot()
	
