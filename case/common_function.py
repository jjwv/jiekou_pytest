#-*- coding:utf-8 -*-
# Author  : Cuiwenhao
# Time    : 2020-03-05 12:07
# Software: PyCharm
import requests

#公共的操作函数

def login(s):
    # s = requests.session()
    url = "http://49.235.92.12:9000/api/v1/login"
    body = {
        "username": "test",
        "password": "123456"
    }

    # 转json
    r = s.post(url, json=body)
    # print(r.json())

    # token
    token = r.json()["token"]
    print("取出token:%s" % token)

    h = {
        "Authorization": "Token %s" % token
    }
    s.headers.update(h)  # 更新到session会话
    # 更新之后的头部
    # print(s.headers)
    return token
