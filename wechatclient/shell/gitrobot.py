# -*- coding:utf-8 -*-
import os
import time


def dev_robot():
    path = "/home/pi/code/wechatserver/wechatclient/"
    os.chdir(path)
    try:
        os.system("git fetch  --all")
        os.system("git reset --hard tornado")
        os.system("git pull")
    except Exception as e:
        raise

    try:
        os.system("python clinet.py")
    except Exception as e:
        raise e


if __name__ == '__main__':

    while True:
        time.sleep(100)
        cas_val = dev_robot()
        print cas_val
