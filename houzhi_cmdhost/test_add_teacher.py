#-*- coding:utf-8 -*-
# Author  : Cuiwenhao
# Time    : 2020-03-05 15:42
# Software: PyCharm

from houzhi_cmdhost.add_teacher import *
import requests,pytest

@allure.feature("编辑teacher")
class TestAddTeacher():

    @allure.story("登录-tescher，保存成功1")
    def test_add_lalala_1(self,login_xadmin_fix,delete_teacher_sql):
        s = login_xadmin_fix
        result = add_teacher(s,name="夏小小1")
        # 判断
        actul_result = get_add_result(result)
        assert actul_result == "夏小小1"

    @allure.story("登录-tescher，保存成功2")
    #如果用例出现问题，直接关联到bug信息
    @allure.issue("https://www.weibangong.com/index.html#/workBoard/workBench")
    @allure.testcase("https://www.baidu.com/baidu?isource=infinity&iname=baidu&itype=web&tn=02003390_42_hao_pg&ie=utf-8&wd=mac%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F")
    def test_add_teacher_2(self, login_xadmin_fix, delete_teacher_sql):
        s = login_xadmin_fix
        result = add_teacher(s, name="夏小小2")
        # 判断
        actul_result = get_add_result(result)
        assert actul_result == "夏小小2"