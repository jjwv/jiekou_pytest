#-*- coding:utf-8 -*-
# Author  : Cuiwenhao
# Time    : 2020-03-05 14:58
# Software: PyCharm

import requests
import re
import allure
from requests_toolbelt import MultipartEncoder
from lxml import etree

@allure.step("登录xadmin")
def login_xadmin(s):
    '''xadmin登陆'''
    url = "http://49.235.92.12:8020/xadmin/"
    r1 = s.get(url)
    # print(r1.text)
    tokens = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", r1.text)
    print(tokens[0])

    body = {
        "csrfmiddlewaretoken": tokens[0],
        "username": "admin",
        "password": "yoyo123456",
        "this_is_the_login_form": "1",
        "next": "/xadmin/"
    }
    r2 = s.post(url, data=body)
    # print(r2.text)
    if "主页面 | 后台页面" in r2.text:
        print("登陆成功")
    else:
        print("登陆失败")

@allure.step("添加老师")
def add_teacher(s, name="小小小老师"):
    '''添加老师'''
    url2 = "http://49.235.92.12:8020/xadmin/hello/teacherman/add/"
    # multipart/form-data  类型post请求
    r3 = s.get(url2)
    tokens2 = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", r3.text)
    print(tokens2[0])
    m = MultipartEncoder(
                fields=[
                    ("csrfmiddlewaretoken", tokens2[0]),
                    ("csrfmiddlewaretoken", tokens2[0]),
                    ("teacher_name", name),
                    ("tel", "1222222"),
                    ("mail", "111@qq.com"),
                    ("sex", "M"),
                    ("_save", ""),
                ]
    )
    r4 = s.post(url2, data=m, headers={'Content-Type': m.content_type})
    return r4.text

@allure.step("获取添加结果")
def get_add_result(result):
    '''获取添加文本的结果'''
    demo = etree.HTML(result)
    nodes = demo.xpath('//*[@id="changelist-form"]/div[1]/table/tbody/tr[1]/td[2]/a')
    # print(nodes[0].text)
    return nodes[0].text

s = requests.session()
login_xadmin(s)

def add_image(title="图片test_111"):
    '''添加图片'''
    url3 = "http://49.235.92.12:8020/xadmin/hello/fileimage/add/"
    r3 = s.get(url3)
    # print(r1.text)
    tokens = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", r3.text)
    # print(tokens[0])

    m = MultipartEncoder(
                    fields=[
                        ("csrfmiddlewaretoken", tokens[0]),
                        ("csrfmiddlewaretoken", tokens[0]),
                        ("title", title),
                        # ("image", ('122.png', open('122.png', 'rb'), 'image/png')),
                        ("fiels", ('122.png', open('122.png', 'rb'), 'image/png')),
                        ("_save", ""),
                    ]
        )
    r4 = s.post(url3, data=m, headers={'Content-Type': m.content_type})
    # print(r4.text)

add_image(title="文件222")

# if __name__ == '__main__':
#     s = requests.session()
#     login_xadmin(s)
#     result = add_teacher(s, name="小小小小")
#     # 判断
#     actul_result = get_add_result(result)
#     assert actul_result == "小小小小"

