#-*- coding:utf-8 -*-
# Author  : Cuiwenhao
# Time    : 2020-03-09 10:46
# Software: PyCharm

import pytest
import allure


@allure.step("用例的操作步骤：1")
def step1():
    print("用例的操作步骤：1")

@allure.step("用例的操作步骤：2")
def step2():
    print("用例的操作步骤：2")

@allure.feature("星座运势")
class TestQQ():
    '''接口名称的描述'''
    @allure.story("星座运势- type传值错误，数字，特殊字符，带空格")
    def test_case_1(self, login):
        '''
        用例详情的描述：接口地址：http://web.juhe.cn:8080/constellation/getAll
        请求方式：get
        星座运势申请一个key如：AppKey：cde5e16435cd0217f505a88898b60707
        :param login: 前置条件-登录
        :return:
        '''
        step1()
        step2()
        print("测试用例1")
        assert 1==1


    @allure.story("星座运势- 必填项type为空")
    def test_case_2(self,login):
        print("测试用例1")


    @allure.story("星座运势-必填项consName值为空")
    def test_case_3(self,login):
        print("测试用例1")


