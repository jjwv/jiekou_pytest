#-*- coding:utf-8 -*-
# Author  : Cuiwenhao
# Time    : 2020-03-05 12:35
# Software: PyCharm
import yaml
import os


def readyml(yamlPath):
    '''读取yaml文件内容
    realPath: 文件的真实绝对路径 '''
    if not os.path.isfile(yamlPath):
        raise FileExistsError("文件路径不存在，请检查路径是否正确：%s" % yamlPath)

    f = open(yamlPath,"r",encoding='utf-8')
    cfg = f.read()
    d = yaml.load(cfg)
    # 用load方法转字典
    print("读取的测试文件数据：%s" % d)
    return d



if __name__ == '__main__':
    data = readyml("/Users/cuiwenhao/Documents/接口自动化/jiekou_pytest/case/mokuai2 ")