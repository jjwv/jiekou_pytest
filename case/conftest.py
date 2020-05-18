#-*- coding:utf-8 -*-
# Author  : Cuiwenhao
# Time    : 2020-03-05 12:06
# Software: PyCharm

import requests
import pytest
from case.common_function import login

@pytest.fixture(scope="module")
def login_fix():
    '''自定义一个前置的操作'''
    print("先登陆")
    s = requests.session()
    login(s)
    return s