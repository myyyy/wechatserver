# -*- coding:utf-8 -*-
import os
import time
def dev_robot():
	path = "/home/pi/code/wechatserver/wechatclient/"
	os.chdir(path)
	val = os.system("git commit -am'gitrobot'")
	val = os.system("git pull")
	os.system("python clinet.py")


if __name__ == '__main__':

	
	while True:
<<<<<<< HEAD
		print(1)
		time.sleep(10) 
=======
		time.sleep(100) 
>>>>>>> 380e7eb0daeaa8503211bd0cae5e3714bb8df907
		cas_val = dev_robot()
	
