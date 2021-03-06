# -*- coding:utf-8 -*-
import os
import time


def dev_robot():
    pwd = os.getcwd()
    # 当前文件的父路径
    path = os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")
    os.chdir(path)
    try:
        os.system("git fetch  --all")
        os.system("git reset --hard tornado")
        os.system("git pull")
    except Exception as e:
        pass


def git_timer():
    while True:
        time.sleep(10)
        cas_val = dev_robot()
        print(cas_val)


if __name__ == '__main__':
    git_timer()
