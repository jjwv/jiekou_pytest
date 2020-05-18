#-*- coding:utf-8 -*-
# Author  : Cuiwenhao
# Time    : 2020-03-05 12:12
# Software: PyCharm
import pytest,os
from common.read_yml import readyml

def test_info(login_fix):
    s = login_fix
    url = "http://49.235.92.12:9000/api/v1/userinfo"
    r = s.get(url)
    # print(r.text)
    assert r.json()["msg"] == "sucess!"
    assert r.json()["code"] == 0


# test_data = [
#     ["M", {"message": "update some data!", "code": 0}],
#     ["F", {"message": "update some data!", "code": 0}],
#     ["x", {"message": "参数类型错误", "code": 3333}],
#     ]

curpath = os.path.dirname(os.path.realpath(__file__))
yamlpath = os.path.join(curpath,"test_data.yml")
test_data = readyml(yamlpath)["updata_info"]

@pytest.mark.parametrize("test_input,expect",test_data)
def test_updata_info(login_fix,test_input,expect):
    '''修改个人信息'''
    s = login_fix
    url = "http://49.235.92.12:9000/api/v1/userinfo"
    body = {"name": "test",
            "sex": test_input,
            "age": 20,
            "mail": "283340479@qq.com"}
    r = s.post(url, json=body)
    print(r.text)
    assert r.json()["message"] == expect["message"]
    assert r.json()["code"] == expect["code"]
