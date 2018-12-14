# coding=utf-8

# author: rongtianbiao
# time:2018-8-17
# 用例编号：KFW_REST_API_01
# 用例说明：获取域名白名单

# 接口名称 getDomainWhiteList(tornado.web.RequestHandler)
# 接收参数 {"domain":"www.a"}
#   字段   类型   解释
#  domain 字符串 域名

# 测试接口：http://192.168.88.26:16008/v1.0/firewall/getDomainWhiteList
# 测试步骤
# 1、输入参数： {"domain":"www.a"}   见结果1（与开发文档结果不一致）；
# 2、输入参数： {"domain": 111}    见结果1 （bug）；
# 3、输入参数： {"domain":"@#$"}    见结果1 （bug）；
# 4、输入参数   {"domain":"------"}  见结果1 （bug）；
# 结果
# 结果1、{"totalpage": 0, "err": 0, "list": [], "result": [], "total": 0, "page": 0, "size": 0}

import HTMLTestRunner
import unittest, time
from common.request_fun import schedul_fun
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

url = "http://192.168.88.26:16008/v1.0/firewall/getDomainWhiteList"
method = "post"


class Test1(unittest.TestCase):
    """
    定义的一个测试类
    """
    def setUp(self):
        self.url = url
        # 测试参数

    def test(self):
        """获取域名白名单:http://192.168.88.26:16008/v1.0/firewall/getDomainWhiteList"""
        pass

    def test01(self):
        """输入参数为：{"domain": "www.a"}"""
        data = {"domain": "www.a"}
        code = 0
        schedul_fun(self, method, self.url, data, code)

    def test02(self):
        """输入参数为：{"domain": 111}"""
        data = {"domain": 111}
        code = 1
        schedul_fun(self, method, self.url, data, code)

    def test03(self):
        """输入参数为： {"domain": "@#$"}"""
        data = {"domain": "@#$"}
        code = 1
        schedul_fun(self, method, self.url, data, code)

    def test04(self):
        """输入参数为： {"domain": "------"}"""
        data = {"domain": "------"}
        code = 1
        schedul_fun(self, method, self.url, data, code)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)



