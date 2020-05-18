#-*- coding:utf-8 -*-
# Author  : Cuiwenhao
# Time    : 2020-03-09 09:15
# Software: PyCharm

import os,pytest,allure
from houzhi_cmdhost.add_teacher import *

def pytest_addoption(parser):
    parser.addoption(
        "--cmdhost",
        action="store",
        default="http://49.235.92.12:8020",
        help="test case project host address"
    )

@pytest.fixture(scope="session", autouse=True)
def host(request):
    '''获取命令行参数，给到环境变量'''
    os.environ["xadmin_host"] = request.config.getoption("--cmdhost")
    print("当前运行环境：%s"%os.environ["xadmin_host"])



@pytest.fixture(scope="session")
def login_xadmin_fix(request):
    s = requests.session()
    login_xadmin(s)

    def close_s():  # 关闭session
        s.close()
    request.addfinalizer(close_s)  # 终结
    return s


@pytest.fixture(scope="function")
def delete_teacher_sql():
    '''删除添加的老师'''
    sql = '''DELETE from djangoweb.hello_teacher WHERE teacher_name = '老师5xxx';'''
    # execute_sql(sql)
    yield
    print("测试用例之后执行")
    # execute_sql(sql)

