#-*- coding:utf-8 -*-
# Author  : Cuiwenhao
# Time    : 2020-03-05 09:13
# Software: PyCharm

import os
from common.read_yml import readyml

# 绝对路径
curPath = os.path.dirname(os.path.realpath(__file__))
print(curPath)
yamPath = os.path.join(curPath, "test_data.yml")
print(yamPath)
test_data = readyml(yamPath)['updata_info']
print(test_data)
