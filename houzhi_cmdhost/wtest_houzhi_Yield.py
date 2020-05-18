#-*- coding:utf-8 -*-
# Author  : Cuiwenhao
# Time    : 2020-03-09 08:57
# Software: PyCharm
import pytest

@pytest.fixture(scope="function")
def demo_fix():
    print("\n测试用例的前置准备操作")
    yield
    print("测试用例的后置操作")

def test_1(demo_fix):
    print("\n执行测试用例11111")

def test_2():
    print("\n执行测试用例22222")

def test_3(demo_fix):
    print("\n执行测试用例33333")
