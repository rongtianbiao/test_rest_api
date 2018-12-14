# coding=utf-8
import unittest
import time
import HTMLTestRunnerCN
from test_case import KFW_REST_API_02

if __name__ == "__main__":
    # 将test_case中的所有测试用例加到测试套中
    test_case_path = "./test_case"
    discover = unittest.defaultTestLoader.discover(test_case_path, pattern='KFW_REST_API_*.py', top_level_dir=None)
    # 定义输出报告的文件路径及名称
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = "./test_report/" + u"rest接口测试报告 " + now + ".html"
    with open(filename, "wb") as fp:
        runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title="防火墙rest接口测试报告", description="报告详情",
                                                 tester="荣天彪")
        runner.run(discover)