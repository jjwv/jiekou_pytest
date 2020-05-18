#-*- coding:utf-8 -*-
# Author  : Cuiwenhao
# Time    : 2020-03-09 10:46
# Software: PyCharm


import pytest


@pytest.fixture(scope="session")
def login():
    print("用例先登录")