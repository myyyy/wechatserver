# -*- coding:utf-8 -*-
import os
import time


def app_timer():
    pwd = os.getcwd()
    #当前文件的父路径
    path=os.path.abspath(os.path.dirname(pwd)+os.path.sep+".")
    #当前文件的前两级目录
    # grader_father=os.path.abspath(os.path.dirname(pwd)+os.path.sep+"..")
    os.chdir(path)
    while True:
        time.sleep(10)
        try:
            os.system("python clinet.py")
        except Exception as e:
            pass


if __name__ == '__main__':
    app_timer()
